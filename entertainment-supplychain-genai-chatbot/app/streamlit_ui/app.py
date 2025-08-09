from streamlit import st
import requests

# Streamlit app configuration
st.set_page_config(page_title="Entertainment Supply Chain GenAI Chatbot", layout="wide")

# Title of the app
st.title("Entertainment Supply Chain GenAI Chatbot")

# Session state to manage conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to call the backend API
def call_backend_api(user_input):
    response = requests.post("http://backend-service-url/api/chat", json={"message": user_input})
    return response.json()

# User input section
user_input = st.text_input("Ask me anything about the entertainment supply chain:")

if st.button("Send"):
    if user_input:
        # Call the backend API with user input
        response = call_backend_api(user_input)
        
        # Append user input and response to conversation history
        st.session_state.conversation.append({"user": user_input, "bot": response['answer']})

# Display conversation history
if st.session_state.conversation:
    for chat in st.session_state.conversation:
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")

# Feedback section
feedback = st.radio("Did this answer help?", ("Yes", "No"))
if st.button("Submit Feedback"):
    # Here you would send feedback to the backend
    feedback_response = requests.post("http://backend-service-url/api/feedback", json={"feedback": feedback})
    st.success("Thank you for your feedback!")