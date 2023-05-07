from .conf import *

def get_event_details(event_id):
    collection_name = db["events"]
    events = collection_name.find({})

    for event in events:
        if event["event_id"] == event_id:
            return event