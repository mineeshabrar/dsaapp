from .conf import *


def get_club_name(email):
    collection_name = db["societies"]
    clubs = collection_name.find({})

    for club in clubs:
        if club["email"] == email:
            return club["club_name"]
