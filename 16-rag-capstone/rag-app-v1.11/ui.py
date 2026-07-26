import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/ask"

st.set_page_config(page_title="Medical Analysis Assistant", page_icon="🤖")

st.title("Medical Analysis Assistant")

query = st.text_input("Enter your query")

if st.button("Submit"):

    if not query.strip():
        st.error("Please enter a query.")

    else:
        try:
            response = requests.get(
                API_URL,
                params={"q": query},
                timeout=60
            )

            if response.status_code == 200:
                data = response.json()

                # Display the "answer" field returned by the backend
                st.success(data.get("answer", "No answer returned."))

            else:
                st.error(response.text)

        except Exception as e:
            st.error(f"Connection Error: {e}")
