import tkinter as tk

janela = tk.Tk()
janela.title("Minha nova interface")
janela.geometry("200x200")
janela.config(bg="purple")

#Utilizando a classe Label
texto = tk.Label(janela,text="Slay é slay",font=("Arial",16),bg="blue",fg="red")
                 
texto.pack(pady=50)

texto2 = tk.Label(janela,
                  text="Aperte o botão para dar slay"
                  ,font= ("Arial",24)
                  ,fg="gray")
texto2.pack()

def clicar():
    texto3 = tk.Label(janela,text="Você acionou o botão!")
    texto3.pack()

def cadastrar():
    print("Método cadastrar")

#Utilizando a classe Button
botao = tk.Button(janela,text="Enviar",command=clicar,bg="blue")
botao.pack()

lista = tk.Listbox(janela,height=4)
lista.insert(1,"JavaScript")
lista.insert(2,"HTML")
lista.insert(3,"CSS")
lista.insert(4,"Python")

lista.pack

#Utilizando a classe Menu
menu_bar = tk.Menu(janela)
arq_menu = tk.Menu(menu_bar,tearoff=1)
arq_menu.add_command(label="Abrir")
arq_menu.add_command(label="Salvar")
arq_menu.add_separator()
arq_menu.add_command(label="Sair", command=janela.quit)
arq_menu.add_cascade(label="Arquivo",menu=arq_menu)
janela.config(menu=menu_bar)

janela.mainloop()