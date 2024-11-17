from models.models import IpCountry
from sqlalchemy import create_engine, event
from models.base import Base
from sqlalchemy.orm import sessionmaker
from models.triggers.ip_country_events import log_ip_country_deletion, log_ip_country_insertion
from settings.settings import BASE_DIR


# Set up the engine for connecting to an SQLite database
DATABASE_PATH = f"{BASE_DIR}/ip_perfix_country_finder.sqlite"
engine = create_engine(f"sqlite:///{DATABASE_PATH}")

# Create a configured session class bound to the engine
Session = sessionmaker(bind=engine)  # This creates a factory for new Session objects
session = Session()  # Instantiate a new session for interacting with the database

# Create all tables defined in the Base's metadata; run this only once to set up the database schema
Base.metadata.create_all(engine)


event.listen(IpCountry, 'after_insert', log_ip_country_insertion)
event.listen(IpCountry, 'after_delete', log_ip_country_deletion)


