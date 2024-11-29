CREATE DATABASE imc_database;

CREATE TABLE imc_calculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    endereco VARCHAR(255),
    altura DECIMAL(5,2),
    peso DECIMAL(5,2),
    imc DECIMAL(5,2),
    data_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM imc_calculos