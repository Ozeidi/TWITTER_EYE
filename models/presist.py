
from datetime import date, datetime
from models.base import Session, engine, Base, session
from models.tweet import Tweet
from models.tweet_mentions import Tweet_Mentions
from models.matching_rules import Matching_Rules


def presist_tweet(response):
    print(f'Pressist Repsponse: {response}')
    for i, ele in enumerate(response):
        print(f'Element: {ele}')
        
        #if i >4: break
        # add tweet to the database
        d =ele['data']
        # print(d)
        tweet_id_exist = session.query(Tweet).filter_by(tweet_id = d.get('tweet_id')).first()  is not None
        if not tweet_id_exist:
            try:
                ref_tw =ele['data']['referenced_tweets'][0]
            except:
                ref_tw={}
            tweet_rec = Tweet(d.get('id'),d.get('author_id'),  d.get('created_at'), d.get('text'), d.get('lang'), d.get('source'), d.get('reply_settings'), 
                                d.get('in_reply_to_user_id'), ref_tw.get('id'), ref_tw.get('type')) 
            session.add(tweet_rec)

        # add mentions to the database
        mentions = ele['includes']
        mentions = mentions.get('users', None)
        # print(mentions)
        if mentions is not None:
            for mention in mentions:
                user_id_exist = session.query(Tweet_Mentions).filter_by(user_id = d.get('user_id')).first()  is not None
                if not user_id_exist: 
                    tw_mention = Tweet_Mentions(d.get('id'), mention.get('id'), mention.get('name'),mention.get('username'))
                    tweet_rec.mentions = [tw_mention]
                    session.add(tw_mention)

        # Matching Rules
        matching_rules = ele['matching_rules']
        # mentions = mentions.get('users', None)
        for rule in matching_rules:
            rule_id_exist = session.query(Matching_Rules).filter_by(rule_id = rule.get('id')).first()  is not None
            if not rule_id_exist:
                rule_rec = Matching_Rules(rule['id'], rule['tag'])
                tweet_rec.matching_rules = [rule_rec]
                session.add(rule_rec)
        session.commit()    
