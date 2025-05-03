
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/ad303f2f-59d8-428a-acec-4c2a509c6f1b/api/v1/run/ee10b65d-db45-4098-b89e-2ebf28d13c3a"  

# Request payload configuration
payload = {
    "input_value": "Tell me about the product 201",  # The input value to be processed by the flow
    "output_type": "chat",  # Specifies the expected output format
    "input_type": "chat"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer "  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    