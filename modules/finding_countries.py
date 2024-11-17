from models.models import IpCountry, IpPerfix, Country
from main import session


def is_public_ip_perfix(x_y_input):
    ip_perfix_object = session.query(IpPerfix).filter_by(ip_perfix = x_y_input).first()
    if ip_perfix_object:
        if ip_perfix_object.is_public:
            return True
    else:
        return False


def finding_countries_in_database(x_y_input):
    ip_perfix_id = session.query(IpPerfix).filter_by(ip_perfix = x_y_input).first().id
    ip_countries_obj = session.query(IpCountry).filter_by(ip_perfix_id = ip_perfix_id).all()
    if ip_countries_obj:
        countries = [ip_country_obj.country.name for ip_country_obj in ip_countries_obj]
        return countries
    else:
        return []


def finding_countries(x_y):
    if is_public_ip_perfix(x_y):
        return ', '.join(finding_countries_in_database(x_y))
    else:
        return {'message':'Enter a public ip perfix'}

