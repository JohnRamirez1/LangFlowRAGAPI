import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()


APPLICATION_TOKEN = os.environ.get("AUTH_TOKEN")


def run_flow(message: str) -> dict:
    api_url = f"https://api.langflow.astra.datastax.com/lf/d173a45f-a20f-4a7b-96b5-3508026c3056/api/v1/run/c8a779a3-62a1-4dc9-aacd-7c3ccb6ebfc5"
  

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")
    
    message = st.text_area("Message", placeholder="Ask something...")
    
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
    
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()