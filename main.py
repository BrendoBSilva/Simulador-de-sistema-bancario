from banco import depositar
from inadimplencia import listar_inadimplencia
from score_credito import calcular_score

def menu():
    while True:
        print("\n=== PIPELINE BANCÁRIA ===")
        print("1 - Depositar")
        print("2 - Listar inadimplentes")
        print("3 - Calcular score de crédito")
        print("4 - Sair")

        op = input("Escolha: ")

        if op == "1":
            id_conta = int(input("ID da conta: "))
            valor = float(input("Valor: R$"))
            depositar(id_conta, valor)

        elif op == "2":
            listar_inadimplencia()

        elif op == "3":
            id_cliente = int(input("ID do cliente: "))
            calcular_score(id_cliente)

        elif op == "4":
            print("Encerrando sistema...")
            break

        else:
            print("❌ Opção inválida!")

menu()
