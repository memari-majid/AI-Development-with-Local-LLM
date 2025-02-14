# Disable tokenizers parallelism to avoid warnings.
# This setting is useful to avoid potential errors when running tokenizers in parallel threads.
import os
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

# Installation instructions:
# This script requires the following packages:
#   langchain
#   langchain-huggingface
#   langchain-community
#   ollama
# To install, run:
#   pip install langchain langchain-huggingface langchain-community ollama

# Import required LangChain components:

# For text embeddings using sentence transformers.
from langchain_huggingface import HuggingFaceEmbeddings

# For splitting documents into smaller chunks.
from langchain.text_splitter import CharacterTextSplitter

# Vector store using SQLite with vector similarity search.
from langchain_community.vectorstores import SQLiteVSS

# Document loader for PDFs using PyPDFLoader for robust PDF parsing.
from langchain_community.document_loaders import PyPDFLoader

# %%
# Determine the absolute path for the PDF file relative to the current script.
# This ensures the file is correctly referenced regardless of where the script is executed from.
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_pdf = os.path.join(current_dir, 'ignitebook-sample.pdf')

# Create a PyPDFLoader instance to load the PDF file.
# The loader parses the PDF and creates Document objects consisting of page content and metadata.
loader = PyPDFLoader(file_path_pdf)
# Automatically load and split the PDF into pages.
pages = loader.load_and_split()

# Print the total number of pages extracted from the PDF.
print("Page counts: ", len(pages))

# %%
# Initialize a text splitter to break down large text into manageable chunks.
# - chunk_size: Maximum number of characters per chunk (1000 characters here).
# - chunk_overlap: Number of overlapping characters between chunks (0 means no overlap).
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

# Split the PDF pages into smaller document chunks.
# This makes it easier to process large documents by dividing them into segments.
docs = text_splitter.split_documents(pages)

# Extract just the text content from each document chunk.
# The list 'texts' will later be used for embedding generation.
texts = [doc.page_content for doc in docs]

# %%
# Instantiate HuggingFaceEmbeddings with a pre-trained sentence transformer model.
# This model "all-MiniLM-L6-v2" is optimized for generating semantic embeddings.
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# %%
# Create a SQLite vector store database to store our text embeddings.
# Parameters:
# - texts: The list of text chunks produced from the PDF.
# - embedding: The embedding model that converts text into vector representations.
# - table: Name of the table ('ignite_book') used within the SQLite database.
# - db_file: File path to the SQLite database (located in the temporary directory).
db = SQLiteVSS.from_texts(
    texts=texts,
    embedding=embedding_function,
    table="ignite_book",
    db_file="/tmp/vss.db"
)

# %%
print("Loading finished!")

# %%
# Define the similarity (semantic search) query.
# This question will be used to retrieve relevant text chunks from our vector store.
question = "What is Data partitioning in Ignite?"
# Perform the similarity search on the vector store based on the semantically encoded question.
data = db.similarity_search(question)

# %%
# Print the content of the best matching document from the similarity search.
print(data[0].page_content)

# %%
# Import the ollama package to utilize the local large language model (LLM) for generating answers.
import ollama

# %%
# The 'data' variable now holds a list of documents that are semantically similar to the question.

# %%
# Concatenate the retrieved document contexts into one string.
# This combined context will provide an elaborate background for the answer generation.
context_str = " ".join([doc.page_content for doc in data])
print("Retrieved context:")
print(context_str)

# %%
# Build a prompt using the retrieved context combined with the original question.
# The prompt instructs the model to base its answer solely on the provided context,
# and to indicate if there's insufficient information.
prompt = f"""Use the following context to answer the question.
If you cannot find the answer in the context, say "I don't have enough information to answer this question."

Context:
{context_str}

Question: {question}

Answer:"""

print("Prompt:")
print(prompt)

# %%
# Generate an answer using Ollama's local LLM.
# The model "llama3.2" is used to process the prompt and generate a response.
response = ollama.generate(model="llama3.2", prompt=prompt)
print("Generated Answer:")
print(response['response'])


