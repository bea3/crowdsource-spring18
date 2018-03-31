# Beatrice Garcia
# February 8, 2017
# Module 2 HW

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import csv
import sys


class StdOutListener(StreamListener):
    global f
    global writer
    global tweets
    count = 0

    def write_tweet(self, from_user, to_user, text):
        global writer
        writer.writerow([from_user, to_user, text])

        if self.count >= 100:
            sys.exit()

    def clean_text(self, text):
        text = text.encode("utf-8")
        text = text.strip()
        text = text.replace('\n', '')
        return text

    def on_data(self, data):
        global count
        data = json.loads(data)
        self.count += 1
        print self.count

        try:
            text = data['text'] if data['text'] is not None else ""
            text = self.clean_text(text)
        except KeyError or UnicodeEncodeError:
            return

        try:
            user_name = data['user']['screen_name'] if data['user']['screen_name'] is not None else ""
            user_name = self.clean_text(user_name)
        except:
            return

        self.write_tweet(data['id'], user_name, text)


def main():
    global f
    global writer

    with open('guns.csv', 'w') as f:
        writer = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["tweetid", "user", "text"])

        consumer_key = "FhiyBRb0cz4zOoDfcHNVOyBDS"
        consumer_secret = "Q7MsbrPbFVzrwztW2KFH5JDGVpnSMhBlztwfJrLQeIGG591LST"
        access_token = "755868887300780032-FqY1RAUiznqmVMToIotldxavDEKdEe9"
        access_secret = "DV3O14tD9nTR1cVThyY1wriLMarXQoNQoudbZMHnUxYBP"

        #set up access and get tweets
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        l = StdOutListener()
        stream = Stream(auth, l)
        stream.filter(track=['gun', 'guns'])

if __name__ == '__main__':
    main()


