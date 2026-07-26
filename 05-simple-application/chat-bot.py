# Imports
from groq import Groq

# Read API keys
with open(r"C:\Users\user\Desktop\Shubham-AI\Shared\ey-ai-upskill-10-main\ey-ai-upskill-10-main\key-vault\huggingface\groq\api.key", "r") as f:
    api_keys = f.read().strip()

# Initialize Groq client
client = Groq(api_key=api_keys)

# Select model
model = "llama-3.1-8b-instant"

# Chat function
def chat():

    # Welcome message
    print("Welcome to the chatbot!")
    print("How can I assist you today? (Type 'exit', 'quit', or 'end' to stop the conversation)")
    # Conversation history (list)
    conversation_history = []

    # Inifinite loop
    while True:
    
        # User input
        user_input = input("You: ")

        # Check for the exit condition (exit, quit, end)
        if user_input.lower() in ["exit", "quit", "end"]:
            print("AI: Goodbye!")
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Build a prompt using conversation history
        try:

            # Get the Groq response
            response = client.chat.completions.create(
                model=model,
                messages=conversation_history
            )

            # extract the output text
            ai_message = response.choices[0].message.content

            # print the output text
            print(f"AI: {ai_message}")

            # add the ai message into the conversation history as an object with a role
            conversation_history.append({"role": "assistant", "content": ai_message})

        except Exception as e:

            # Add an exception message
            print(f"AI: Sorry, I encountered an error: {str(e)}")

# run the chatbot
if __name__ == "__main__":
    chat()