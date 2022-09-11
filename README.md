# tweet_streamer
Streaming pipeline to listen some twitter keyword into Google Pub/Sub and host the data to BigQuery table. All process using streaming method. Enjoy!

# How to
- Create credentials in https://developer.twitter.com/en/products/twitter-api, then save it in secure note
- Clone this repos
- Create Google Cloud Platform Project
- Turn on Bigquery API and Pub/Sub API
- Generate Service account, and give it these permissions: 
  - BigQuery Data Editor
  - BigQuery Metadata Viewer
  - Pub/Sub Publisher
- Save Service account to your local device
- Create Pub/sub topic
- Create dataset and table in BigQuery with `data` column schema name
- `cd` to tweet_streamer repos in your local
- Run with command `./run.sh -k 'twitter_consumer_key' -s 'twitter_consumer_secret' -a 'twitter_access_token' -c 'twitter_access_secret' -p '/path/to/service_account.json'`
