import sys
import threading
sys.path.append('../')

from metrics_computer.consumer import init_consumer  # NOQA
from metrics_computer.streaming_processor import processor  # NOQA


def main():
    consumer = threading.Thread(target=init_consumer, name="consumer")
    consumer.start()

    stream_processor = threading.Thread(target=processor, name="stream_processor")
    stream_processor.start()

    consumer.join()
    stream_processor.join()


if __name__ == "__main__":
    main()
