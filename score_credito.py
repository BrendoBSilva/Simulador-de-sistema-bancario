from db import get_connection


def calcular_score(id_cliente):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    score = 1000

    cursor.execute("""
        SELECT valor_total, valor_pago, status
        FROM emprestimos
        WHERE id_cliente = %s
    """, (id_cliente,))

    emprestimos = cursor.fetchall()

    if not emprestimos:
        score += 50
    else:
        for e in emprestimos:
            percentual_pago = e["valor_pago"] / e["valor_total"]

            if e["status"] == "atrasado":
                score -= 400
            elif percentual_pago < 0.5:
                score -= 300
            elif percentual_pago < 1:
                score -= 150

    score = max(0, min(score, 1000))

    if score >= 700:
        classificacao = "alto"
    elif score >= 400:
        classificacao = "medio"
    else:
        classificacao = "baixo"

    cursor.execute("""
        INSERT INTO score_credito (id_cliente, score, classificacao)
        VALUES (%s, %s, %s)
    """, (id_cliente, score, classificacao))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"📊 Score calculado: {score} ({classificacao})")
