from queue import Queue
import random

queue = Queue()

def generate_request():
    request_count = random.randint(1, 10)
    for i in range(request_count):
        queue.put(i)

def process_request():
    if queue.empty():
        print("Queue is empty")
        return False
    else:
        request = queue.get()
        print(f"Processing request {request}")
        return True
    
def main():
    while True:
        try:
            generate_request()
            is_queue_not_empty = True
            while is_queue_not_empty:
                is_queue_not_empty = process_request()
        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

