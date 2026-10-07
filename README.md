#  AI Agent for Manufacturing Data Integration

An autonomous AI agent designed to query, analyze, and report on manufacturing process data via custom API endpoints. This project demonstrates the intersection of traditional backend engineering and Agentic AI, showcasing how Large Language Models (LLMs) can be given "tools" to interact with real-world industrial data.

## 🚀 Key Features

- **Autonomous Reasoning:** Uses a ReAct (Reasoning + Acting) loop to dynamically decide when and how to query data based on natural language prompts.
- **Anomaly Detection:** Automatically identifies and highlights manufacturing anomalies (e.g., torque value errors) without hardcoded `if/else` logic.
- **RESTful Backend:** FastAPI server serving structured machine data from a relational database.
- **Production-Ready Architecture:** Fully containerized using Docker and Docker Compose for reproducible, isolated environments.
- **Local & Private LLM Integration:** Powered entirely by Ollama (Llama 3.2), ensuring sensitive manufacturing data never leaves the local environment.
## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Backend API:** FastAPI, Uvicorn, Pydantic
- **AI & Orchestration:** LangChain, LangGraph
- **Database:** SQLite
- **Deployment:** Docker, Docker Compose
- **LLM Provider:** Ollama (Llama 3.2)

## 📂 Project Structure

```text
.
├── app.py                # FastAPI backend serving machine data
├── agent.py              # LangChain AI agent logic and tool definitions
├── setup_db.py           # Database initialization and dummy data seeding
├── requirements.txt      # Python dependencies
├── Dockerfile            # Container definition for the application
├── docker-compose.yml    # Orchestrates the API and Agent containers
└── README.md             # Project documentation
