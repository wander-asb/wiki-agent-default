
# 🌐 Chatbot with LangChain and Wikipedia API

Este projeto é um **chatbot inteligente** que responde perguntas com base em dados da **Wikipedia**, utilizando o **LangChain**, **OpenAI GPT** e a API da Wikipedia.

Ele é estruturado com uma arquitetura multiagente, onde um **Supervisor Agent** orquestra subagentes especializados, cada um com um domínio de conhecimento específico.

---
## 📦 Requisitos para rodar o projeto

- Python 3.10+
- API Key da OpenAI configurada no arquivo `.env`

Instale as dependências:

```bash
pip install -r requirements.txt
streamlit run app.py
