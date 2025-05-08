from langchain_community.llms import LlamaCpp

def load_llm(model_path="models\mistral-7b-instruct-v0.1.Q4_K_M.gguf"):           # can be replaced by tinyllama(for faster response but it gived shalow and genric repsonse,but mistral gives Detailed, context-aware )
    return LlamaCpp(
        model_path=model_path,
        n_ctx=4096,             #no of token the model can see once
        max_tokens=1024,        #max token to generate in a response
        temperature=0.7,        #randomness
        top_p=0.95,             #used for selecting most likely token from the probability
        verbose=True            #prints model loading and inference details 
    )


####### LlamaCpp #######
# allows to load anf interact with models like LLaMA ,Mistral,TinyLlama and others locally
# no API key is required for this
# it works with .gguf files- helps for fast inference


