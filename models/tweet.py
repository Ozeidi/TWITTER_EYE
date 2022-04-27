
from sqlalchemy import Column, String, Text, Integer, BigInteger, Date, DateTime, Table, ForeignKey, column
from sqlalchemy.orm import relationship

from models.base import Base




tweet_mentions_association = Table(
    'tweet_mentions_association', Base.metadata,
    Column('tweet_id', BigInteger, ForeignKey('tweets.tweet_id')),
    Column('mention', BigInteger, ForeignKey('tweet_mentions.id'))
)

matching_rules_associdation = Table(
    'matching_rules_associdation', Base.metadata,
    Column('tweet_id', BigInteger, ForeignKey('tweets.tweet_id')),
    Column('matching_rule', BigInteger, ForeignKey('matching_rules.rule_id'))
)

class Tweet(Base):
    __tablename__ = 'tweets'

    #id = Column(BigInteger, primary_key=True)
    tweet_id = Column(BigInteger, primary_key=True)
    author_id= Column(BigInteger)
    created_at = Column(DateTime)
    text = Column(Text)
    lang = Column(String)
    source = Column(Text)
    reply_settings = Column(String)
    in_reply_to_user_id = Column(BigInteger)
    referenced_tweets_id = Column(BigInteger)
    referenced_tweets_type = Column(String)
    mentions = relationship("Tweet_Mentions", secondary=tweet_mentions_association)
    matching_rules = relationship('Matching_Rules', secondary=matching_rules_associdation)

    def __init__(self, tweet_id, author_id, created_at, text, lang, source, reply_settings, in_reply_to_user_id, referenced_tweets_id,referenced_tweets_type):
        self.tweet_id = tweet_id
        self.author_id = author_id
        self.created_at = created_at
        self.text = text
        self.lang = lang
        self.source  = source
        self.reply_settings = reply_settings
        self.in_reply_to_user_id = in_reply_to_user_id
        self.referenced_tweets_id = referenced_tweets_id
        self.referenced_tweets_type = referenced_tweets_type