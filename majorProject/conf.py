from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

connection_string = "mongodb+srv://mineeshabrar:mineeshabrar@e-curricular.sv9lmse.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string, server_api=ServerApi('1'))
db = client["dsa-app"]

ObjectIdStudents = "644bc6df4fe71be145aadf0b"
ObjectIdClubs = "6448e7997a9e308e6440f264"
ObjectIdEvents = "644bc6984fe71be145aadf0a"