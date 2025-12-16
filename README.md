 Chatbot – Clínica Odonto Silva
 Descrição do Projeto

Este projeto consiste no desenvolvimento de um chatbot de atendimento para uma clínica fictícia chamada Clínica Odonto Silva.
O bot foi criado com o objetivo de automatizar o primeiro contato com os clientes, facilitando o trabalho dos atendentes humanos e tornando o atendimento mais rápido e prático.

O chatbot é capaz de:

Responder mensagens iniciais dos usuários

Realizar agendamento de consultas

Apresentar informações sobre a clínica

Auxiliar na resolução de dúvidas frequentes

Redirecionar o usuário para um atendente humano, quando necessário

 Objetivo

O principal objetivo do projeto é simular um sistema real de atendimento automatizado, aplicando conceitos de programação em Python, lógica de estados, manipulação de datas, armazenamento de dados e comunicação em tempo real.

 Funcionamento Geral

O usuário inicia o atendimento com uma saudação.

O bot apresenta um menu de opções.

O usuário pode:

Agendar uma consulta

Falar com um atendente humano

Durante o agendamento, o bot:

Coleta dados do usuário

Calcula a idade a partir da data de nascimento

Sugere datas e horários disponíveis

Confirma o agendamento

Salva os dados em um arquivo JSON

Caso solicitado, o atendimento é transferido para um atendente humano via WebSocket.

 Tecnologias Utilizadas

Python 3

FastAPI – servidor WebSocket

Uvicorn – servidor ASGI

WebSockets – comunicação em tempo real

JSON – armazenamento dos agendamentos

Unidecode – normalização de textos

Datetime – manipulação de datas

Bot da Clinica python/
│
├── server.py                # Servidor WebSocket (FastAPI)
├── clientes_ws.py           # Cliente WebSocket
├── agendar_consulta.py      # Lógica de agendamento
├── funcoes_auxiliares.py    # Funções auxiliares
├── agendamentos.json        # Armazenamento das consultas
├── main.py                  # Arquivo principal (opcional)
└── README.md                # Documentação do projeto

Como executar o projeto?

1.  instalar as dependencias
  - pip install fastapi uvicorn websockets unidecode
2. Iniciar o Servidor
 - python -m uvicorn server:app --reload
3. Executar o cliente WebSocket
   -python clientes_ws.py
Observações

A interação com o usuário ainda não é 100% perfeita, mas já apresenta um fluxo funcional e consistente.

O projeto passou por uma refatoração completa, com melhorias de estrutura, legibilidade, organização e correção de erros.

O código foi desenvolvido com foco em aprendizado e prática, não em produção.

 Uso do ChatGPT

O ChatGPT foi utilizado como ferramenta de apoio para:

Correção de erros

Sugestões de melhorias

Organização de lógica

Estruturação do código

Boas práticas de programação

 Próximos Passos (Melhorias Futuras)

Melhorar a interpretação de mensagens do usuário

Implementar histórico de conversas

Criar painel web para atendentes

Persistência de dados com banco de dados (SQLite ou PostgreSQL)

Autenticação de atendentes

 Autor

Projeto desenvolvido para fins educacionais, como parte do aprendizado em Python e desenvolvimento de sistemas de atendimento automatizado.

