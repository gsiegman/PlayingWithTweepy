from mongoengine import *

class TweetDoc(Document):
    author = StringField(required=True)
    tweet = StringField()
    created = StringField()
    source = StringField()

    