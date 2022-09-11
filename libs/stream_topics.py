import socket
import json
from os import environ
from pubsub_publisher import PublishMessage
from tweepy import Stream


consumer_key    = str(environ['CONSUMER_KEY'])
consumer_secret = str(environ['CONSUMER_SECRET'])
access_token    = str(environ['ACCESS_TOKEN'])
access_secret   = str(environ['ACCESS_SECRET'])

class TweetsListener(Stream):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, topic_id, project_id):
        self.topic_id = topic_id
        self.project_id = project_id

        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
        
    # we override the on_data() function in StreamListener
    def on_data(self, data):
        try:
            message = json.loads(data)
            msg = message['text'].encode('utf-8')
            print(msg)
            # self.client_socket.send( message['text'].encode('utf-8') )
            PublishMessage(msg, self.topic_id, project_id=self.project_id).run()

            return True
        except Exception as e:
            # return
            print("Error on_data: %s" % str(e))
        return True

    def if_error(self, status):
        print(status)
        return True
        
def send_tweets(keyword, topic_id, project_id):
    twtr_stream = TweetsListener(
        consumer_key, consumer_secret,
        access_token, access_secret,
        topic_id, project_id
    )

    twtr_stream.filter(track=keyword)
    
if __name__ == "__main__":
    send_tweets(['bjorka'], 'bjorka', 'gcp_project')
