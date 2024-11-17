from models.models import Country
from modules.main import session
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from settings.settings import proxies



def parse_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all cards
    cards = soup.find_all('div', class_='card')

    # Loop through each card and extract data
    country_names = []
    for card in cards:
        # Find the country name and link
        country_tag = card.find('a')
        if country_tag:
            country_name = country_tag.text.strip()
            country_names.append(country_name)
    return country_names

def get_country_names():
    url = 'https://lite.ip2location.com/ip-address-ranges-by-country?lang=en_US'
    session_html = HTMLSession()
    # Set proxies for the session
    if proxies:
        session_html.proxies = proxies
    response = session_html.get(url)
    html_content = response.html.html
    return parse_content(html_content)


def save_countries_in_database():
    countries = get_country_names()
    if countries:
        for name in countries:
            country_obj = session.query(Country).filter_by(name=name).first()
            if not country_obj:
                print(name)
                new_country = Country(name=name)
                session.add(new_country)  # Add the new country object to the session
        session.commit()

if __name__ == '__main__':
    save_countries_in_database()
