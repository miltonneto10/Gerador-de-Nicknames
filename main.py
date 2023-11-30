import tkinter as tk
from tkinter import Entry, Label, Button
import random

def generate_nicknames(name):
    #Definindo listas de prefixos, sufixos, números e variações para os nicknames.
    prefixes = ["", "The", "Pro", "Master", "Ultra", "Super", "Epic", "Mega", "Ninja", "Golden", "Grande", "Soberano", "Lord", "Don"]
    suffixes = ["", "Gamer", "Player", "Sniper", "Legend", "Warrior", "Champion", "Boss", "King", "Queen", "God", "San"]
    numbers = [str(i) for i in range(10)]
    variations = ["", "X", "_", "-", ".", "Official", "Real"]

    nickname_list = []
    for _ in range(5):
        #Escolhendo aleatoriamente um prefixo, sufixo, númeor e variação.
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        number = random.choice(numbers)
        variation = random.choice(variations)
        #Criando o nickname combinando os elementos escolhidos
        nickname = f"{prefix}{name}{suffix}{number}{variation}"
        #Adicionando o nickname à lsita
        nickname_list.append(nickname)

    return nickname_list

def generate_button_click():
    #obtendo o nome inserido pelo usuário
    name = name_entry.get()
    if name:
        #Se tiver algum nome, vai gerar os nicknames e exibi-los na tela
        nicknames = generate_nicknames(name)
        result_label.config(text="\n".join(nicknames))
    else:
        #Se não tiver nenhum nome inserido, vai ser solicitado que escreva um nome.
        result_label.config(text="\n" + "\n".join([
            "Por favor,",
            "insira um nome."]),
            font=("Arial", 12, "bold")
        )

#Criando a interface gráfica
root = tk.Tk()
root.title("Gerador de Nicknames")
root.geometry("400x300")
root.configure(bg="#FFDEAD")
root.resizable(False, False)  # Bloquear maximização

#Elementos da interface
title_label = Label(root, text="Digite seu nome:", bg="#FFDEAD", font=("Arial", 14))
title_label.pack(pady=10)

name_entry = Entry(root, font=("Arial", 12))
name_entry.pack(pady=10)

generate_button = Button(root, text="Gerar Nicknames", command=generate_button_click, bg="#F4A460", font=("Arial", 12))
generate_button.pack(pady=10)

result_label = Label(root, text="", bg="#FFDEAD", font=("Arial", 12))
result_label.pack(pady=10)

#Iniciando o loop principal
root.mainloop()