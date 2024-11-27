from flask import Flask  #importa a classe Flask pra criar a aplicação web

app = Flask(__name__) #cria uma instância Flask com argumento __name__, ajuda o flask a localizar/gerenciar recursos

@app.route("/") # rota para mapear URL
def home(): # definir a função home para ser executada quando a rota definida for acessada 
    return "Olá sou do App1!"

if __name__ == "__main__":  # verifica se o script esta sendo executado diretamente
    app.run(host="0.0.0.0", port=5000) # inicia o servidor web Flask, "host" permite que o servidor seja acessado por qualquer dispositivo na rede e define a porta 5000 em que o servidor sera executado