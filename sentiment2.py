import tweepy
from textblob import TextBlob

consumer_key = 'sR25RGBpUx696JooEMtFkKG6V'
consumer_secret = 'tM5PMaj65VwlGdpc9H8zqqFkqxX8AaF6HtBJsgofaBOIUGsgqp'

access_token = '1105549460975902722-rzGdnKnD69TU7Z2XVZ8u4AuTGU34hj'
access_token_secret = 'Vrvb5XSMmdXqR7IS3WBKe9RCUmZkkr7pLwkVZAfCdeqOD'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('pathofexile')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
