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

# R - CRUD / READ //// LENDO TODOS OS DADOS
@app.route('/tasks', methods=['GET']) # ta requisitando os dados
def get_tasks():
    #metodo simples e menos visual
    task_list = [task.to_dict() for task in tasks] # QUANDO CHAMAR, VAI SAIR COMO DICIONARIO DA CLASSE
    
    #metodo visual e complexo
    for task in tasks:
        task_list.append(task.to_dict())
    outpot = {
        "tasks": task_list, # VAI CHAMAR O DICIONARIO DA TAREFA PRA CA, A EXIBIÇÃO
        "total_tasks": len(task_list) 
        }
    return jsonify(outpot) # RETORNAR EM JSON PRA A API

# R - CRUD / READ //// LENDO APENAS UM DADO EM ESPECIFICO
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict()) # VAI RETORNAR EM JSON PRA API A TAREFA CHAMADA EM DICIONARIO
        
    return jsonify({"message": "Não foi possível encontrar a atividade."}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade."}), 404
    
    data = request.get_json()
    task.title = data['titulo']
    task.descricao = data['descricao']
    task.completo = data['completo']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)
