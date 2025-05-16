import gradio as gr
from core.converter import BusinessRuleConverter

def create_interface():
    converter = BusinessRuleConverter()
    
    examples = [
        "Se o cliente for VIP, frete grátis",
        "Aplicar 20% de desconto para compras acima de R$ 1000",
        "Se hora > 18:00, cobrar taxa noturna",
        "Acima de 10 produtos, adicionar desconto de 10% acumulativo a cada 10 produtos"
    ]
    
    with gr.Blocks(theme=gr.themes.Soft(), title="Conversor de Regras") as interface:
        gr.Markdown("""<h1><center>🛠️ Conversor de Regras de Negócio para Python</center></h1>""")
        
        with gr.Row():
            with gr.Column():
                input_box = gr.Textbox(
                    label="Regra de Negócio",
                    placeholder="Ex: Se temperatura > 30, ligar ventilador...",
                    lines=3
                )
                gr.Examples(
                    examples=examples,
                    inputs=input_box,
                    label="Clique em um exemplo"
                )
                
            with gr.Column():
                output_code = gr.Code(
                    label="Código Python Gerado",
                    language="python",
                    interactive=True
                )
        
        submit_btn = gr.Button("Converter", variant="primary")
        submit_btn.click(
            fn=converter.convert,
            inputs=input_box,
            outputs=output_code
        )
        
        input_box.submit(
            fn=converter.convert,
            inputs=input_box,
            outputs=output_code
        )
    
    return interface