import tweepy
from tweepy.auth import OAuthHandler
from tweepy import Stream
import socket
import json

consumer_key    = 
consumer_secret = 
access_token    = 
access_secret   = 

class TweetsListener(Stream):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, csocket):
        self.client_socket = csocket

        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret)
    # we override the on_data() function in StreamListener
    def on_data(self, data):
        try:
            message = json.loads( data )
            print( message['text'].encode('utf-8') )
            self.client_socket.send( message['text'].encode('utf-8') )
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def if_error(self, status):
        print(status)
        return True
        
 def send_tweets(c_socket, topics):
    twtr_stream = TweetsListener(
        consumer_key, consumer_secret,
        access_token, access_secret,
        csocket=c_socket
    )
    
    twtr_stream.filter(track=topics)
    
 if __name__ == "__main__":
    new_skt = socket.socket()         # initiate a socket object
    host = "127.0.0.1"     # local machine address
    port = 5559           # specific port for your service.
    new_skt.bind((host, port))        # Binding host and port

    print("Now listening on port: %s" % str(port))

    new_skt.listen(5)                 #  waiting for client connection.
    c, addr = new_skt.accept()        # Establish connection with client. it returns first a socket object,c, and the address bound to the socket

    print("Received request from: " + str(addr))
    # and after accepting the connection, we aill sent the tweets through the socket
    send_tweets(c, ['Chelsea'])
