from db import get_connection
from emprestimos import atualizar_inadimplencia

def listar_inadimplencia():
    atualizar_inadimplencia()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        Select c.nome, e.valor_total, e.valor_pago, e.data_vencimento
        From emprestimos e
        Join clientes c on e.id_cliente = c.id_cliente
        Where e.status = 'atrasado'
        """)

    resultados = cursor.fetchall()

    if resultados:
        print("\n--- INADIMPLENTES ---")
        for r in resultados:
            print(r)
    else:
        print("\n✅ Nenhum inadimplente")

    cursor.close()
    conn.close()