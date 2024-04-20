import threading
from time import sleep


def thread_function():
    print("Start")
    sleep(2)
    print("End")


if __name__ == "__main__":
    print("Main_Loop: START")
    thread = threading.Thread(target=thread_function)
    print("Main_Loop: Before Running")
    thread.start()  # Start an Async task that is not part of main loop
    print("Main_Loop: Program is running")
    thread.join()  # Join the async task back to main loop
    print("Main_Loop: Compelte")
