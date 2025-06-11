<p align="center">
  <a href="https://github.com/daltonnyx/AgentCrew">
    <img src="https://saigontechnology.com/wp-content/uploads/2024/09/logo-black-1.svg" alt="AgentCrew Logo" width="300">
  </a>
</p>
<h1 align="center">AgentCrew: Your Multi-Agent AI Assistant Framework</h1>

[![GitHub stars](https://img.shields.io/github/stars/saigontechnology/AgentCrew)](https://github.com/saigontechnology/AgentCrew/stargazers)
[![Pylint](https://github.com/saigontechnology/AgentCrew/actions/workflows/pylint.yml/badge.svg)](https://github.com/saigontechnology/AgentCrew/actions/workflows/pylint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/saigontechnology/AgentCrew/blob/main/LICENSE)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-blue)](https://github.com/saigontechnology/AgentCrew/releases)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/release/python-3120/)

## ℹ️ Introduction

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
_Coming soon_

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

**🛠️ Powerful Tools for Agents with User Control:**

- **Tool Call Approval:** You decide if an agent can use a tool. AgentCrew will
  ask for your permission before a tool is run. This gives you more control.
- **Model Context Protocol (MCP):** Lets agents connect to external tools like
  Jira, with your approval.
- **Web Search:** Agents can find current information online, with your
  approval.
- **Clipboard Access:** Agents can copy text from your clipboard or write text
  to it, with your approval.
- **Memory:** Agents remember past parts of your conversation. This helps them
  give relevant replies. You can tell agents to forget certain topics.
- **Code Assistance:** Agents can analyze code and help with coding tasks, with
  your approval.

**💬 Easy Interaction and Chat Management:**

- **Dual Interfaces:** Chat with AgentCrew using a text console or a graphical
  window (GUI).
- **File Handling:** AI agents can work with text and image files in chat.
  AgentCrew also supports PDF, DOCX, XLSX, and PPTX files.
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
curl -LsSf https://gist.githubusercontent.com/daltonnyx/aa45d64fd8fb6a084067d4012a5710a6/raw/116f24fe3d94f0c1a972da92cac2f278a59fdad6/install.sh | bash
```

**Quick Install (Windows):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://gist.githubusercontent.com/daltonnyx/e2d9a4d371e095bfa07cf5246d7e0746/raw/af138f99ed5351dc59cae81143e058ef95b5fa37/install.ps1 | iex"
```

_(Note: The Windows script is generated by AI and have not been tested. Your
feedback is welcome if you have trouble.)_

**Standard Installation (Good for all computers):**

1. **Get the code:**

   ```bash
   git clone https://github.com/daltonnyx/AgentCrew.git
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

## ▶️ Getting Started / Basic Usage

Chat with AgentCrew using its interface. The graphical interface (GUI) is
usually the easiest way to start.

**Using the command line:**

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

**To set up GitHub Copilot authentication:** Before using GitHub Copilot as a
provider, run:

```bash
agentcrew copilot-auth
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

AgentCrew is available under the [MIT License](LICENSE).
