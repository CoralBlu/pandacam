# import tweepy
import tweepy as tw

# your Twitter API key and API secret
my_api_key = "XXXXXXXXXXXXXXXXX"
my_api_secret = "XXXXXXXXXXXXXXXXXXXXXXX"

# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)
