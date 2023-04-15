from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client['dsaapp-db']
collection_name = db["student_student"]

students = collection_name.find({})
for student in students:
    print(student)
