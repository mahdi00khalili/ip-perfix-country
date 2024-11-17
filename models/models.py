from sqlalchemy import ForeignKey, String, Column, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base


class IpPerfix(Base):
    __tablename__ = 'ip_perfix'

    id = Column(Integer, primary_key=True)
    ip_perfix = Column(String(255))
    is_public = Column(Boolean, default=True)

    # # Many-to-Many relationship with Country via IpCountry
    # countries = relationship("Country", secondary="ip_countries", backref="ip_prefixes")


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class IpCountry(Base):
    __tablename__ = 'ip_countries'

    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)
    ip_perfix_id = Column(Integer, ForeignKey('ip_perfix.id'), nullable=False)

    # Establish relationships
    country = relationship("Country", backref="ip_countries")
    ip_prefix = relationship("IpPerfix", backref="ip_countries")


class IpCountryLog(Base):
    __tablename__ = 'ip_country_logs'

    id = Column(Integer, primary_key=True)
    changed_column = Column(String(50))
    old_value = Column(String)
    new_value = Column(String)
    operation = Column(String)
    changed_at = Column(DateTime(timezone=False), default=func.now())

    ip_country_id = Column(Integer, ForeignKey('ip_countries.id'), nullable=False)  # ForeignKey added
