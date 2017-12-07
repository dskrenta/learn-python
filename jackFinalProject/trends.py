from state import load_states
from country import Country
from tweet import Tweet
from colors import get_sentiment_color
from geo import GeoPosition
import json
import codecs
# you may want to import more libraries here

# Please consult the tips & tricks document as well as piazza for help!

# You should copy and paste this main function to begin writing your program.
#def main():
#    sentiments = load_sentiments()    # a map from strings to float in (-1.0, +1.0) range
#    states = load_states()            # list of State instances
#    usa = Country(states, 1200)       # graphical rendering of Country (feel free to change the width)
#    # You should prompt the user for a search term.
#    # You should also implement a function to load the tweets using the json library
#    # to do this you should load the tweets from one of the .json files
#    # talk to one of the TA/CA/LAs if you want help understanding JSON format.
#    # Read more: https://docs.python.org/3/library/json.html
#    # here is a tutorial: http://docs.python-guide.org/en/latest/scenarios/json/
#    #
#    # You will also need to implement a function to load the sentiments.
#    # The sentiments file is in the following format:
#    # word, score
#    # word, score
#    # Make sure to save this data as the correct types!
#    # Some entries have multiple words (abandoned person,-0.375),
#    # You may ignore these entries.
#    #
#    # When you display the map of the USA, it will appear behind
#    # your spyder window.

def load_sentiments():
    return 0

def load_tweets(tweets_file_name):
    tweets = []
    tweets_file = codecs.open(tweets_file_name, 'r', 'utf-8')

    for line in tweets_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass

    tweets_file.close()
    return tweets

def main():
    sentiments = load_sentiments()
    states = load_states()
    tweets = load_tweets('data/tweets_with_time.json')
    # usa = Country(states, 1200)

    print tweets

    # tweets_file = open('data/tweets_with_time.json', 'r')
    # print tweets_file.read()
    # print tweets_file.read().encode('utf-8')
    # json.loads(tweets_file.read().encode('utf-8'))
    # decoded_file = json.loads(tweets_file.read().encode('utf-8'))

    # print tweets

    '''
    tweets = json.loads(tweets)

    for tweet in tweets:
        print tweet
    '''


#------------ your code should follow ------------

main()
