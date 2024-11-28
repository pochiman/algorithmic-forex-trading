import threading
import time
import random


class test_thread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):

        while True:
            print(self.name, "running stuff")
            time.sleep(random.randint(2,5))

def main():

    threads = []
    for i in range(3):
        t = test_thread(f"Thread {i}")
        t.daemon = True
        threads.append(t)
        t.start()

    try:
        for t in threads:
            t.join()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")

    print("OVER")

if __name__ == "__main__":
    main()
    