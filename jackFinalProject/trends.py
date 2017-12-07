from state import load_states
from country import Country
from tweet import Tweet
from colors import get_sentiment_color
from geo import GeoPosition
import json
import codecs

def load_sentiments():
    sentiments = {}
    sentiments_file = open('data/sentiments.csv', 'r')

    for line in sentiments_file:
        values = line.split(',')
        sentiments[values[0]] = float(values[1])

    return sentiments

def load_tweets(tweets_file_name):
    tweets = []
    tweets_file = codecs.open(tweets_file_name, 'r', 'utf-8')

    for line in tweets_file:
        try:
            tweet_dict = json.loads(line)
            tweets.append(
                Tweet(
                    tweet_dict['text'],
                    tweet_dict['created_at'],
                    GeoPosition(
                        tweet_dict['coordinates'][1],
                        tweet_dict['coordinates'][0]
                    )
                )
            )
        except:
            pass

    tweets_file.close()
    return tweets

def map_sentiment_to_state(tweets, sentiments, states, filter_terms):
    sentiment_color_map = {}
    filtered_tweets = []

    for tweet in tweets:
        tokens = tweet.message().split(' ')
        for token in tokens:
            for term in filter_terms:
                if token == term:
                    filtered_tweets.append(tweet)

    for tweet in filtered_tweets:
        tokens = tweet.message().split(' ')
        tweet_sentiment = 0.0

        for token in tokens:
            if token in sentiments:
                tweet_sentiment += sentiments[token]

        min_distance = 10000.0
        closest_state = ''

        for state in states:
            distance = tweet.position().distance(state.centroid())

            if distance < min_distance:
                min_distance = distance
                closest_state = state.abbrev()

        if closest_state in sentiment_color_map:
            sentiment_color_map[closest_state].append(tweet_sentiment)
        else:
            sentiment_color_map[closest_state] = [tweet_sentiment]

    for state in sentiment_color_map:
        average = 0.0

        for sentiment in sentiment_color_map[state]:
            average += sentiment

        average /= len(sentiment_color_map[state])
        sentiment_color_map[state] = get_sentiment_color(average)

    return sentiment_color_map

def main():
    input_terms = raw_input("Please enter search your filter terms separated by a comma: ")
    filter_terms = input_terms.split(',')
    sentiments = load_sentiments()
    states = load_states()
    # load all tweets
    tweets = load_tweets('data/tweets_with_time.json')
    sentiment_color_map = map_sentiment_to_state(tweets, sentiments, states, filter_terms)
    usa = Country(states, 1200)

    for state in sentiment_color_map:
        usa.setFillColor(state, sentiment_color_map[state])

main()
