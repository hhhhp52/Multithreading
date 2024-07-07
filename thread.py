import threading
import time
import queue
import random


class AutoIntegerSelfHandlingMachine:

    def __init__(
            self,
            terminate_time: int = 10,
            queue_maxsize: int = 10,
            producer_execute_time: float = 0.1,
            consumer_execute_time: float = 0.15
    ):
        """
        :param terminate_time: The time for the program running time.
        :param queue_maxsize: Set the queue max size.
        :param producer_execute_time: Set the time for putting the data from the queue
        :param consumer_execute_time:  Set the time for getting the data from the queue
        """
        self.flag = True
        self.consumer_execute_time = consumer_execute_time
        self.producer_execute_time = producer_execute_time
        self.lock = threading.Lock()
        self.terminate_time = terminate_time
        self.queue = queue.Queue(maxsize=queue_maxsize)

        # Operation for check the lock is safe.
        # self.operation = list()

    def producer(self):
        while self.flag:
            with self.lock:
                if not self.queue.full():
                    # self.operation.append(0)
                    number = random.randint(1, 100)
                    # print(f"Producer the number: {number}")
                    self.queue.put(number)
                    # self.operation.append(1)
            time.sleep(self.producer_execute_time)

    def consumer(self):
        while self.flag:
            with self.lock:
                if not self.queue.empty():
                    # self.operation.append(0)
                    number = self.queue.get()
                    print(f"Consume the number: {number}")
                    # self.operation.append(2)
            time.sleep(self.consumer_execute_time)

    def starter(self):
        # Set the producer and consumer to thread
        p = threading.Thread(target=self.producer)
        c = threading.Thread(target=self.consumer)
        print(f"Start The Job, And Terminate After {self.terminate_time} Seconds")

        # Start the thread
        p.start()
        c.start()

        # Run the program for terminate time
        time.sleep(self.terminate_time)
        self.flag = False

        # Terminate the threads
        p.join(timeout=1)
        print("terminate the producer")
        c.join(timeout=1)
        print("terminate the consumer")


if __name__ == '__main__':
    m = AutoIntegerSelfHandlingMachine()
    m.starter()
    print("Finish the program.")
