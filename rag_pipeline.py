import os
import pandas as pd
from langchain_core.prompts import PromptTemplate
# from langchain.document_loaders import DataFrameLoader
from langchain_community.document_loaders import DataFrameLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI


# Env & paths
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DATA_PATH = "dayofaiusa_grades3_5_2025-10-15.csv"
DB_DIR    = "./chroma_db"

# Models
embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm_model       = ChatGoogleGenerativeAI(model="gemini-2.0-flash",
                                         temperature=0.75, top_p=0.8)

# Build or load Chroma vectorstore
if not os.path.isdir(DB_DIR) or not os.listdir(DB_DIR):
    df     = pd.read_csv(DATA_PATH)
    # Combine Title, Section and Text columns for better context
    df['content'] = df.apply(lambda x: f"{x['Title']}\n{x['Section']}\n{x['Text']}", axis=1)
    loader = DataFrameLoader(df, page_content_column="content")
    docs   = loader.load()
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding_function=embedding_model,
        persist_directory=DB_DIR
    )
    vectorstore.persist()
else:
    vectorstore = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding_model
    )

retriever = vectorstore.as_retriever()

# Instructional prompt template
rag_prompt = PromptTemplate.from_template("""
You are a helpful assistant for answering questions.

Use the following context to answer the question accurately.
Context:
{context}

Question:
{question}

Instructions:
- If the answer is not found in the context, respond with: "I could not find that information in the provided document."
- Keep your answer clear and under four sentences.
""")

# Main answering function
def answer_question(question: str) -> str:
    """
    Answers a question using retrieved context + Gemini.
    Returns plain text (no metadata formatting).
    """
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
        
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs[:5]])

    prompt = rag_prompt.format(context=context, question=question)
    response = llm_model.invoke(prompt)
    return getattr(response, "content", str(response))
