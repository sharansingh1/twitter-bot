import tweepy


CONSUMER_KEY = 'XHxuNi89m13KfTGFzot1DByvA'
CONSUMER_SECRET = 'RL2fLilbmfA6fphWJzYBD09cQGKyzXBKTk6cIOxJMyIXvm1ziE'
ACCESS_KEY = '1581709222458187777-yZ20H6OlX1c8u4Ant7RJ2iPuNg2NYn'
ACCESS_SECRET = 'bjVvadxTckj4edD2HjJD7WhukJEPYqohLZxBpJE5at1Hi'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

#since_id = read_last_seen(FILE_NAME)
#create variable for tweets with mentions
tweets = api.mentions_timeline()

#loop to grab all tweets and their id/text
for tweet in reversed(tweets):
    if '#ultimatebot' in tweet.full_text.lower():
        print(str(tweet.id) + ' - ' + tweet.full_text)
        api.update_status("@" + tweet.user.screen_name + "AUTO REPLY IS WORKING!", tweet.id)
        store_last_seen(FILE_NAME, tweet.id)