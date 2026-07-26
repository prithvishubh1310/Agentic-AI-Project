from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


from dotenv import load_dotenv
load_dotenv()

# keypath = r"C:\Users\user\Desktop\Shubham-AI\Shared\ey-ai-upskill-10-main\ey-ai-upskill-10-main\key-vault\huggingface\openai\api.key"
# with open(keypath) as f:
#     api_key = f.read().strip()

def get_retriever():
    # embeddings = OpenAIEmbeddings(api_key=api_key)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2" # Embedding model from Hugging Face
    )

    db = FAISS.load_local(
        "vectorstore/",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_kwargs={"k": 20}  # top 4 chunks
    )

    return retriever