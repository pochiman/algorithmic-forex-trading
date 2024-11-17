from multiprocessing import Process
import time
import random

def run_process(name):
    print("PROCESS", name, "STARTED")

    time.sleep(random.randint(3, 8))

    print("PROCESS", name, "ENDED")

def run_processes():
    processes = []

    for i in range(4):
        processes.append(Process(target=run_process, args=(f"Pr_{i}",)))

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("ALL DONE")
