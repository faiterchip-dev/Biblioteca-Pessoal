from tkinter import *




janela = Tk()
janela.title("biblioteca pessoal")
janela.geometry("1100x432")
janela.config(bg="#4690AF")
janela.resizable(width=False,height=False)

def teste():
    global contador_teste
    texto1 = "solo library"
    texto2 = "call of duty"
    
    if (contador_teste %2) == 0:
        print(texto1)
    else:
        print(texto2)
        
    contador_teste = contador_teste + 1
contador_teste=0

# label = Label(janela,width=30,height=3,text="biblioteca pessoal",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
# label.place(x=0,y=0)
label_coluna_botao = Label(janela,width=30,height=3,text="biblioteca pessoal",font=("Aria 10 bold"),fg="white",bg="#696969")
label_coluna_botao.grid(row=0, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#D9D9D9")
label_coluna_botao.grid(row=1, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
label_coluna_botao.grid(row=2, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
label_coluna_botao.grid(row=3, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
label_coluna_botao.grid(row=4, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
label_coluna_botao.grid(row=5, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
label_coluna_botao.grid(row=6, column=0)

label_coluna_botao = Label(janela,width=30,height=3,text="",font=("Aria 10 bold"),fg="white",bg="#9C9DB1")
label_coluna_botao.grid(row=7, column=0)
#-----------------------------------------------------------------------------------------------------------
label_coluna_botao = Label(janela,width=26,height=2,text="",font=("Aria 10 bold"),fg="white",bg="white")
label_coluna_botao.grid(row=1, column=0)

label_coluna_botao = Label(janela,width=29,height=2,text="",font=("Aria 10 bold"),fg="white",bg="#9DC8F9")
label_coluna_botao.grid(row=2, column=0)

label_coluna_botao = Label(janela,width=29,height=2,text="",font=("Aria 10 bold"),fg="white",bg="#9DC8F9")
label_coluna_botao.grid(row=3, column=0)

label_coluna_botao = Label(janela,width=29,height=2,text="",font=("Aria 10 bold"),fg="white",bg="#9DC8F9")
label_coluna_botao.grid(row=4, column=0)

label_coluna_botao = Label(janela,width=29,height=2,text="",font=("Aria 10 bold"),fg="white",bg="#9DC8F9")
label_coluna_botao.grid(row=5, column=0)

label_coluna_botao = Label(janela,width=29,height=2,text="",font=("Aria 10 bold"),fg="white",bg="#9DC8F9")
label_coluna_botao.grid(row=6, column=0)

label_coluna_botao = Label(janela,width=29,height=2,text="",font=("Aria 10 bold"),fg="white",bg="#9DC8F9")
label_coluna_botao.grid(row=7, column=0)

#------------------------------------------------------------------------------------------------------------
botao = Button(janela,command=teste,width=27,height=1,text=" ♱ pesquisar",bg="#D9D9D9")
botao.grid(row=1,column=0)

botao = Button(janela,width=27,text="recentes",bg="#85B1E3",font=("Aria 10 bold"),fg="white")
botao.grid(row=2,column=0)

botao = Button(janela,width=27,text="meus livros",bg="#85B1E3",font=("Aria 10 bold"),fg="white")
botao.grid(row=3,column=0)

botao = Button(janela,width=27,text="explorar on-line",bg="#85B1E3",font=("Aria 10 bold"),fg="white")
botao.grid(row=4,column=0)

botao = Button(janela,width=27,text="listar arquivos",bg="#85B1E3",font=("Aria 10 bold"),fg="white")
botao.grid(row=5,column=0)

botao = Button(janela,width=27,text="marcadores",bg="#85B1E3",font=("Aria 10 bold"),fg="white")
botao.grid(row=6,column=0)

botao = Button(janela,width=27,text="configurações",bg="#85B1E3",font=("Aria 10 bold"),fg="white")
botao.grid(row=7,column=0)

janela.mainloop()