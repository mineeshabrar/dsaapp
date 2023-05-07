import pandas as pd
from bson import ObjectId
from conf import *


df = pd.read_excel("C:/Users/Aabhas/Downloads/3rd year prof.xlsx", dtype=str)

df["events_organization"] = df["events_organization"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df["events_participation"] = df["events_participation"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
df["points"] = df["points"].fillna("")
df["email"] = df["email"].fillna("")

students = df.to_dict(orient="records")

collection_name = db["students"]
query = collection_name.insert_many(students)

print("Documents updated:", len(query.inserted_ids))
