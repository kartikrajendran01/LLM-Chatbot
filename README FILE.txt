After cloning the repository in your local add "models","db" folders to it.
Download "mistral-7b-instruct-v0.1.Q4_K_M.gguf" file from (https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/tree/main) and paste it in "models" folder.

File structure:
pdf-chatbot/
├── app.py
├── llm_setup.py
├── pdf_utils.py
├── vector_store.py
├── requirements.txt
├── models/
│  	 └── tinyllama.gguf   # Your downloaded TinyLlama GGUF model
└── db/                  # Vectorstore persistence


Install the requirements
pip install -r requirements.txt

To run:
 streamlit run app.py