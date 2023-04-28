from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://mineeshabrar:mineeshabrar@e-curricular.sv9lmse.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["dsa-app"]
    collection_name = db["dsa_email"]

    dsa_emails = collection_name.find({})
    for h in dsa_emails:
        print(h)
        
except Exception as e:
    print(e)