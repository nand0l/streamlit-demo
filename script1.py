import streamlit as st
import requests

# API Gateway URL
api_url = "https://9tljevfbm6.execute-api.eu-west-1.amazonaws.com/Prod/"
st.title('API Gateway Integration')
# Button in Streamlit to trigger API
if st.button('Trigger API Gateway'):
    # Request to API Gateway
    resp = requests.get(api_url)

    # Success response handling
    if resp.status_code == 200:
        try:
            # Parse JSON and display
            response_text = resp.content.decode('utf-8')
            st.success('API Call Successful!')
            # Display decoded string
            st.text(response_text)
        except ValueError:
            # JSON parsing error
            st.error('Error decoding JSON response.')
    else:
        # API call failure handling
        st.error(f'API call failed. Status code: {resp.status_code}')
