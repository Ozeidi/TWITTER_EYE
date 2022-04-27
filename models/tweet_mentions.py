
from sqlalchemy import Column, PrimaryKeyConstraint, String, Text, Integer,BigInteger, Date, DateTime, Table, ForeignKey, column
from sqlalchemy.orm import relationship

from models.base import Base



class Tweet_Mentions(Base):
    __tablename__ = 'tweet_mentions'

    id = Column(BigInteger, primary_key=True)
    tweet_id = Column(BigInteger)
    user_id = Column(BigInteger)
    user_name = Column(Text)
    user_username = Column(Text)


    def __init__(self, tweet_id, user_id, user_name, user_username):
        self.tweet_id = tweet_id
        self.user_id = user_id
        self.user_name = user_name
        self.user_username = user_username