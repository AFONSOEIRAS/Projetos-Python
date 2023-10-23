import tkinter as tk

# Função para criar widgets com diferentes valores de padding
def create_widget_with_padding(padding_values):
    frame = tk.Frame(root, background="lightgray", width=100, height=100)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="Exemplo", background="lightblue")
    if isinstance(padding_values, int):
        label.pack(padx=padding_values, pady=padding_values)
    elif isinstance(padding_values, tuple) and len(padding_values) == 2:
        padx, pady = padding_values
        label.pack(padx=padx, pady=pady)

# Criar uma janela principal
root = tk.Tk()
root.title("Exemplo de Padding")

# Criar widgets com diferentes valores de padding
create_widget_with_padding(5)          # 5 pixels em todos os lados
create_widget_with_padding((5, 10))    # 5 à esquerda e à direita, 10 no topo e na parte inferior
create_widget_with_padding((5, 7))  # Valores específicos para cada lado

# Iniciar a interface gráfica
root.mainloop()
