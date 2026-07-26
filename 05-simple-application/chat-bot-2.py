from pathlib import Path
from groq import Groq


def load_api_key():
    base_dir = Path(__file__).resolve().parent.parent

    candidate_paths = [
        base_dir / "key-vault" / "groq" / "api.key",
        base_dir / "key-vault" / "huggingface" / "groq" / "api.key",
    ]

    for path in candidate_paths:
        if path.exists():
            return path.read_text().strip()

    raise FileNotFoundError(
        "API key file not found. Expected one of: "
        + ", ".join(str(p) for p in candidate_paths)
    )


API_KEY = load_api_key()
client = Groq(api_key=API_KEY)
MODEL_NAME = "llama-3.1-8b-instant"


def chat():
    print("Welcome to the chatbot!")
    print("Type 'exit', 'quit', or 'end' to stop the conversation.\n")

    conversation_history = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Keep responses concise and friendly.",
        }
    ]

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit", "end"}:
            print("AI: Goodbye!")
            break

        if not user_input:
            print("AI: Please enter a message.")
            continue

        conversation_history.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=conversation_history,
            )
            ai_message = response.choices[0].message.content
            print(f"AI: {ai_message}")
            conversation_history.append({"role": "assistant", "content": ai_message})
        except Exception as e:
            print(f"AI: Sorry, I encountered an error: {e}")


if __name__ == "__main__":
    chat()
