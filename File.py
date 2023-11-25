import requests
import threading
import time

ascii_art = """
██     ██ ███████ ██████  ██   ██  ██████   ██████  ██   ██     ███████ ██████   █████  ███    ███ ███    ███ ███████ ██████  
██     ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██      ██      ██   ██ ██   ██ ████  ████ ████  ████ ██      ██   ██ 
██  █  ██ █████   ██████  ███████ ██    ██ ██    ██ █████       ███████ ██████  ███████ ██ ████ ██ ██ ████ ██ █████   ██████  
██ ███ ██ ██      ██   ██ ██   ██ ██    ██ ██    ██ ██  ██           ██ ██      ██   ██ ██  ██  ██ ██  ██  ██ ██      ██   ██ 
 ███ ███  ███████ ██████  ██   ██  ██████   ██████  ██   ██     ███████ ██      ██   ██ ██      ██ ██      ██ ███████ ██   ██ 
                                                                                                                              
                                                                                                                              """

print(ascii_art)

url = input("webhook url: ")
payload = input("enter the message you want to send: ")

message_counter = 0

def function():
    global message_counter
    message_counter += 1
    requests.post(url, json={'content': payload})
    print(f"message sent ({message_counter})")

while True:
    function()
    time.sleep(0.1) # Modify As You Please.