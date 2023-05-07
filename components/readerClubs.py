import pandas as pd
from bson import ObjectId
from conf import *


df = pd.read_excel("C:/Users/DELL/Desktop/Lavanya/Societies.xlsx", dtype=str)

df["events"] = df["events"].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else []
)

clubs = df.to_dict(orient="records")

collection_name = db["societies"]
query = collection_name.insert_many(clubs)

print("Documents updated:", len(query.inserted_ids))
