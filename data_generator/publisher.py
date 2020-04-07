import uuid
import json
import sys
sys.path.append('../')

from rabbitmq.manager import publish  # NOQA


def publish_metric(start_time, end_time):
    time_taken = end_time - start_time
    event = {
        "id": str(uuid.uuid4()),
        "start_time": start_time,
        "time_taken": time_taken
    }

    event_json = json.dumps(event)
    publish(event_json)
