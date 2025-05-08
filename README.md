After cloning the repo in your local add "models","db" folders to it.
Download "mistral-7b-instruct-v0.1.Q4_K_M.gguf" file and paste it in "models" folder.

File structure:

pdf-chatbot/

├── app.py

├── llm_setup.py

├── pdf_utils.py

├── vector_store.py

├── requirements.txt

├── models/

              └── mistral-7b-instruct-v0.1.Q4_K_M.gguf / tinyllama.gguf   # Your downloaded TinyLlama GGUF model

└── db/                  # Vectorstore persistence
