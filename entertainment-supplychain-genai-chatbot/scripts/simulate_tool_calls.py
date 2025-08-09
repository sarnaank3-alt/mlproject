import random
import requests

# Configuration
API_URL = "http://localhost:8000/chat"  # Update with the actual API endpoint
TOOL_CALL_LIMIT = 25

def simulate_tool_calls(num_calls):
    if num_calls > TOOL_CALL_LIMIT:
        print(f"Exceeded tool call limit of {TOOL_CALL_LIMIT}.")
        return

    for i in range(num_calls):
        user_query = f"Simulated query {i + 1}"
        response = requests.post(API_URL, json={"message": user_query})

        if response.status_code == 200:
            print(f"Response {i + 1}: {response.json()}")
        else:
            print(f"Error on call {i + 1}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    num_calls_to_simulate = random.randint(1, 30)  # Simulate between 1 and 30 calls
    print(f"Simulating {num_calls_to_simulate} tool calls...")
    simulate_tool_calls(num_calls_to_simulate)