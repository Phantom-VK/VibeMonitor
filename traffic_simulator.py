import requests
import random
import time

def start_traffic(url:str, requests_count:int = 100, min_delay = 0.1, max_delay = 1.0):

    print(f"Starting network traffic at {url}, total count = {requests_count}")

    for i in range(requests_count):
        try:
            response = requests.get(url)
            print(f"[{i + 1}/{requests_count}] Status: {response.status_code}, Response: {response.json()}")
        except Exception as e:
            print(f"{i+1}th request failed!:{e}")
        time.sleep(random.uniform(min_delay, max_delay))
    print("Traffic simulation completed!")


if __name__ == "__main__":
    target_url = "http://localhost:8000/"

    start_traffic(target_url, requests_count=50, min_delay=0.1, max_delay=0.5)