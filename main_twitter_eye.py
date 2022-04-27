import requests
import os
import json
import time
from datetime import datetime,timezone
# For Security we are keeping these Confidential Data into Environment Variable
# Get Tweeter Bearer Token
from env import bearer_token
from rules import rules
from utils import flatten

# Model
from datetime import date, datetime
from models.base import Session, engine, Base, session
# from models.tweet import Tweet
# from models.tweet_mentions import Tweet_Mentions

from models.presist import presist_tweet

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(rules):

    payload = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(outputfile):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream?expansions=author_id&tweet.fields=author_id,created_at,in_reply_to_user_id,lang,referenced_tweets,reply_settings,source,text", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        # print(response_line)
        if response_line:
            json_response = json.loads(response_line)
            # print(json.dumps(json_response, indent=4, sort_keys=True))
            temp = json_response#json.dumps(json_response, indent=4, sort_keys=True)
            # try:
            #     json_response['data']['user'] = json_response['includes']['users'] 
            # except:
            #     json_response['data']['user'] = "KEY ERROR"
            #     print('Could not fetch users')
            # flatten_response =flatten(json_response['data'])
            # print(flatten_response)
            with open(outputfile, "a") as file:
                # Writing data to a file
                file.write(f"{temp}, \n")
            presist_tweet([temp])



def main():
    Base.metadata.create_all(engine)
    # Writing to file
    f = f"data/output_{datetime.now()}.json"
    with open(f, "w") as file:
        # Writing data to a file
        file.write("[ \n")
    old_rules = get_rules()
    delete_all_rules(old_rules)
    set_rules(rules)
    get_stream(f)


if __name__ == "__main__":
    # main()
    while True:
        try:
            main()
        except:
            print("Errror Occured")
            main()
