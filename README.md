<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="30%">
</p>

<h1 align="center">AI-AGENT-WITH-DOCKER</h1>

---

## 📚 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
  - [Project Index](#project-index)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)

---

## Overview

A robust **multi-agent system** built with **LangGraph** and **FastAPI** that acts as an intelligent personal assistant.

The system follows a **Supervisor architecture**, where a central **Manager (Supervisor) agent** interprets user requests (for example, _“Research this topic and email me the results”_) and dynamically delegates tasks to specialized agents:

- **Research Agent** — content gathering and generation
- **Email Agent** — sending emails via SMTP

---

## 🚀 Key Features

- **Multi-Agent Orchestration**
  Uses **LangGraph** to manage agent state, execution flow, and hand-offs.

- **Strict Tool Validation**
  Enforces **Pydantic schemas** to prevent hallucinated or malformed tool calls (especially helpful with Llama 3).

- **Resilient Data Handling**
  Custom validators gracefully handle inconsistent AI outputs (e.g., dict vs. string responses).

- **Production-Ready**
  Fully containerized with **Docker** and deployable via **Railway**.

- **REST API**
  Built on **FastAPI** for easy integration with web or backend services.

---

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **AI Framework:** LangChain / LangGraph
- **LLM:** Llama 3.3 70B (via Groq or OpenAI)
- **Backend:** FastAPI
- **Database:** SQLModel (PostgreSQL / SQLite)
- **Deployment:** Docker & Railway


---

##  Project Structure

```sh
└── AI-Agent-with-Docker/
    ├── README.md
    ├── backend
    │   ├── .dockerignore
    │   ├── Dockerfile
    │   ├── railway.json
    │   ├── requirements.txt
    │   └── src
    │       ├── api
    │       │   ├── __init__.py
    │       │   ├── ai
    │       │   │   ├── __init__.py
    │       │   │   ├── agents.py
    │       │   │   ├── assistants.py
    │       │   │   ├── llms.py
    │       │   │   ├── schemas.py
    │       │   │   ├── services.py
    │       │   │   └── tools.py
    │       │   ├── chat
    │       │   │   ├── __init__.py
    │       │   │   ├── models.py
    │       │   │   └── routing.py
    │       │   ├── db.py
    │       │   └── myemailer
    │       │       ├── __init__.py
    │       │       ├── gmail_imap_parser.py
    │       │       ├── inbox_reader.py
    │       │       └── sender.py
    │       ├── ignoreme
    │       │   └── test.txt
    │       └── main.py
    ├── body.json
    ├── compose.yaml
    ├── docker-commands.md
    └── static_html
        ├── src
        │   ├── abc.html
        │   ├── about.html
        │   ├── contact.html
        │   └── index.html
        └── static.Dockerfile
```


###  Project Index
<details open>
	<summary><b><code>AI-AGENT-WITH-DOCKER/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/compose.yaml'>compose.yaml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/body.json'>body.json</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- static_html Submodule -->
		<summary><b>static_html</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/static_html/static.Dockerfile'>static.Dockerfile</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/static_html/src/about.html'>about.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/static_html/src/abc.html'>abc.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/static_html/src/index.html'>index.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/static_html/src/contact.html'>contact.html</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- backend Submodule -->
		<summary><b>backend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/requirements.txt'>requirements.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/railway.json'>railway.json</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/Dockerfile'>Dockerfile</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
			<details>
				<summary><b>src</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/main.py'>main.py</a></b></td>
						<td><code>❯ REPLACE-ME</code></td>
					</tr>
					</table>
					<details>
						<summary><b>ignoreme</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/ignoreme/test.txt'>test.txt</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>api</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/db.py'>db.py</a></b></td>
								<td><code>❯ REPLACE-ME</code></td>
							</tr>
							</table>
							<details>
								<summary><b>chat</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/chat/models.py'>models.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/chat/routing.py'>routing.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>ai</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/ai/services.py'>services.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/ai/llms.py'>llms.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/ai/schemas.py'>schemas.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/ai/assistants.py'>assistants.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/ai/agents.py'>agents.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/ai/tools.py'>tools.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
							<details>
								<summary><b>myemailer</b></summary>
								<blockquote>
									<table>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/myemailer/sender.py'>sender.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/myemailer/inbox_reader.py'>inbox_reader.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									<tr>
										<td><b><a href='https://github.com/SahilSinhaCodes/AI-Agent-with-Docker/blob/master/backend/src/api/myemailer/gmail_imap_parser.py'>gmail_imap_parser.py</a></b></td>
										<td><code>❯ REPLACE-ME</code></td>
									</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with AI-Agent-with-Docker, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install AI-Agent-with-Docker using one of the following methods:

**Build from source:**

1. Clone the AI-Agent-with-Docker repository:
```sh
❯ git clone https://github.com/SahilSinhaCodes/AI-Agent-with-Docker
```

2. Navigate to the project directory:
```sh
❯ cd AI-Agent-with-Docker
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r backend/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t SahilSinhaCodes/AI-Agent-with-Docker .
```




###  Usage
Run AI-Agent-with-Docker using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```

