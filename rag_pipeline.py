from langchain_groq import ChatGroq
from vector_database import faiss_db
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Step 1: Setup LLM (Using Deepseek R1 through Groq- Can you a more powerful model)

llm_model = ChatGroq(model = "llama-3.3-70b-versatile")

# Step 2: Retrieve Relevent Documents

def retrieve_docs(query):
    return faiss_db.similarity_search(query)

def get_context(documents):  # Storing all the relevent Info. to query in 1 doc
    context = "\n\n".join([doc.page_content for doc in documents])
    return context


#  Step 4: Answer Question

custom_prompt_template = """
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Question: {question} 
Context: {context} 
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt_template)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})
