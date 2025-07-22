import tkinter as tk 
from tkinter import filedialog, Frame, messagebox
from PIL import Image, ImageTk
import os

# Configuração da janela principal
janela = tk.Tk()
janela.title("Editor de Imagens")
janela.geometry("650x550")
janela.config(bg="#f0f0f0")
janela.resizable(True, True)

# Variável global para armazenar a imagem atual
imagem_atual = None

# Funções
def ExibirImagem():
    global imagem_atual
    try:
        caminho_imagem = filedialog.askopenfilename(
                title="Selecione uma imagem",
                filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if caminho_imagem:
            img = Image.open(caminho_imagem)
            imagem_atual = img.copy()  # Salvar uma cópia da imagem original
            img_resized = img.resize((400, 400))
            img_tk = ImageTk.PhotoImage(img_resized)
            imagem_label.config(image=img_tk)
            imagem_label.image = img_tk
            nome_arquivo = os.path.basename(caminho_imagem)
            status_label.config(text=f"Imagem carregada: {nome_arquivo}")
        else:
            status_label.config(text="Nenhuma imagem selecionada.")
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir a imagem: {e}")
        status_label.config(text="Erro ao abrir a imagem.")

def TonsCinza():
    global imagem_atual
    try:
        if imagem_atual:
            # Converter a imagem para tons de cinza
            img_cinza = imagem_atual.convert('L')
            # Redimensionar a imagem
            img_resized = img_cinza.resize((400, 400))
            # Converter para formato exibível pelo tkinter
            img_tk = ImageTk.PhotoImage(img_resized)
            # Exibir a imagem em preto e branco
            imagem_label.config(image=img_tk)
            imagem_label.image = img_tk
            status_label.config(text="Imagem convertida para tons de cinza")
        else:
            status_label.config(text="Nenhuma imagem foi aberta para converter.")
            messagebox.showwarning("Aviso", "Por favor, abra uma imagem primeiro.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter a imagem: {e}")

def SalvarImagem():
    global imagem_atual
    if imagem_atual:
        try:
            arquivo = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")]
            )
            if arquivo:
                # Se a imagem está sendo exibida em tons de cinza, salvar na versão P&B
                if "tons de cinza" in status_label.cget("text"):
                    img_cinza = imagem_atual.convert('L')
                    img_cinza.save(arquivo)
                else:
                    imagem_atual.save(arquivo)
                status_label.config(text=f"Imagem salva como: {os.path.basename(arquivo)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível salvar a imagem: {e}")
    else:
        messagebox.showwarning("Aviso", "Não há imagem para salvar.")

# Frame para o título
titulo_frame = Frame(janela, bg="#f0f0f0")
titulo_frame.pack(pady=10, fill=tk.X)

titulo_label = tk.Label(titulo_frame, text="EDITOR DE IMAGENS", 
                      font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
titulo_label.pack()

# Frame para os botões
botoes_frame = Frame(janela, bg="#f0f0f0")
botoes_frame.pack(pady=10)

# Estilo dos botões
estilo_botao = {"font": ("Arial", 11),
               "fg": "white",
               "relief": tk.RAISED,
               "width": 15,
               "height": 2,
               "borderwidth": 2}

botaoAbrir = tk.Button(botoes_frame, text="1. Abrir Imagem", command=ExibirImagem, 
                     **{**estilo_botao, "bg": "#4CAF50"})
botaoAbrir.pack(side=tk.LEFT, padx=5)

botaoP_B = tk.Button(botoes_frame, text="2. Converter para P&B", command=TonsCinza, 
                   **{**estilo_botao, "bg": "#2196F3"})
botaoP_B.pack(side=tk.LEFT, padx=5)

botaoSalvar = tk.Button(botoes_frame, text="3. Salvar Imagem", command=SalvarImagem,
                      **{**estilo_botao, "bg": "#FF5722", "font": ("Arial", 11, "bold")})
botaoSalvar.pack(side=tk.LEFT, padx=5)

# Adicionar descrição para instruir o usuário
instrucao_label = tk.Label(janela, text="Selecione uma imagem, converta para preto e branco e depois salve",
                         font=("Arial", 10, "italic"), bg="#f0f0f0")
instrucao_label.pack(pady=5)

# Frame para exibir a imagem
imagem_frame = Frame(janela, bg="#e0e0e0", width=420, height=420, 
                   highlightbackground="#999", highlightthickness=1)
imagem_frame.pack(pady=10)
imagem_frame.pack_propagate(False)  # Manter o tamanho do frame fixo

# Label para a imagem
imagem_label = tk.Label(imagem_frame, bg="#e0e0e0")
imagem_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Status bar na parte inferior
status_label = tk.Label(janela, text="Aguardando imagem...", 
                       font=("Arial", 10), bg="#f0f0f0", fg="#555555", 
                       bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

janela.mainloop()