pip install tweepy
import tweepy

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

def post_to_twitter(message):
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Post the tweet
    api.update_status(message)
    print("Tweet posted successfully!")

def main():
    message = input("Enter your tweet: ")
    post_to_twitter(message)

if __name__ == "__main__":
    main()
