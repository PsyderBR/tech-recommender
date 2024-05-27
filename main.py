import customtkinter as ctk
from tkinter import messagebox, Listbox
from pyswip import Prolog

# Inicializa o Prolog
prolog = Prolog()
prolog.consult("tech_recommendations.pl")

# Função para obter recomendações de tecnologias
def get_recommendations():
    try:
        role = role_var.get()
        if not role:
            messagebox.showwarning("Aviso", "Por favor, selecione um papel de desenvolvedor.")
            return

        query = f"recommend_tech({role}, Tech)"
        techs = list(prolog.query(query))
        if not techs:
            messagebox.showinfo("Sem Recomendações", "Nenhuma tecnologia encontrada para o papel selecionado.")
        
        # Limpa a lista de recomendações
        recommendation_list.delete(0, ctk.END)
        
        # Adiciona as novas recomendações à lista
        for tech in techs:
            recommendation_list.insert(ctk.END, tech['Tech'])
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Cria a janela principal
try:
    root = ctk.CTk()
    root.title("Recomendações de Tecnologias de Programação")

    # Cria e configura o frame principal
    mainframe = ctk.CTkFrame(root)
    mainframe.grid(column=0, row=0, sticky=(ctk.W, ctk.E, ctk.N, ctk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Variável de controle para o papel de desenvolvedor
    role_var = ctk.StringVar()

    # Label e combobox para seleção do papel de desenvolvedor
    ctk.CTkLabel(mainframe, text="Escolha um papel de desenvolvedor:").grid(column=1, row=1, sticky=ctk.W, padx=5, pady=5)
    role_combobox = ctk.CTkComboBox(mainframe, variable=role_var, values=['front_end', 'back_end', 'fullstack'])
    role_combobox.grid(column=2, row=1, sticky=(ctk.W, ctk.E), padx=5, pady=5)

    # Botão para obter recomendações
    ctk.CTkButton(mainframe, text="Recomendar", command=get_recommendations).grid(column=2, row=2, sticky=ctk.W, padx=5, pady=5)

    # Listbox para exibir recomendações
    recommendation_list = Listbox(mainframe, height=10)
    recommendation_list.grid(column=1, row=3, columnspan=2, sticky=(ctk.W, ctk.E), padx=5, pady=5)

    # Adiciona algum padding ao redor de cada widget
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    # Define o foco inicial na combobox
    role_combobox.focus()

    # Inicia o loop principal
    root.mainloop()
except Exception as e:
    messagebox.showerror("Erro Crítico", f"Ocorreu um erro crítico na interface gráfica: {e}")
    root.destroy()
