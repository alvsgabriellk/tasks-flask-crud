class Task:
    def __init__(self, id, titulo, descricao, completo=False)-> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.completo = completo

    def to_dict(self):
        return {
            "id": self.id, 
            "titulo":self.titulo,
            "descricao": self.descricao, 
            "completo": self.completo
        }