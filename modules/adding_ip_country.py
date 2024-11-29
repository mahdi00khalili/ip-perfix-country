from models.models import Country, IpCountry, IpPerfix
from requests_html import HTML
from bs4 import BeautifulSoup
import requests
from modules.main import session
import time
from settings.config import proxies
from requests_html import HTMLSession

def convert_ip_to_perfix(ip):
    x, y, c, d = ip.split('.')
    return f'{x}.{y}'


def parse_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.select('#ip-address tbody tr')

    ip_perfixes = []
    for row in rows:
        cells = row.find_all('td')
        ip_perfix_start = convert_ip_to_perfix(cells[0].get_text(strip=True))  # First IP address
        ip_perfix_end = convert_ip_to_perfix(cells[1].get_text(strip=True))  # Second IP address
        ip_perfixes.extend([ip_perfix_start, ip_perfix_end])

    return set(ip_perfixes)


def check_not_exists(country_id, ip_perfix):
    ip_perfix_obj = session.query(IpPerfix).filter_by(ip_perfix=ip_perfix).first()
    if ip_perfix_obj:
        ip_country_obj = session.query(IpCountry).filter_by(ip_perfix_id=ip_perfix_obj.id,
                                                            country_id=country_id).first()
        if ip_country_obj:
            return False
        else:
            return ip_perfix_obj.id


def update_ip_country(country_name, ip_perfixes):
    country_obj = session.query(Country).filter_by(name=country_name).first()
    all_perfixes_for_country_in_db_obj = session.query(IpCountry).filter_by(country_id=country_obj.id).all()
    for ip_perfix in all_perfixes_for_country_in_db_obj:
        ip_perfix_obj = session.query(IpPerfix).filter_by(id=ip_perfix.ip_perfix_id).first()
        if ip_perfix_obj.ip_perfix not in ip_perfixes:
            session.delete(ip_perfix)
    session.commit()


def add_ip_country_for_one_country(country_name, ip_perfixes):
    country_object = session.query(Country).filter_by(name=country_name).first()
    if country_object:
        for ip_perfix in ip_perfixes:
            print(country_name, ': ', ip_perfix)
            check_ip_country = check_not_exists(country_object.id, ip_perfix)
            if check_ip_country:
                new_ip_country = IpCountry(country_id=country_object.id, ip_perfix_id=check_ip_country)
                session.add(new_ip_country)

    session.commit()


def get_ip_perfixes_by_country(country_name, html_content):
    ip_perfixes = parse_content(html_content)
    add_ip_country_for_one_country(country_name, ip_perfixes)
    update_ip_country(country_name, ip_perfixes)


def get_country_page_url(country_name):
    country_name_slug = '-'.join(country_name.split(' ')).lower()
    url = f'https://lite.ip2location.com/{country_name_slug}-ip-address-ranges'
    return url


def add_ip_country_for_all_countries():
    all_countries = session.query(Country).all()

    session_request = HTMLSession()

    for i, country in enumerate(all_countries):
        print(f'\n{country.name}')
        # Start the timer
        start_time = time.time()
        if proxies:
            response = session_request.get(get_country_page_url(country.name), proxies=proxies)
        else:
            response = session_request.get(get_country_page_url(country.name))

        response.html.render(wait=3, sleep=2, scrolldown=3)
        html_content = response.html.html
        print(len(html_content))

        get_ip_perfixes_by_country(country.name, html_content)
        end_time = time.time()  # End the timer

        print(f"Duration: {end_time - start_time:.5f} seconds")  # Calculate and print the duration


if __name__ == '__main__':
    add_ip_country_for_all_countries()
