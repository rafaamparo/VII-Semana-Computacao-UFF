class agendaDeContatos:
    def __init__(self):
        self.contatos = []
    
    def adicionarContato(self, contato):
        self.contatos.append(contato)
    
    def removerContato(self, contato):
        self.contatos.remove(contato)

    def listarContatos(self):
        for contato in self.contatos:
            print(contato.nome, contato.numero)
    
    def buscarContato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                return contato
        return None

    def buscarContatoNumero (self, numero):
        for contato in self.contatos:
            if contato.numero == numero:
                return contato
        return None