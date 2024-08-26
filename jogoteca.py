from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Driver', 'Ação', 'PS1')
    jogo2 = Jogo('Mario World', 'Aventura', 'Super Nintendo')
    jogo3 = Jogo('Counter Strike', 'Tiro', 'PC')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(debug=True)