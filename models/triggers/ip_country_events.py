from sqlalchemy.orm import sessionmaker
from models.models import IpCountryLog
from sqlalchemy import inspect


# Define the listener functions


def log_ip_country_insertion(mapper, connection, target):

    session = sessionmaker(bind=connection)()

    log_entry = IpCountryLog(
        ip_country_id=target.id,
        changed_column='multiple columns',
        old_value='',  # For new insertions, there is no old value
        new_value='',
        operation="INSERT",
    )
    session.add(log_entry)

    session.commit()

def log_ip_country_deletion(mapper, connection, target):

    session = sessionmaker(bind=connection)()

    log_entry = IpCountryLog(
        ip_country_id=target.id,
        changed_column='',
        old_value='',  # For new insertions, there is no old value
        new_value='',
        operation="delete",
    )
    session.add(log_entry)

    session.commit()



