from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__) # Cria uma instância da nossa aplicação web
app.secret_key = 'uma-chave-secreta-bem-aleatoria-12345'

# --- FUNÇÃO NOVA PARA CONECTAR AO DB ---
def get_db_connection():
    # Se conecta ao arquivo database.db
    conn = sqlite3.connect('../../database.db')
    # Retorna as linhas como dicionários sendo mais fácil de usar
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/", methods=['GET', 'POST'])
def login_page():
    if 'username' in session:
        return redirect(url_for('chat_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # --- LÓGICA DE LOGIN ATUALIZADA ---
        # 1. Abre a conexão com o banco de dados
        conn = get_db_connection()
        # 2. Procura por um usuário com o username fornecido
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        # 3. Fecha a conexão
        conn.close()

        # 4. Verifica se o usuário foi encontrado e se a senha bate
        if user and user['password'] == password:
            session['username'] = user['username']
            return redirect(url_for('chat_page'))
        else:
            flash("Usuário/senha inválido! 🔐.")
            return redirect(url_for('login_page'))
            
    return render_template("login.html")

@app.route("/chat")
def chat_page():
    if 'username' in session:
        #If it is, the user can log in. We pass the name to the template.
        return render_template("index.html", username=session['username'])
    else:
        #If not, access denied! We'll send you back to login..
        flash("Você precisa fazer login para acessar esta página.")
        return redirect(url_for('login_page'))
    
@app.route("/logout")
def logout():
    #Clears user information from the session.
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == "__main__":
    app.run(debug=True, port=5000) # e inicia o servidor. debug=True reinicia o servidor automaticamente quando você salva o arquivo.