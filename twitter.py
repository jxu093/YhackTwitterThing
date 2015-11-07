#!/usr/bin/env python

import requests
from requests_oauthlib import OAuth1
import json
twitter_key = "9aSjk9rhH9U9bDQyt1m9Jh3lz"

oauth_consumer_key="eKoZcY8kbsEFKYmMw8shguOYT"
oauth_consumer_secret="mBlreU1Uuj0AdFV40q2y1Cha7w1PsrMi7cB2wlzQajsakn0mWe"
oauth_access_token="254556588-NaI5yKZCQJhlvlXQKgNRfquQnjpKAokKNNAUuoQq"
oauth_access_secret="mkQZpH1hH3BpbtZFe3V1u9y7D4lEOWyKawRpwjJB5qURr"

tweet_list = []
def get_oauth():
    oauth = OAuth1(oauth_consumer_key,
                client_secret=oauth_consumer_secret,
                resource_owner_key=oauth_access_token,
                resource_owner_secret=oauth_access_secret)
    return oauth

def twit_search(query):
    url = 'https://api.twitter.com/1.1/search/tweets.json?q='+query
    oauth = get_oauth()
    json_obj = requests.get(url,auth=oauth)
    data = json_obj.json()

    for item in data['statuses']:
        tweet_list.append(item['text'])

    for i in range(0, len(tweet_list)):
        print '\n' + tweet_list[i]


twit_search('toronto')
