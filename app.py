from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__) # nome do arquivo atual

tasks = [] # banco de dados simples e temporario
task_id_control = 1 # proximo id disponivel

@app.route('/tasks', methods=['POST'])
def create_tasks():
    global task_id_control # vai modificar a variavel global
    data = request.get_json() # pega os dados json que foram enviados da request
    new_task = Task(id=task_id_control,titulo=data['titulo'], descricao=data.get("descricao", "")) #busque a chave descricao, "" valor reserva se n achar a chave
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"}) # resposta da API

if __name__ == "__main__":
    app.run(debug=True)
