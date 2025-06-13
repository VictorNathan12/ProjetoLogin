import webbrowser
from tkinter import *
from tkinter import messagebox, simpledialog

# Temas (Claro e Escuro)
temas = {
    "claro": {
        "bg": "#ffffff", "fg": "#333333", "botao": "#1e90ff", "destaque": "#32cd32", "entrada": "#f0f0f0"
    },
    "escuro": {
        "bg": "#1e1e1e", "fg": "#ffffff", "botao": "#007acc", "destaque": "#00ff7f", "entrada": "#2e2e2e"
    }
}

tema_atual = "claro"
# Agora credenciais é um dicionário para facilitar o cadastro
contas = {"Victor": "123456789", "admin": "admin"}

janela = Tk()
janela.title("Tela de Login")
janela.geometry("310x350")
janela.resizable(False, False)

btn_nao_clique = None  # Declarar global antes

def aplicar_tema(widget=None):
    global btn_nao_clique
    cor = temas[tema_atual]
    janela.configure(bg=cor["bg"])
    frame_cima.configure(bg=cor["bg"])
    frame_baixo.configure(bg=cor["bg"])
    for w in frame_cima.winfo_children() + frame_baixo.winfo_children():
        if isinstance(w, (Label, Button)):
            w.configure(bg=cor["bg"], fg=cor["fg"])
        if isinstance(w, Entry):
            w.configure(bg=cor["entrada"], fg=cor["fg"], insertbackground=cor["fg"])
    if btn_nao_clique is not None:
        btn_nao_clique.configure(bg=cor["botao"], fg=temas[tema_atual]["bg"])
    botao_confirmar.configure(bg=cor["botao"], fg=temas[tema_atual]["bg"])
    btn_registrar.configure(bg=cor["botao"], fg=temas[tema_atual]["bg"])  # Novo botão

def verificar_senha():
    nome = e_nome.get()
    senha = str(e_pass.get())
    if nome in contas and contas[nome] == senha:
        messagebox.showinfo('Login', f'Seja bem-vindo, {nome}!')
        limpar_tela()
        nova_janela(nome)
    else:
        messagebox.showwarning('Erro', 'Verifique o nome de usuário ou a senha.')

def limpar_tela():
    for widget in frame_cima.winfo_children():
        widget.destroy()
    for widget in frame_baixo.winfo_children():
        widget.destroy()

def trocar_tema():
    global tema_atual
    tema_atual = "escuro" if tema_atual == "claro" else "claro"
    aplicar_tema()

def abrir_link():
    url = "https://youtu.be/QdBZY2fkU-0?si=wwoDXywOfQNtvBUT"
    webbrowser.open(url)

def nova_janela(usuario):
    limpar_tela()
    l_nome = Label(frame_cima, text="Usuário: " + usuario, font=('Segoe UI', 18, 'bold'))
    l_nome.place(x=10, y=10)

    btn_tema = Button(frame_cima, text="💡", font=('Segoe UI', 14), command=trocar_tema, bd=0)
    btn_tema.place(x=270, y=10)

    l_bemvindo = Label(frame_baixo, text=f"Seja bem-vindo, {usuario}!", font=('Segoe UI', 14))
    l_bemvindo.place(x=40, y=80)

    global btn_nao_clique
    btn_nao_clique = Button(frame_baixo, text="Não clique", font=('Segoe UI', 10, 'bold'),
                            width=15, height=1, command=abrir_link)
    btn_nao_clique.place(x=80, y=130)

    aplicar_tema()

def toggle_password():
    if e_pass.cget('show') == '':
        e_pass.config(show='*')
        btn_toggle.config(text='👁')
    else:
        e_pass.config(show='')
        btn_toggle.config(text='🙈')

def recuperar_senha():
    user = simpledialog.askstring("Recuperar Senha", "Digite o nome do usuário:")
    if user:
        if user in contas:
            messagebox.showinfo("Senha Recuperada", f"A senha do usuário '{user}' é: {contas[user]}")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

def registrar_usuario():
    def salvar_novo_usuario():
        novo_usuario = entrada_usuario.get().strip()
        nova_senha = entrada_senha.get().strip()
        if not novo_usuario or not nova_senha:
            messagebox.showerror("Erro", "Usuário e senha não podem ser vazios.")
            return
        if novo_usuario in contas:
            messagebox.showerror("Erro", "Usuário já existe.")
            return
        contas[novo_usuario] = nova_senha
        messagebox.showinfo("Sucesso", f"Conta '{novo_usuario}' registrada com sucesso!")
        janela_registro.destroy()

    janela_registro = Toplevel(janela)
    janela_registro.title("Registrar Novo Usuário")
    janela_registro.geometry("300x180")
    janela_registro.resizable(False, False)

    Label(janela_registro, text="Novo Usuário:").pack(pady=5)
    entrada_usuario = Entry(janela_registro, width=30)
    entrada_usuario.pack()

    Label(janela_registro, text="Nova Senha:").pack(pady=5)
    entrada_senha = Entry(janela_registro, width=30, show='*')
    entrada_senha.pack()

    btn_salvar = Button(janela_registro, text="Registrar", command=salvar_novo_usuario)
    btn_salvar.pack(pady=10)

frame_cima = Frame(janela, width=310, height=50)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300)
frame_baixo.grid(row=1, column=0)

l_titulo = Label(frame_cima, text="LOGIN", font=('Segoe UI', 24, 'bold'))
l_titulo.place(x=10, y=5)

linha = Label(frame_cima, width=300, height=1)
linha.place(x=5, y=45)

l_nome = Label(frame_baixo, text="Usuário", font=('Segoe UI', 10, 'bold'))
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, font=('Segoe UI', 12), relief="solid")
e_nome.place(x=10, y=45)

l_pass = Label(frame_baixo, text="Senha", font=('Segoe UI', 10, 'bold'))
l_pass.place(x=10, y=85)
e_pass = Entry(frame_baixo, show='*', width=21, font=('Segoe UI', 12), relief="solid")
e_pass.place(x=10, y=110)

btn_toggle = Button(frame_baixo, text='👁', bd=0, command=toggle_password)
btn_toggle.place(x=255, y=110)

botao_confirmar = Button(frame_baixo, text="Entrar", width=30, height=2, font=('Segoe UI', 10, 'bold'),
                         relief=RAISED, overrelief=RIDGE, command=verificar_senha)
botao_confirmar.place(x=10, y=160)

btn_recuperar = Button(frame_baixo, text="Recuperar Senha", bg="gray", fg="white",
                       font=('Segoe UI', 10), command=recuperar_senha)
btn_recuperar.place(x=10, y=220, width=140)

btn_registrar = Button(frame_baixo, text="Registrar Novo Usuário", bg="gray", fg="white",
                       font=('Segoe UI', 10), command=registrar_usuario)
btn_registrar.place(x=160, y=220, width=140)

aplicar_tema()

janela.mainloop()
