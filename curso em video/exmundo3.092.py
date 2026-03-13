#  Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
# o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.



from datetime import datetime  # Imports datetime to work with dates / Importa datetime para trabalhar com datas

def register_employee():  # Defines the employee registration function / Define a função de cadastro do funcionário
    employee_data = dict()  # Creates a dictionary to store employee data / Cria um dicionário para armazenar os dados do funcionário
    current_year = datetime.now().year  # Gets the current year from the system / Obtém o ano atual do sistema

    employee_data['name'] = str(input('Name: '))  # Asks for the employee's name / Solicita o nome do funcionário
    birth_year = int(input('Year of birth: '))  # Asks for the year of birth / Solicita o ano de nascimento
    employee_data['age'] = current_year - birth_year  # Calculates the current age / Calcula a idade atual
    employee_data['CTPS'] = int(input('Work Card: '))  # Asks for the work card (0 if not available) / Solicita a carteira de trabalho (0 se não tiver)

    if employee_data['CTPS'] != 0:  # If the work card is not 0 / Se a carteira de trabalho for diferente de 0
        employee_data['hiring_year'] = int(input('Year of hiring: '))  # Asks for the hiring year / Solicita o ano de contratação
        employee_data['salary'] = float(input('Salary: R$ '))  # Asks for the salary / Solicita o salário

        contribution_time = current_year - employee_data['hiring_year']  # Calculates the contribution time / Calcula o tempo de contribuição
        employee_data['contribution_time'] = contribution_time  # Stores the contribution time / Armazena o tempo de contribuição

        remaining_years = 35 - contribution_time  # Calculates remaining years to reach 35 / Calcula os anos restantes para atingir 35

        if remaining_years > 0:  # If there are still years to contribute / Se ainda houver anos para contribuir
            employee_data['retirement_age'] = employee_data['age'] + remaining_years  # Age when they will retire / Idade em que poderá se aposentar
            employee_data['years_to_contribute'] = remaining_years  # Remaining contribution years / Anos restantes de contribuição
        else:
            employee_data['retirement_age'] = employee_data['age']  # Can retire at current age / Pode se aposentar com a idade atual
            employee_data['status'] = 'Can retire now'  # Adds retirement status / Adiciona o status de aposentadoria

    print('\n--- Employee Data ---')  # Displays the title of the data / Exibe o título dos dados

    for key, value in employee_data.items():  # Loops through the dictionary and prints the data / Percorre o dicionário e imprime os dados
        print(f'{key.capitalize()}: {value}')  # Displays the key and value formatted / Exibe a chave e o valor formatados

register_employee()  # Calls the function to run the program / Chama a função para executar o programa




