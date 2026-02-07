CREATE DATABASE sistema_bancario;
USE sistema_bancario;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) NOT NULL UNIQUE,
    email VARCHAR(100),
    telefone VARCHAR(15)
);

CREATE TABLE contas (
    id_conta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    tipo_conta ENUM('corrente', 'poupanca') NOT NULL,
    saldo DECIMAL(12,2) DEFAULT 0,
    data_abertura DATE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

INSERT INTO clientes (nome, cpf, email, telefone) VALUES
('Brendo Barbosa Silva', '12345678901', 'brendo@email.com', '11999999999'),
('Ana Souza', '23456789012', 'ana@email.com', '11988888888'),
('Carlos Pereira', '34567890123', 'carlos@email.com', '11977777777');

INSERT INTO contas (id_cliente, tipo_conta, saldo) VALUES
(1, 'corrente', 1000.00),
(1, 'poupanca', 500.00),
(2, 'corrente', 1500.00),
(3, 'corrente', 2000.00);


INSERT INTO transacoes (id_conta_destino, tipo, valor) VALUES
(1, 'deposito', 300.00);


UPDATE contas
SET saldo = saldo + 300.00
WHERE id_conta = 1;

INSERT INTO transacoes (id_conta_origem, tipo, valor) VALUES
(2, 'saque', 200.00);

UPDATE contas
SET saldo = saldo - 200.00
WHERE id_conta = 2;

INSERT INTO transacoes (id_conta_origem, id_conta_destino, tipo, valor) VALUES
(1, 3, 'transferencia', 150.00);

UPDATE contas
SET saldo = saldo - 150.00
WHERE id_conta = 1;

UPDATE contas
SET saldo = saldo + 150.00
WHERE id_conta = 3;

SELECT t.id_transacao, t.tipo, t.valor, t.data_transacao,
       c_origem.nome AS origem, c_destino.nome AS destino
FROM transacoes t
LEFT JOIN contas co ON t.id_conta_origem = co.id_conta
LEFT JOIN clientes c_origem ON co.id_cliente = c_origem.id_cliente
LEFT JOIN contas cd ON t.id_conta_destino = cd.id_conta
LEFT JOIN clientes c_destino ON cd.id_cliente = c_destino.id_cliente
WHERE t.id_conta_origem = 1 OR t.id_conta_destino = 1
ORDER BY t.data_transacao;

CREATE TABLE emprestimos (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    valor_total DECIMAL(12,2) NOT NULL,
    valor_pago DECIMAL(12,2) DEFAULT 0,
    data_inicio DATE DEFAULT CURRENT_TIMESTAMP,
    data_vencimento DATE NOT NULL,
    status ENUM('em_dia', 'atrasado', 'quitado') DEFAULT 'em_dia',
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE score_credito (
    id_score INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    score INT NOT NULL,
    classificacao ENUM('baixo', 'medio', 'alto') NOT NULL,
    data_calculo DATE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);


INSERT INTO emprestimos (id_cliente, valor_total, valor_pago, data_vencimento) VALUES
(1, 1000.00, 200.00, '2026-01-25'),
(2, 500.00, 500.00, '2026-01-28'),
(3, 1500.00, 1000.00, '2026-01-20');

USE sistema_bancario;
Select * From score_credito;









