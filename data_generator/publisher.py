import uuid
import json
import sys
sys.path.append('../')

from rabbitmq.manager import publish  # NOQA


def publish_metric(start_time, end_time, no_of_records):
    start_time_epoch = int(start_time.timestamp() * 1000)
    end_time_epoch = int(end_time.timestamp() * 1000)
    time_taken = end_time_epoch - start_time_epoch

    event = {
        "id": str(uuid.uuid4()),
        "start_time": start_time_epoch,
        "time_taken": time_taken,
        "no_of_records": no_of_records
    }

    event_json = json.dumps(event)
    publish(event_json)
