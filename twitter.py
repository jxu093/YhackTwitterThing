#!/usr/bin/env python

import requests
from requests_oauthlib import OAuth1
import json
twitter_key = "9aSjk9rhH9U9bDQyt1m9Jh3lz"
#alex_oauth_consumer_key="DC0sePOBbQ8bYdC8r4Smg"
#alex_oauth_consumer_secret="ze5pMwf3k7XuAYr2ZKgoGZQjgUXLuyfIVePkjDqiMlmgMG0oGB"
oauth_consumer_key="eKoZcY8kbsEFKYmMw8shguOYT"
oauth_consumer_secret="mBlreU1Uuj0AdFV40q2y1Cha7w1PsrMi7cB2wlzQajsakn0mWe"
oauth_access_token="254556588-NaI5yKZCQJhlvlXQKgNRfquQnjpKAokKNNAUuoQq"
oauth_access_secret="mkQZpH1hH3BpbtZFe3V1u9y7D4lEOWyKawRpwjJB5qURr"
#payload = {'Authorization': auth_key, 'Host':'api.twitter.com','X-Target-URI':'https://api.twitter.com','Connection':'Keep-Alive'}

def get_oauth():
    oauth = OAuth1(oauth_consumer_key,
                client_secret=oauth_consumer_secret,
                resource_owner_key=oauth_access_token,
                resource_owner_secret=oauth_access_secret)
    return oauth

def twit_search(query):
    #api_key = twitter_key
    url = 'https://api.twitter.com/1.1/search/tweets.json?q='+query
    oauth = get_oauth()
    #url = 'https://api.twitter.com/1.1/search/tweets.json?q=' +'?key=' + query+ twitter_key
    #results = twitter.search(q=query, count = 50)
    json_obj = requests.get(url,auth=oauth)
    #data = json.load(json_obj.text)
    data = json_obj.json()
    #for tweet in results['statuses']:
      #  print tweet['user'].encode('utf-8')
    #for item in data['statuses']:
     #   print item['user']
    #for item in data['statuses']:
        #print item['metadata']
    print data
    print json_obj.headers


twit_search('toronto')
