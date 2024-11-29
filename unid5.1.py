import mysql.connector

# Função para calcular o IMC
def calcular_imc(altura_cm, peso_kg):
    try:
        altura_m = float(altura_cm) / 100  # Converte para metros
        peso = float(peso_kg)
        imc = peso / (altura_m ** 2)
        return round(imc, 2)
    except ValueError:
        return None

# Função para conectar ao banco de dados MySQL
def conectar_banco():
    try:
        # Substitua os valores abaixo pelos dados do seu banco de dados
        conexao = mysql.connector.connect(
            host="localhost",  # ou o endereço IP do seu servidor MySQL
            user="root",  # seu nome de usuário MySQL
            password="A1234",  # sua senha MySQL
            database="imc_database"  # nome do banco de dados
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

# Função para armazenar o cálculo no banco de dados
def armazenar_no_banco(nome, endereco, altura, peso, imc):
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        try:
            # Inserção de dados na tabela
            query = "INSERT INTO imc_calculos (nome, endereco, altura, peso, imc) VALUES (%s, %s, %s, %s, %s)"
            dados = (nome, endereco, altura, peso, imc)
            cursor.execute(query, dados)
            conexao.commit()  # Confirma a transação
            print("Cálculo de IMC armazenado com sucesso no banco de dados!")
        except mysql.connector.Error as err:
            print(f"Erro ao inserir dados: {err}")
        finally:
            cursor.close()
            conexao.close()

# Função principal para execução no terminal
def main():
    print("Calculadora de IMC")

    # Entrada dos dados do paciente
    nome = input("Nome do Paciente: ")
    endereco = input("Endereço Completo: ")
    altura = input("Altura (em cm): ")
    peso = input("Peso (em kg): ")

    # Verifica se todos os campos foram preenchidos
    if nome and endereco and altura and peso:
        imc = calcular_imc(altura, peso)
        if imc:
            print(f"\nResultado do IMC para {nome}: {imc}")
            # Armazenar no banco de dados
            armazenar_no_banco(nome, endereco, altura, peso, imc)
        else:
            print("Valores inválidos. Tente novamente.")
    else:
        print("Por favor, preencha todos os campos.")

    # Pergunta se o usuário quer calcular novamente ou sair
    while True:
        reiniciar = input("\nDeseja calcular novamente? (s/n): ").lower()
        if reiniciar == 's':
            main()  # Chama novamente a função para um novo cálculo
            break
        elif reiniciar == 'n':
            print("Obrigado por usar a calculadora de IMC.")
            break
        else:
            print("Opção inválida. Por favor, responda com 's' ou 'n'.")

if __name__ == "__main__":
    main()
