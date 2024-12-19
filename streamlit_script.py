import streamlit as st
from datetime import datetime
import time
import requests
import base64
import pandas as pd

def my_function():
    return f"Function executed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    url = "https://netgate.pepipost.com:8080/v1/mail/send"
 
    data = {
        "A": [1, 4, 7, 10],
        "B": [2, 5, 8, 11],
        "C": [3, 6, 9, 12]
    }
    df = pd.DataFrame(data)
    
    excel_filename = "content.xlsx"
    df.to_excel(excel_filename, index=False)
    
    with open(excel_filename, mode='rb') as file:
        excel_base64 = base64.b64encode(file.read()).decode('utf-8')
    
    payload = {
        "personalizations": [
            {
                "recipient": "sparmar@godrej.com",
                "recipient_cc": ["yashkhot@godrej.com", "aarushid@godrej.com"]
            }
        ],
        "from": {
            "fromEmail": "info@godrejinterio.com",
        },
        "subject": "Amazon Ratings and Reviews",
        "content": "Hi, PFA the Ratings and Reviews Dump for Amazon",
        "templateId": 33201,
        "attachments": [
            {
                "fileContent": excel_base64,
                "fileName": "RatingsAndReviews.xlsx"
            }
        ]
    }
    
    headers = {
        "api_key": "50b39b265e9b8cca8a264652a27b57ef",
        "Content-Type": "application/json",
        "Accept": ""
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
    start_time = datetime.strptime("11:22:00", "%H:%M:%S").time()
    end_time = datetime.strptime("11:30:00", "%H:%M:%S").time()

    if start_time <= current_time <= end_time:
        result = my_function()
        log_placeholder.write(result)
        status_placeholder.info("Function executed successfully!")
        time.sleep(60)  # Wait for 60 seconds
    else:
        status_placeholder.warning("Waiting for the time range...")
        time.sleep(10)  # Check again in 10 seconds
