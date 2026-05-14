from tkinter import *




janela = Tk()
janela.title("biblioteca pessoal")
janela.geometry("1100x432")
janela.config(bg="#4690AF")
janela.resizable(width=False,height=False)
# label = Label(janela,width=30,height=3,text="biblioteca pessoal",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
# label.place(x=0,y=0)
label_coluna_botao1 = Label(janela,width=30,height=3,text="biblioteca pessoal",font=("Aria 10 bold"),fg="white",bg="#696969")
label_coluna_botao1.grid(row=0, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text=" ♱ pesquisar",font=("Aria 10 bold"),fg="white",bg="#D9D9D9")
label_coluna_botao1.grid(row=1, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text="recentes",font=("Aria 10 bold"),fg="white",bg="#85B1E3")
label_coluna_botao1.grid(row=2, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text="meus livros",font=("Aria 10 bold"),fg="white",bg="#85B1E3")
label_coluna_botao1.grid(row=3, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text="explorar on-line",font=("Aria 10 bold"),fg="white",bg="#85B1E3")
label_coluna_botao1.grid(row=4, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text="listar arquivos",font=("Aria 10 bold"),fg="white",bg="#85B1E3")
label_coluna_botao1.grid(row=5, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text="marcadores",font=("Aria 10 bold"),fg="white",bg="#85B1E3")
label_coluna_botao1.grid(row=6, column=0)

label_coluna_botao1 = Label(janela,width=30,height=3,text="configurações",font=("Aria 10 bold"),fg="white",bg="#85B1E3")
label_coluna_botao1.grid(row=7, column=0)



janela.mainloop()