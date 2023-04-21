from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client['dsaapp-db']
collection_name = db["student_student"]

students = collection_name.find({})
for student in students:
    print(student)


# "students": [
#     {
#       "sid": "19105115",
#       "name": "Aabhas",
#       "email": "aabhaschopra.bt19ele@pec.edu.in"
#       "prof": "saasc",
#       "event_ids": [
#         "ev1",
#         "ev2"
#       ]
#     },
#     {
#       "sid": "19105123",
#       "name": "Annchit",
#       "email": "annchitbhatnagar.bt19mech@pec.edu.in"
#       "prof": "music",
#       "event_ids": [
#         "mus1",
#         "mus2"
#       ]
#     }
#   ]





# "clubs": {
#     "saasc": [
#       "saasc1",
#       "saasc2"
#     ],
#     "music": [
#       "mus1",
#       "mus2",
#       "mus3"
#     ]
#   }





# "ev1": [
#     "19105115",
#     "19105123"
#   ],
#   "ev2": [
#     "19105115",
#     "19105053",
#     "19105118"
#   ]