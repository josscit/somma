import gradio as gr

def somma(a, b):
    """Ritorna la somma di due numeri"""
    return a + b

# Crea un'interfaccia Gradio con due ingressi numerici e un'uscita numerica
interfaccia = gr.Interface(fn=somma, inputs=[gr.Number(), gr.Number()], outputs="number", 
                           title="Somma due numeri")
# Avvia l'app su un server locale
interfaccia.launch()
