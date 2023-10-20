import contato;
import agendaDeContatos;

def main():
    minhaAgenda = agendaDeContatos.AgendaDeContatos();

    print("Menu Interativo")
    print("1 - Adicionar Contato")
    print("2 - Remover Contato")
    print("3 - Buscar Contato")
    print("4 - Listar Contatos")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada: "))
    while opcao != 5:
        if opcao == 1:
            nome = input("Digite o nome do contato: ")
            numero = input("Digite o número do contato: ")
            novoContato = contato.Contato(nome, numero)
            minhaAgenda.adicionarContato(novoContato)
        elif opcao == 2:
            nome = input("Digite o nome do contato: ")
            minhaAgenda.removerContato(nome)
        elif opcao == 3:
            nome = input("Digite o nome do contato: ")
            print(minhaAgenda.buscarContato(nome))
        elif opcao == 4:
            print(minhaAgenda.listarContatos())
        else:
            print("Opção inválida!")

        opcao = int(input("Digite a opção desejada: "))