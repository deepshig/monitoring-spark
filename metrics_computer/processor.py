import sys
import threading
sys.path.append('../')

from metrics_computer.consumer import init_consumer  # NOQA
from metrics_computer.streaming_processor import processor  # NOQA
from metrics_computer.batch_processor import batch_processor  # NOQA


def main():
    consumer = threading.Thread(target=init_consumer, name="consumer")
    consumer.start()

    stream_processing = threading.Thread(
        target=processor, name="stream_processing")
    stream_processing.start()

    batch_processing = threading.Thread(
        target=batch_processor, name="batch_processing")
    batch_processing.start()

    consumer.join()
    stream_processing.join()
    batch_processing.join()


if __name__ == "__main__":
    main()
