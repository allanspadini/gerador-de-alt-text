import gradio as gr
import base64
from io import BytesIO
import requests


def processa_imagem(imagem):
    buffer = BytesIO()
    imagem.save(buffer, format='PNG')
    buffer.seek(0)
    imagem_base64 = base64.b64encode(buffer.getvalue()).decode()
    info = {
        "stream": False,
        "image_data":[{"id":10,"data":imagem_base64}],
        "prompt":"You are an AI assistant that generates alt-texts. \n"
        "USER: Generate an alt-text for the [img-10]. \n"
        "ASSISTANT:"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://localhost:8080/completion', headers=headers, json=info)
    r = response.json()
    
    return r["content"]


demo = gr.Interface(
    fn=processa_imagem,
    inputs = gr.Image(type="pil"),
    outputs = gr.Textbox()
)
    

if __name__ == "__main__":
    demo.launch()
	