from google.cloud import pubsub_v1
from google.oauth2 import service_account
from os import environ

class PublishMessage():

    def __init__(self, data, topic, **kwargs) -> None:
        self.data = data
        self.topic_id = topic
        self.project_id = kwargs['project_id']

    def run(self):
        credentials = service_account.Credentials.from_service_account_file(str(environ['PUBSUB_CREDS']))

        publisher = pubsub_v1.PublisherClient(credentials=credentials)

        # The `topic_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/topics/{topic_id}`
        topic_path = publisher.topic_path(self.project_id, self.topic_id)

        # Data must be a bytestring
        if not isinstance(self.data, bytes):
            self.data = self.data.encode("utf-8")
        
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, self.data)
        
        print(future.result())
        print(f"Published messages to {topic_path}.")
