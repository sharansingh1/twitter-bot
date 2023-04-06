import tweepy
import time

api_key = "M9ZBkRTOh1xmBshW5xRmzR0NG"
api_secret = "Ip7JHjNLBqHivZ3MclnrU5r1jsslDXX8RLBCy9dOsD7tJQnvUB"
bearer = "AAAAAAAAAAAAAAAAAAAAAKv7iAEAAAAA%2BbqpM%2FwsfbX5z0kbty9Dk1Eothc%3D1Yzy8CBfLPSi22GWkLbLcxFH0toprk4JCa0PGzM7oym20kUxTR"
access_token = "1581709222458187777-tZQgbeG1tF7eTcEq0wOLw3vRx52U1n"
access_token_secret = "spuADcg5vWzZVc8DE9AHQSukYGNw8R9ag1DBqFgQBQN7T"

client = tweepy.Client(bearer, api_key, api_secret, access_token, access_token_secret)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

person = client.get_user(username="jackharlowjr").data.id

for tweet in client.get_users_tweets(person).data:
    print(tweet.text)

search_terms = ["python", "programming", "coding"]