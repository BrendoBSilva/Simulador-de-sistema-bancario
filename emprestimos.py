from datetime import date
from db import get_connection

def atualizar_inadimplencia():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    hoje = date.today()

    cursor.execute("SELECT * FROM emprestimos")
    emprestimos = cursor.fetchall()

    for e in emprestimos:
        if e["valor_pago"] >= e["valor_total"]:
            status = "quitado"
        elif e["data_vencimento"] < hoje:
            status = "atrasado"
        else:
            status = "em_dia"

        cursor.execute(
            "UPDATE emprestimos SET status=%s WHERE id_emprestimo=%s",
            (status, e["id_emprestimo"])
        )

    conn.commit()
    cursor.close()
    conn.close()
