import pandas as pd
from bson import ObjectId
from conf import *


df = pd.read_excel("C:/Users/Aabhas/Downloads/3rd year prof.xlsx")
students = df.to_dict(orient="records")

collection_name = db["students"]
query = collection_name.update_many({"_id": ObjectId(ObjectIdStudents)}, {"$set": {"students": students}}, upsert=True)
print("Documents updated:", query.modified_count)
