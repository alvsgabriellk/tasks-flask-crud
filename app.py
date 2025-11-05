from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__) # nome do arquivo atual

tasks = [] # banco de dados simples e temporario
task_id_control = 1 # proximo id disponivel
# C - CRUD / CREATE
@app.route('/tasks', methods=['POST'])
def create_tasks():
    global task_id_control # vai modificar a variavel global
    data = request.get_json() # pega os dados json que foram enviados da request
    new_task = Task(id=task_id_control,titulo=data['titulo'], descricao=data.get("descricao", "")) #busque a chave descricao, "" valor reserva se n achar a chave
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"}) # resposta da API

@app.route('/tasks', methods=['GET']) # ta requisitando os dados
def get_tasks():
    #metodo simples e menos visual
    task_list = [task.to_dict() for task in tasks]
    
    #metodo visual e complexo
    for task in tasks:
        task_list.append(task.to_dict())
    outpot = {
        "tasks": task_list,
        "total_tasks": len(task_list)
        }
    return jsonify(outpot)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

if __name__ == "__main__":
    app.run(debug=True)
