import requests
import random
import time

def start_traffic(url:str, requests_count:int = 100, min_delay = 0.1, max_delay = 1.0):
    """
    Function to simulate traffic
    :param url: url on which we want to make traffic
    :param requests_count: count of requests to make to the url
    :param min_delay: min delay between each request
    :param max_delay: max delay between each request
    :return: None
    """

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