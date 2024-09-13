# C214

# Professor Schedule

Este projeto é uma aplicação em Python para gerenciar e validar informações sobre horários de atendimento de professores. Ele determina o prédio com base no número da sala e valida os dados fornecidos, como horários de atendimento, para garantir que estejam no formato correto.

## 📁 Estrutura do Projeto

- **`professor_schedule.py`**: Contém a classe `ProfessorSchedule`, responsável por processar e validar os dados de horários de atendimento dos professores.
- **`validate.py`**: Contém funções auxiliares de validação, como `validate_horario`, que verifica o formato dos horários.
- **`test_professor_schedule.py`**: Contém testes unitários para garantir o funcionamento correto da classe `ProfessorSchedule` e das funções de validação.

## 🚀 Funcionalidades

- **Detecção do Prédio**: Determina o prédio com base no número da sala.
- **Validação de Horário**: Verifica se o horário de atendimento está no formato correto ("HH:MM - HH:MM").
- **Verificação de Dados**: Garante que todos os campos necessários (nome do professor, horário, período, sala) estão presentes e são válidos.

## 🛠️ Pré-requisitos

- Python 3.7 ou superior

## 📝 Instalação

1. Clone o repositório:

   ``` bash
   git clone https://github.com/carolinyat/C214.git
   ```

2. Navegue para o diretório do projeto:
   cd C214/Ex01

## 📦 Como Executar os Testes
<br>
Para rodar os testes, utilize o comando:

   ```bash
   python -m unittest test_professor_schedule.py
   ```


Isso executará uma série de testes para validar as funcionalidades principais, como a determinação do prédio e a validação de horários.
<br>

Os testes incluídos no projeto verificam:
<br>
- Cenários de Sucesso: A classe funciona conforme o esperado com entradas válidas.
  
- Cenários de Falha: A classe lida adequadamente com entradas inválidas e lança os erros apropriados.

## ✍️ Autores
- Caroliny Abreu
- Fernanda Ellen
- Tiago Giugni
