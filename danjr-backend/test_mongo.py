# test_mongo.py

from mongoengine import Document, StringField, connect
import jetTools  # your config helper

# Connect to MongoDB using your config
connect(host=jetTools.cfg["MongoAtlasDB"]["connstring"])

# Define a temporary test model
class Ping(Document):
    message = StringField()

# Insert a test document
test_doc = Ping(message="It works!")
test_doc.save()

# Retrieve and print it
for doc in Ping.objects:
    print(f"Retrieved from MongoDB: {doc.message}")
