<p align="center">
  <a href="https://github.com/daltonnyx/AgentCrew">
    <img src="https://saigontechnology.com/wp-content/uploads/2024/09/logo-black-1.svg" alt="AgentCrew Logo" width="300">
  </a>
</p>
<h1 align="center">AgentCrew: Your Multi-Agent AI Assistant Framework</h1>

[![GitHub stars](https://img.shields.io/github/stars/saigontechnology/AgentCrew)](https://github.com/saigontechnology/AgentCrew/stargazers)
[![Pylint](https://github.com/saigontechnology/AgentCrew/actions/workflows/pylint.yml/badge.svg)](https://github.com/saigontechnology/AgentCrew/actions/workflows/pylint.yml)
[![CodeQL](https://github.com/saigontechnology/AgentCrew/actions/workflows/codeql.yml/badge.svg)](https://github.com/saigontechnology/AgentCrew/actions/workflows/codeql.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](https://github.com/saigontechnology/AgentCrew/blob/main/LICENSE)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-blue)](https://github.com/saigontechnology/AgentCrew/releases)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://hub.docker.com/r/daltonnyx/agentcrew)

## Introduction

<p align="center">
  <img src="./AgentCrew/assets/agentcrew_logo.png" alt="AgentCrew Logo" width="128">
</p>

**What is AgentCrew?**

AgentCrew helps you build AI assistants. You can create a team of AI "agents."
Each agent focuses on a specific area. These agents work together to complete
tasks. This teamwork can produce good results.

**Who Might Like AgentCrew?**

AgentCrew is for anyone interested in AI assistants. If you want to see how
different AIs can team up, or if you want to build your own AI helpers,
AgentCrew can help.

**Key Benefits**

- **Solves Complex Problems:** Use an AI team for tasks too big for one AI.
- **Works with Many AI Models:** Supports AI from OpenAI (GPT), Anthropic
  (Claude), Google (Gemini), GitHub Copilot, and others. Switching models is
  simple.
- **Creates Expert Agents:** Make AI agents for specific jobs, like writing or
  research.
- **Connects to Other Tools:** Agents can use external software through the
  Model Context Protocol (MCP).
- **User Control:** You can approve or deny when an agent wants to use a tool.
- **Simple to Use:** Chat with your AI agents using a text display or a
  graphical window.
- **Manages Conversations:** Easily go back to earlier messages or combine
  messages.

**Short Demo**

<https://github.com/user-attachments/assets/32876eac-b5e6-4608-bd5e-82d6fa4db80f>

## 💡 Core Ideas Behind AgentCrew

AgentCrew uses these main ideas:

1. **AI Teamwork:** Just like a human team. Each person has a special skill.
   Projects work when these specialists help each other. AgentCrew applies this
   idea to AI. You create different AI agents. Each has its own instructions and
   tools. For example, one agent might find information online. Another might
   write summaries.

2. **Smart Task Sharing:** Agents in AgentCrew can decide to pass tasks to
   another agent. They have instructions on when and how to share work and
   information. This lets the right AI take over at the right time.

3. **Flexible AI Models Selection:** AgentCrew lets you use different AI models
   (Large Language Models like GPT or Claude). You are not stuck with one AI
   provider. AgentCrew makes it easy to connect and use the AI model you choose.

## ✨ Key Features

Here are some things AgentCrew can do:

**🤖 Wide AI Model Support:**

- Works with AI from Anthropic (Claude series), Google (Gemini series), OpenAI
  (GPT series), Groq, and DeepInfra.
- Supports **GitHub Copilot**. Set up authentication with
  `agentcrew copilot-auth`.
- Connect to custom AI providers compatible with OpenAI.

**🚀 Strong Agent Capabilities:**

- Define multiple AI agents, each with its own expertise.
- Agents can pass tasks to other agents when they need to.
- Customize each agent's system prompt. You can include information like the
  current date.

**🔄 Adaptive Behaviors for Agents:**

- Use the `adapt` tool to declare rules in a `"when...do..."` format. For
  example,
  `when user asks for code examples, do provide complete annotated snippets`.
- Agents automatically store and apply these behaviors to keep improving
  interactions.
- Manage and update adaptive rules at any time for fine-tuned personalization.

**🛠️ Powerful Tools for Agents with User Control:**

- **Tool Call Approval:** You decide if an agent can use a tool. AgentCrew will
  ask for your permission before a tool is run. This gives you more control.
- **Model Context Protocol (MCP):** Lets agents connect to external tools like
  Jira.
- **Web Search:** Agents can find current information online.
- **Clipboard Access:** Agents can copy text from your clipboard or write text
  to it.
- **Memory:** Agents remember past parts of your conversation. This helps them
  give relevant replies. You can tell agents to forget certain topics.
- **Code Assistance:** Agents can analyze code and help with coding tasks.

**💬 Easy Interaction and Chat Management:**

- **Dual Interfaces:** Chat with AgentCrew using a text console or a graphical
  window (GUI).
- **File Handling:** AI agents can work with text and image files in chat.
  AgentCrew also supports PDF, DOCX, XLSX, and PPTX files.
- **📋 Smart Paste Detection:** Automatically detects images and binary content when pasted (Ctrl+V). Images from screenshots, copied files, or other sources are automatically converted to `/file` commands for seamless processing.
- **Streaming Responses:** Get real-time replies from AI agents.
- **"Thinking Mode":** Some AI models can show their reasoning process.
- **Rollback Messages:** Easily go back to an earlier point in your
  conversation.
- **Consolidate Messages:** Combine multiple chat messages into one using the
  `/consolidate` command.

**⚙️ Simple Configuration:**

- Set up AgentCrew using text files or, more easily, through its **graphical
  user interface (GUI)**.
- The GUI helps you manage API keys, agent settings, and MCP server connections.
- Save and load your conversation histories.

## ✅ Prerequisites

- Python 3.12 or newer.
- `uv` (a fast Python package manager). Install it with `pip install uv`.
- Git (a system for managing code versions).
- API keys for the AI models you plan to use. You need at least one API key.

## 📦 Installation

You can install AgentCrew using a quick script or by following standard steps.

**Quick Install (Linux and MacOS):**

```bash
curl -LsSf https://agentcrew.dev/install.sh | bash
```

**Quick Install (Windows):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://agentcrew.dev/install.ps1 | iex"
```

**Standard Installation (Good for all computers):**

1. **Get the code:**

   ```bash
   git clone https://github.com/saigontechnology/AgentCrew.git
   cd AgentCrew
   ```

2. **Set up a Python environment:**

   ```bash
   uv sync
   uv run AgentCrew/main.py chat
   ```

3. **Install AgentCrew:**

   ```bash
   uv tool install .
   ```

**Docker Installation:**

If you prefer containerized deployment or want to avoid local Python setup:

1. **Using Pre-built Image (Recommended):**

   ```bash
   # Pull and run the latest image
   docker pull daltonnyx/agentcrew:latest

   # Run with console interface
   docker run -it --rm \
     -e ANTHROPIC_API_KEY="your_claude_api_key" \
     -e OPENAI_API_KEY="your_openai_api_key" \
     daltonnyx/agentcrew chat
   ```

2. **Building from Source:**

   ```bash
   # Clone the repository
   git clone https://github.com/saigontechnology/AgentCrew.git
   cd AgentCrew

   # Build Docker image (must be run from project root)
   docker build -f docker/Dockerfile -t agentcrew-ai .

   # Or use the provided build script
   ./docker/build.sh
   ```

3. **Docker Features:**
   - **Console Mode Only:** GUI is disabled in Docker for better compatibility
     and smaller image size
   - **Persistent Data:** Use Docker volumes to persist conversations and
     settings
   - **A2A Server Mode:** Run as a server exposing agents via HTTP API
   - **Multiple AI Providers:** Same provider support as the regular
     installation

## 🐳 Docker Usage

**Quick Start with Docker:**

```bash
# Interactive console mode
docker run -it --rm \
  -e ANTHROPIC_API_KEY="your_api_key" \
  daltonnyx/agentcrew chat

# With persistent data
docker volume create agentcrew_data
docker run -it --rm \
  -v agentcrew_data:/home/agentcrew/.AgentCrew \
  -e ANTHROPIC_API_KEY="your_api_key" \
  daltonnyx/agentcrew chat

# A2A Server mode (HTTP API)
docker run -d \
  --name agentcrew-server \
  -p 41241:41241 \
  -e ANTHROPIC_API_KEY="your_api_key" \
  daltonnyx/agentcrew a2a-server --host 0.0.0.0 --port 41241
```

**Custom Configuration with Docker:**

```bash
# Create custom agents configuration
cat > custom_agents.toml << EOF
[[agents]]
name = "researcher"
description = "AI Research Assistant"
system_prompt = """You are a research assistant specialized in finding and analyzing information.
Current date: {current_date}
"""
tools = ["memory", "web_search", "code_analysis"]

[[agents]]
name = "coder"
description = "AI Coding Assistant"
system_prompt = """You are a coding assistant specialized in software development.
Current date: {current_date}
"""
tools = ["memory", "clipboard", "code_analysis"]
EOF

# Run with custom configuration
docker run -it --rm \
  -v $(pwd)/custom_agents.toml:/home/agentcrew/.AgentCrew/agents.toml:ro \
  -e ANTHROPIC_API_KEY="your_api_key" \
  daltonnyx/agentcrew chat --agent-config /home/agentcrew/.AgentCrew/agents.toml
```

For complete Docker documentation, see [`docker/DOCKER.md`](docker/DOCKER.md).

## ▶️ Getting Started / Basic Usage

Chat with AgentCrew using its interface. The graphical interface (GUI) is
usually the easiest way to start for local installations. **Docker users will
automatically use the console interface** as GUI is disabled in containers for
better compatibility.

**Using the command line (Local Installation):**

To start AgentCrew, open your terminal and use the `agentcrew chat` command.
Here are some common ways to use it (assuming you have installed AgentCrew using
the steps above):

- **Start with the GUI (default):**

  ```bash
  agentcrew chat
  ```

- **Start with the console interface:**

  ```bash
  agentcrew chat --console
  ```

- **Choose a specific AI provider (e.g., OpenAI) for the main chat:**

  ```bash
  agentcrew chat --provider openai --console
  ```

  _(Replace `openai` with `claude`, `groq`, `google`, `deepinfra`, or
  `github_copilot` as needed.)_

- **Specify a custom agent configuration file:**

  ```bash
  agentcrew chat --agent-config /path/to/your/agents.toml
  ```

- **Specify a custom MCP servers configuration file:**

  ```bash
  agentcrew chat --mcp-config /path/to/your/mcp_servers.json
  ```

- **Choose a specific AI model for memory processing:**

  ```bash
  agentcrew chat --memory-llm claude --console
  ```

  _(This sets which AI model helps the system analyze and manage conversation
  memory. Replace `claude` with `openai`, `groq`, `google`, `deepinfra`, or
  `github_copilot`.)_

- **Combine options:**

  ```bash
  agentcrew chat --provider google --memory-llm openai --agent-config custom_agents.toml --console
  ```

_Remember to replace `/path/to/your/agents.toml` and
`/path/to/your/mcp_servers.json` with the actual paths to your configuration
files if you use those options._

**Using Docker Commands:**

For Docker users, replace `agentcrew` with the full Docker command:

```bash
# Basic Docker usage (equivalent to agentcrew chat)
docker run -it --rm \
  -e ANTHROPIC_API_KEY="your_key" \
  daltonnyx/agentcrew chat

# With specific provider (equivalent to agentcrew chat --provider openai)
docker run -it --rm \
  -e OPENAI_API_KEY="your_key" \
  daltonnyx/agentcrew chat --provider openai

# With custom config (mount config files)
docker run -it --rm \
  -v $(pwd)/custom_agents.toml:/home/agentcrew/.AgentCrew/agents.toml:ro \
  -e ANTHROPIC_API_KEY="your_key" \
  daltonnyx/agentcrew chat --agent-config /home/agentcrew/.AgentCrew/agents.toml

# A2A Server mode
docker run -d -p 41241:41241 \
  -e ANTHROPIC_API_KEY="your_key" \
  daltonnyx/agentcrew a2a-server --host 0.0.0.0 --port 41241
```

**To set up GitHub Copilot authentication:**

_Local installation:_

```bash
agentcrew copilot-auth
```

_Docker:_

```bash
# Interactive authentication with persistent storage
docker run -it --rm \
  -v agentcrew_data:/home/agentcrew/.AgentCrew \
  daltonnyx/agentcrew copilot-auth
```

**In-Chat Commands (for console and GUI):**

- `/clear` or `Ctrl+L`: Starts a new chat.
- `/copy` or `Ctrl+Shift+C`: Copies the AI's last reply.
- `/file <path/to/file>`: Adds a file's content to your message.
- `/agent [agent_name]`: Switches to a different AI agent.
- `/consolidate <num_of_preserve_messages>`: Combines selected messages into
  one.
- `/think <level>`: Turns on "thinking mode" for some AIs. Example:
  `/think medium`. Use `/think 0` to turn it off.
- `exit` or `quit`: Closes the chat.

## 🔧 Configuration Overview

AgentCrew needs API keys for AI models. You also define your AI agents. **The
easiest way to configure AgentCrew is through its graphical user interface
(GUI).**

- **API Keys:** Needed for services like OpenAI or GitHub Copilot. Manage these
  in the GUI (Settings -> Global Settings) or set them as environment variables.
- **Agent Definitions:** Describe your agents (name, skills, tools) in the GUI
  (Settings -> Agents). This edits the `agents.toml` file, usually in
  `~/.AgentCrew/agents.toml`.
- **Global Settings & MCP Servers:** Manage other settings and Model Context
  Protocol server connections using the GUI. This updates files like
  `~/.AgentCrew/config.json` and `~/.AgentCrew/mcp_servers.json`.

For full configuration details, see `CONFIGURATION.md` (this file will contain
detailed setup information).

## 👨‍💻 Development & Customization

If you are a developer, you can add to AgentCrew:

- **New Tools:** Create new tool modules in the `AgentCrew/modules/` folder.
- **New AI Providers:** Add support for more AI services. For OpenAI-compatible
  ones, add them through the GUI or by editing `config.json`.
- **Custom Agents:** Edit agent settings using the GUI or directly in the
  `agents.toml` file.
- **Share Example Agents:** You can create useful agent configurations and share
  them with the community by adding them to the `examples/agents/` folder in the
  project.

## ⚠️ Security and Responsible Usage Advisory ⚠️

You control how AgentCrew and its AI agents work. You are responsible for:

- The instructions you give your AI agents.
- The tools you let agents use. The **Tool Call Approval** feature helps you
  manage this.
- Any results from your prompts or tool setups. This includes risks like data
  leaks or unintended actions.

Please review all prompts and tool settings.

- Give agents only the permissions they truly need.
- Do not put secret information (like passwords or API keys) directly in agent
  prompts.
- Be very careful with tools that can access many files or the internet, even
  with approval.

AgentCrew is powerful. Please use it responsibly.

## 🤝 Contributing

We welcome contributions. Feel free to submit pull requests or open issues for
bugs, new ideas, or improvements.

## 📜 License

AgentCrew is available under the [Apache 2.0 License](LICENSE).
