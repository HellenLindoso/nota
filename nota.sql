USE bd_nota;
CREATE TABLE tb_informacoes(
codigo INT PRIMARY KEY AUTO_INCREMENT,
movimentacao VARCHAR(50) NOT NULL,
descricao VARCHAR(100) NOT NULL,
valor FLOAT NOT NULL,
categoria VARCHAR(50) NOT NULL,
dataMovimentacao DATE NOT NULL
);

SELECT * FROM tb_informacoes;