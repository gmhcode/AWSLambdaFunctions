import time


def hello(event, context):
    print("First Update!")
    time.sleep(4)
    return "hello-world"
    
