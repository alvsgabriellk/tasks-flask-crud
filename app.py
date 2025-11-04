from flask import Flask
app = Flask(__name__) # nome do arquivo

@app.route('/')
def ola_mundo():
    return "Hello Word"

@app.route('/about')
def about():
    return "Página Sobre" 

if __name__ == "__main__":
    app.run(debug=True)
