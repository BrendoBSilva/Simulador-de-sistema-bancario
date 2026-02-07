from db import get_connection


def depositar(id_conta, valor):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "INSERT INTO transacoes (id_conta_destino, tipo, valor) VALUES (%s, 'deposito', %s)",
        (id_conta, valor)
    )
    cursor.execute(
        "UPDATE contas SET saldo = saldo + %s WHERE id_conta = %s",
        (valor, id_conta)
    )

    conn.commit()
    cursor.close()
    conn.close()

    print(f"✅ Depósito de R${valor} realizado")


def sacar(id_conta, valor):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT saldo FROM contas WHERE id_conta = %s",
        (id_conta,)
    )
    conta = cursor.fetchone()

    if not conta:
        print("❌ Conta não encontrada")
    elif conta["saldo"] >= valor:
        cursor.execute(
            "INSERT INTO transacoes (id_conta_origem, tipo, valor) VALUES (%s, 'saque', %s)",
            (id_conta, valor)
        )
        cursor.execute(
            "UPDATE contas SET saldo = saldo - %s WHERE id_conta = %s",
            (valor, id_conta)
        )
        conn.commit()
        print(f"✅ Saque de R${valor} realizado da conta {id_conta}")
    else:
        print("⚠️ Saldo insuficiente!")

    cursor.close()
    conn.close()


def extrato(id_conta):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT t.id_transacao, t.tipo, t.valor, t.data_transacao,
           c_origem.nome AS origem, c_destino.nome AS destino
    FROM transacoes t
    LEFT JOIN contas co ON t.id_conta_origem = co.id_conta
    LEFT JOIN clientes c_origem ON co.id_cliente = c_origem.id_cliente
    LEFT JOIN contas cd ON t.id_conta_destino = cd.id_conta
    LEFT JOIN clientes c_destino ON cd.id_cliente = c_destino.id_cliente
    WHERE t.id_conta_origem = %s OR t.id_conta_destino = %s
    ORDER BY t.data_transacao
    """

    cursor.execute(query, (id_conta, id_conta))
    resultados = cursor.fetchall()

    if resultados:
        print("\n--- EXTRATO ---")
        for r in resultados:
            print(
                f"{r['data_transacao']} | {r['tipo']} | "
                f"R${r['valor']} | Origem: {r['origem'] or '-'} | Destino: {r['destino'] or '-'}"
            )
    else:
        print("\n⚠️ Nenhuma transação encontrada")

    cursor.close()
    conn.close()
