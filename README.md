# 🌐 Chatbot with LangChain and Wikipedia API

This project is a chatbot that answers questions based on Wikipedia data using LangChain and OpenAI's GPT models.

                         +---------------------+
                          |  🧠 Supervisor Agent  |
                          +----------+----------+
                                     |
          +--------------------------+----------------------------+
          |                          |                            |
+------------------+      +------------------+         +------------------+
| 📚 Subagent 1     |      | 🌐 Subagent 2     |         | 🎨 Subagent 3     |
| (Geography Expert)|      | (Wikipedia Expert)|         | (Flag Color Expert)|
+------------------+      +------------------+         +------------------+

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py