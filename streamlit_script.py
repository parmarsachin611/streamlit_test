import streamlit as st
from datetime import datetime
import time

def my_function():
    # Your function logic here
    return f"Function executed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Streamlit app
st.title("Scheduled Function Execution")

# Display current status
status_placeholder = st.empty()
log_placeholder = st.empty()

while True:
    current_time = datetime.now().time()
    start_time = datetime.strptime("00:15:00", "%H:%M:%S").time()
    end_time = datetime.strptime("00:45:00", "%H:%M:%S").time()

    if start_time <= current_time <= end_time:
        result = my_function()
        log_placeholder.write(result)
        status_placeholder.info("Function executed successfully!")
        time.sleep(60)  # Wait for 60 seconds
    else:
        status_placeholder.warning("Waiting for the time range...")
        time.sleep(10)  # Check again in 10 seconds
