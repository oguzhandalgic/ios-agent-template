# iOS Agent Template  
**AI-Powered Multi-Agent Development Workflow for Complex iOS Swift Projects**

![Swift](https://img.shields.io/badge/Swift-6.0-orange?logo=swift&logoColor=white)
![Claude 4.5 Opus](https://img.shields.io/badge/Claude-4.5%20Opus-9F70D1?logo=anthropic)
![CrewAI](https://img.shields.io/badge/CrewAI-0.4%2B-FF6B6B?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

Template repository for building complex iOS / Swift applications using a **multi-agent AI workflow** powered by **Claude 4.5 Opus**, **CrewAI**, and free-tier MCP servers.

Every new iOS project can be bootstrapped from this template in minutes — with strict Git flow, automatic documentation reading, shared project status, file locking, feature-branch-only workflow, PR auto-documentation, and automated merging.

## ✨ Features

- **Claude 4.5 Opus** as the core reasoning & code generation model
- **CrewAI** for autonomous agent orchestration & task delegation
- **Strict Git workflow** enforced by dedicated GitAgent:
  - Feature branches only (`feature/task-xxx-description`)
  - No direct pushes to `main`
  - Automatic PR creation with rich documentation
  - Claude-powered PR analysis + automated merge (when checks pass)
- **Shared project state** via `status.json` + file locking (`status.lock`)
- **Automatic docs ingestion** — every agent reads `/docs/` folder on startup
- **Free MCP integrations**:
  - Task management → CrewAI built-in + optional Task Manager style queuing
  - Context retrieval → LangChain RAG over docs + latest Apple docs
- Ready for iOS apps **+** SaaS landing pages (deployable to Vercel/Netlify)
- Modular agent architecture (easy to add new specialized agents)

## 📋 Project Structure

```text
project_root/
├── docs/                  # All project documentation — agents read this automatically
├── agents/                # Agent implementations (all extend BaseAgent)
│   ├── base_agent.py
│   ├── architect_agent.py
│   ├── coder_agent.py
│   ├── tester_agent.py
│   ├── integrator_agent.py
│   └── git_agent.py       # Enforces branch/PR/merge workflow
├── tasks/                 # CrewAI task definitions (optional separation)
├── src/                   # Generated Swift source code
├── tests/                 # XCTest files
├── landing/               # SaaS landing page (HTML/JS/CSS - deployable to Vercel)
├── status.json            # Shared project status (phase, git status, readiness)
├── status.lock            # Prevents concurrent status modifications
├── crew.py                # Main orchestrator — runs the whole workflow
├── requirements.txt       # Python dependencies
├── swiftlint.yml          # SwiftLint configuration for code quality
├── .gitignore
└── README.md              # ← You are here
