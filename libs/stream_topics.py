import argparse
import json
from os import environ
from pubsub_publisher import PublishMessage
from sentiment_analysis import SentimentAnalysis
from tweepy import Stream


consumer_key    = str(environ['CONSUMER_KEY'])
consumer_secret = str(environ['CONSUMER_SECRET'])
access_token    = str(environ['ACCESS_TOKEN'])
access_secret   = str(environ['ACCESS_SECRET'])

class TweetsListener(Stream):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, **kwargs):
        self.topic = kwargs['topic']
        self.project_id = kwargs['project_id']

        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)

    # we override the on_data() function in StreamListener
    def on_data(self, data):
        try:
            message = json.loads(data)
            
            msg = message['text'].encode('utf-8')
            
            SentimentAnalysis(msg).analyze()
            
            PublishMessage(msg, self.topic, project_id=self.project_id).run()

            return True
        except Exception as e:
            print("Error on_data: %s" % str(e))
        
        return True

    def if_error(self, status):
        print(status)
        
        return True
        
def send_tweets(keyword, project_id):
    twtr_stream = TweetsListener(
        consumer_key, 
        consumer_secret,
        access_token, 
        access_secret,
        topic=keyword, 
        project_id=project_id
    )

    twtr_stream.filter(track=keyword)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str)
    args = parser.parse_args()

    send_tweets([args.topic], 'your-gcp-project-id')
