from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client['dsaapp-db']
collection_name = db["student_student"]

students = collection_name.find({})
for student in students:
    print(student)


# {
#   "students": [
#     {
#       "sid": "19105115",
#       "name": "Aabhas",
#       "prof": "saasc",
#       "email": "aabhaschopra.bt19ele@pec.edu.in",
#       "event_organization": [
#         "ev1",
#         "ev2"
#       ],
#       "event_participation": [
#         "ev3"
#       ],
#       "points": ""
#     },
#     {
#       "sid": "19105123",
#       "name": "Annchit",
#       "prof": "music",
#       "email": "annchitbhatnagar.bt19mech@pec.edu.in",
#       "event_organization": [
#         "mus1",
#         "mus2"
#       ],
#       "event_participation": [
#         "mus3",
#         "mus4"
#       ],
#       "points": ""
#     }
#   ]
# }





# {
#   "clubs": {
#     "saasc": [
#       {
#         "name": "pecmun",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu",
#         "event_organization": [
#           "19105115",
#           "19105118"
#         ],
#         "event_participation": [
#           "19105123",
#           "19105113"
#         ],
#         "event_id": "saasc2301"
#       },
#       {
#         "name": "geoquiz",
#         "description": "isegvkjaebjfdbciaebjviajbDKCfbaSKUFB",
#         "event_organization": [
#           "19105111",
#           "19105123"
#         ],
#         "event_participation": [
#           "19104011",
#           "19105120"
#         ],
#         "event_id": "saasc2302"
#       },
#       {
#         "name": "intrapec",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu",
#         "event_organization": [
#           "19105115",
#           "19105118"
#         ],
#         "event_participation": [
#           "19105123",
#           "19105113"
#         ],
#         "event_id": "saasc2303"
#       },
#       {
#         "name": "Cognition",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu",
#         "event_organization": [
#           "19105115",
#           "19105118"
#         ],
#         "event_participation": [
#           "19105123",
#           "19105113"
#         ],
#         "event_id": "saasc2304"
#       }
#     ],
#     "music": [
#       {
#         "name": "dastak",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu",
#         "event_organization": [
#           "19105115",
#           "19105118"
#         ],
#         "event_participation": [
#           "19105123",
#           "19105113"
#         ],
#         "event_id": "music2301"
#       },
#       {
#         "name": "aagaz",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu",
#         "event_organization": [
#           "19105115",
#           "19105118"
#         ],
#         "event_participation": [
#           "19105123",
#           "19105113"
#         ],
#         "event_id": "music2302"
#       },
#       {
#         "name": "chords",
#         "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqu",
#         "event_organization": [
#           "19105115",
#           "19105118"
#         ],
#         "event_participation": [
#           "19105123",
#           "19105113"
#         ],
#         "event_id": "music2303"
#       }
#     ]
#   }
# }



# "ev1": [
#     "19105115",
#     "19105123"
#   ],
#   "ev2": [
#     "19105115",
#     "19105053",
#     "19105118"
#   ]




# head_email
#
# {"emails" : ["aabhaschopra.bt19ele@pec.edu.in"]}