from langchain_community.document_loaders import PDFPlumberLoader  # uses the pdfplumber library under the hood to read PDFs page by page and extract clean text
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1: Upload & Load Raw PDF

pdfs_directory = 'pdfs/'

def upload_pdf(file):   # Func. Saves an Uploaded PDF file (from frontend) to a local folder
    with open(pdfs_directory + file.name, "wb") as f:   # wb= write in Binary Mode
        f.write(file.getbuffer())    # Copies the Uploaded file's raw bytes into your local storage in a new file


def load_pdf(file_path):  # Used to Read & Extract text from a PDF File

    loader = PDFPlumberLoader(file_path)
    documents = loader.load() # returns a list of Document objects & Each Document typically represents one page of the PDF
    return documents


# Testing
file_path = 'act3.pdf'
documents =  load_pdf(file_path)
# print(len(documents))

# Step 2: Creating Chunks
def create_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size= 1000,
        chunk_overlap = 200,
        add_start_index = True
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

text_chunks = create_chunks(documents)
# print("Chunk Count: ", len(text_chunks))


# Step 3: Setting Up Embedding Model (Using Deepseek R1 with Ollama)
ollama_model_name="deepseek-r1:7b"

def get_embedding_model(ollama_model_name):
    embeddings = OllamaEmbeddings(model=ollama_model_name)
    return embeddings

# Step 4: Index Documents (Storing Embedding in VectorDB - FAISS)
FAISS_DB_PATH = "vectorstore/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, get_embedding_model(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)
