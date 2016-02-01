import sys, os
import tweepy

# File with colon-separaten consumer/access token and secret
consumer_file='twitter.consumer'
access_file='twitter.access'

def __load_auth(file):
    if os.path.exists(file):
        with open(file) as f:
            tokens = f.readline().replace('\n','').replace('\r','').split(':')
        if len(tokens) == 2:
            return tokens[0],tokens[1]
        else:
            raise ValueError("Expecting two colon-separated tokens")
    else:
        raise IOError("File not found: %s" % file)

def twit(message, secret_dir='/secret'):
    #
    # Load the twitter consumer and access tokens and secrets
    consumer_token, consumer_secret = __load_auth(os.path.join(secret_dir, consumer_file))
    access_token, access_secret = __load_auth(os.path.join(secret_dir, access_file))
    #
    # Perform OAuth authentication
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    #
    # Create the API and post the status update
    try: 
        api = tweepy.API(auth)
        api.update_status(message)
    except tweepy.error.TweepError:
        print "Failed to post status update"
        print "Using:"
        print "  consumer[%s][%s]" % (consumer_token, consumer_secret)
        print "  access[%s][%s]" % (access_token, access_secret)

if __name__ == '__main__':
    tokens = sys.argv[1:]
    #
    twit(' '.join(tokens))
