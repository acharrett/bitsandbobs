#!/usr/bin/python3

# https://python-twitter.readthedocs.io/en/latest/twitter.html#module-twitter.api
import twitter

configs = {}
configs['consumer_key'] = 'abc'
configs['consumer_secret'] = 'def'
configs['access_token'] = 'ghi'
configs['access_token_secret'] = 'jkl'

twitter_api = twitter.Api(consumer_key=configs['consumer_key'],
                          consumer_secret=configs['consumer_secret'],
                          access_token_key=configs['access_token'],
                          access_token_secret=configs['access_token_secret'])

followers = twitter_api.GetFollowers()

for follower in followers:
    print(follower.name + " | " + follower.screen_name)

