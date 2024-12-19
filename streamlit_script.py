import streamlit as st
from datetime import datetime
import time
import requests

def my_function():
    
    url = "https://netgate.pepipost.com:8080/v1/mail/send"
 
    payload = {
        "from": {
            "email": "lesley.knope@parksnrec.com",
            "name": "Lesley Knope"
        },
        "reply_to": {
            "email": "ron.swanson@shutthegovernment.com",
            "name": "Ron Swanson"
        },
        "subject": "Tribute to Lil'Sebastian",
        "content": [
            {
                "value": "Andy Dwyer & Mouse Rat will be singing a tribute song for our Lil'Sebastian.",
                "type": "text/plain"
            }
        ],
        "personalizations": [
            {
                "to": {
                    "email": "april.ludgate@parksnrec.com",
                    "name": "April Ludgate"
                },
                "cc": {
                    "email": "ann.perkins@parksnrec.com",
                    "name": "Ann Perkins"
                },
                "bcc": {
                    "email": "ben.white@parksnrec.com",
                    "name": "Ben White"
                },
                "subject": "Tribute to Lil'Sebastian"
            }
        ],
        "mail_settings": {
            "bcc": {
                "enable": True,
                "email": "rob.lowe@parksnrec.com"
            },
            "footer": {
                "enable": True,
                "text": "This is a footer",
                "html": "<p>This is a footer</p>"
            }
        },
        "tracking_settings": {
            "click_tracking": { "enabled": True },
            "open_tracking": { "enabled": True },
            "subscription_tracking": { "enabled": True }
        }
    }
    headers = {
        "api_key": "<API KEY>",
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(response.json())

    return f"Function executed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Streamlit app
st.title("Scheduled Function Execution")

# Display current status
status_placeholder = st.empty()
log_placeholder = st.empty()

while True:
    current_time = datetime.now().time()
    start_time = datetime.strptime("11:16:00", "%H:%M:%S").time()
    end_time = datetime.strptime("11:18:00", "%H:%M:%S").time()

    if start_time <= current_time <= end_time:
        result = my_function()
        log_placeholder.write(result)
        status_placeholder.info("Function executed successfully!")
        time.sleep(60)  # Wait for 60 seconds
    else:
        status_placeholder.warning("Waiting for the time range...")
        time.sleep(10)  # Check again in 10 seconds
