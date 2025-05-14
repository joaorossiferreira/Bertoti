import ollama
from interfaces.gradio_ui import create_interface

def verify_ollama():
    try:
        ollama.list()
        return True
    except:
        print("Erro: Ollama não está rodando. Por favor execute 'ollama serve' primeiro.")
        return False

if __name__ == "__main__":
    if verify_ollama():
        create_interface().launch(server_port=7860)