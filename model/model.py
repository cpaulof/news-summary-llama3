from llama_cpp import Llama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate


MODEL_PATH = './model/Meta-Llama-3-8B-Instruct.Q2_K.gguf'

llm = Llama(MODEL_PATH, n_ctx=8192)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=8192,
    chunk_overlap=50,
    length_function=len
)

def split_file(path):
    with open(path, 'r') as file:
        text = file.read()
        file.close()
    
    texts = text_splitter.create_documents([text])
    return texts

def split_text(text):
    texts = text_splitter.create_documents([text])
    return texts

template = """
    Write a concise summary of the text, return your response with a single paragraph that covers the key points of the text.
    ```{text}```
    SUMMARY:
    """
prompt_creator = PromptTemplate(template=template, input_variables=["text"])
def generate_prompt(chunk):
    return template.format(text=chunk)

def create_dialog(content):
    return [{'role': 'user', 'content': content}]

def get_prev_kp(content):
    return '\n'.join([i for i in content.splitlines() if i.startswith('*')])

def generate_summary(text):
    text_chunks = split_text(text)
    size = len(text_chunks)
    responses = []
    for i, chunk in enumerate(text_chunks):
        print(f"\n\nProcessing chunk {i+1} of {size}")
        dialog = create_dialog(generate_prompt(chunk.page_content))
        r = llm.create_chat_completion(dialog)
        content = r['choices'][0]['message']['content']
        responses.append(content)
    
    # with open('Results.txt', 'w') as file:
    #     file.write('\n\n'.join(responses))
    
    #     file.close()
    # return responses
    return '\n\n'.join(responses)

