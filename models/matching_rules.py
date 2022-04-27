
from sqlalchemy import Column, PrimaryKeyConstraint, String, Text, Integer,BigInteger, Date, DateTime, Table, ForeignKey, column
from sqlalchemy.orm import relationship

from models.base import Base



class Matching_Rules(Base):
    __tablename__ = 'matching_rules'

    rule_id = Column(BigInteger, primary_key=True)
    rule_tag = Column(Text)


    def __init__(self, rule_id, rule_tag):
        self.rule_id = rule_id
        self.rule_tag = rule_tag