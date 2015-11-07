#!/usr/bin/env python

import requests, json

apiurl = "https://api.havenondemand.com/1/api/sync/analyzesentiment/v1"
apikey = "49ee1576-46eb-424a-b963-d50c2a4c4397"

def getSentiment(type, data):
    """ Gets the sentiment of a single string or a url.
        @param {string} types Use either text or url.
        @param {string} data
    """
    language = "eng"

    params = {'apikey':apikey, type:type, 'language':language, type:data}
    r = requests.get(apiurl, params=params)

    response = json.loads(r.text)
    #print json.dumps(r.text, sort_keys=True, indent=4, separators=(',', ': '))

    return response

def getSentiments(tweets):
    """Gets the seniment of a list of strings.
       @param {list} tweets
    """
    params = {'apikey':apikey, type:'text'}
    url = apiurl
    for tweet in tweets: # build a string since a dict can't have the same key multiple times
        url += '?text=' + tweet
    r = requests.get(url, params=params)
    response = json.loads(r.text)
    return response
    

def parseResponse(response):
    """ Parses the positive and negative results into a single list of Topic:Score pairs."""
    sentiments = []
    for section in ['positive','negative']:
        for item in response[section]:
            print item['topic'] + ' ' + str(item['score'])
            sentiments.append({item['topic']:item['score']})
    return sentiments
	   
def test():
    " you can delete this".
    url = "http://docs.python-requests.org/en/latest/user/quickstart/"
    #    response = getSentinent('url', url)
    response = getSentiment('text', 'I am really annoyed with your poor performance recently. I like cheese.')
    return parseResponse(response)

def test2():
    tweets = ['TWeet1 sample text', 'I m really annoyedwith your poor performance recently.', 'Tweet 3 is the best tweet.']
    response = getSentiments(tweets)
    return parseResponse(response)

print test2()



