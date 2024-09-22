import time
import threading
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, time_window):
        # Store the maximum number of requests allowed and the time window in seconds
        self.max_requests = max_requests
        self.time_window = time_window
        # A dictionary to track user requests (user_id: [timestamps of requests])
        self.user_requests = defaultdict(list)
        # A lock to ensure thread safety in a concurrent environment
        self.lock = threading.Lock()

    def allow_request(self, user_id):
        current_time = time.time()

        with self.lock:
            # Get the list of request timestamps for the user
            if user_id in self.user_requests:
                requests = self.user_requests[user_id]
            else:
                requests = []

            # Filter out requests that are outside the time window
            valid_requests = [req_time for req_time in requests if current_time - req_time < self.time_window]
            self.user_requests[user_id] = valid_requests

            # Check if the user has exceeded the allowed number of requests
            if len(valid_requests) < self.max_requests:
                # If not exceeded, allow the request and add the current timestamp
                self.user_requests[user_id].append(current_time)
                return True
            else:
                # Otherwise, deny the request
                return False

# Example Usage
rate_limiter = RateLimiter(max_requests=5, time_window=60)  # 5 requests per 60 seconds

def simulate_request(user_id):
    if rate_limiter.allow_request(user_id):
        print(f"Request allowed for user {user_id}")
    else:
        print(f"Request denied for user {user_id}")

# Simulate multiple users making requests
user_id = 'user_1'
for _ in range(7):  # Simulate 7 requests
    simulate_request(user_id)
    time.sleep(10)  # Sleep for 10 seconds between requests
