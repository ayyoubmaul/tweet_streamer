from google.cloud import language_v1
from google.oauth2 import service_account
from os import environ


class SentimentAnalysis():

    def __init__(self, text_content):
        self.text_content = text_content

    def analyze(self):
        """
        Analyzing Sentiment in a String

        Args:
        text_content The text content to analyze
        """
        creds = service_account.Credentials.from_service_account_file(str(environ['PUBSUB_CREDS']))
        
        client = language_v1.LanguageServiceClient(credentials=creds)

        # Available types: PLAIN_TEXT, HTML
        type_ = language_v1.Document.Type.PLAIN_TEXT
        
        document = {"content": self.text_content, "type_": type_}

        encoding_type = language_v1.EncodingType.UTF8

        response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
        
        output = {}

        output['text'] = self.text_content
        output['overall_sentiment'] = response.document_sentiment.score
        output['overall_magnitude'] = response.document_sentiment.magnitude
        output['language'] = response.language

        print(output)

        return output
