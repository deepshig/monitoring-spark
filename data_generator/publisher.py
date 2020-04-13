import uuid
import json
import sys
sys.path.append('../')

from rabbitmq.manager import publish  # NOQA


def publish_metric(start_time, end_time, no_of_records):
    time_taken = end_time - start_time
    event = {
        "id": str(uuid.uuid4()),
        "start_time": start_time,
        "time_taken": time_taken,
        "no_of_records": no_of_records
    }

    event_json = json.dumps(event)
    publish(event_json)
