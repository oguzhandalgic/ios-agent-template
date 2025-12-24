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

## 🔄 Workflow Diagram (Conceptual)

docs/ → Agents read & summarize automatically
   ↓
status.json (locked) → Controls agent readiness & current phase
   ↓
CrewAI orchestrator → Delegates tasks autonomously
   ↓
Specialized Agents (Architect → Coder → Tester → Integrator)
   ↓
GitAgent → Creates feature branch → Commits → Pushes → Creates documented PR
   ↓
GitAgent (analysis) → Runs swiftlint + tests + Claude review
   ↓
Merge to main (if all checks pass) or loop back for fixes
   ↓
Optional: Deploy SaaS landing → Vercel / Netlify / Firebase

## 🛠️ Common Customizations You Might Want

- Change Claude model: Edit `model="claude-4.5-opus-..."` in `base_agent.py`
- Add new agent: Create new file in `agents/`, inherit from `BaseAgent`, add to `crew.py`
- Add new MCP: Import in `base_agent.py` and use in `run_task()`
- Custom branch naming: Modify `create_feature_branch()` in `git_agent.py`
- Stricter PR checks: Extend `analyze_and_merge()` with more tools (Danger, SonarQube, etc.)

## 📊 Current Stack & Versions (Dec 2025)

- Python 3.10+
- CrewAI >= 0.67.1
- Anthropic SDK latest
- LangChain >= 0.3.x (for Context retrieval)
- Claude 4.5 Opus (as of December 2025)

## 🔮 Planned / Nice-to-have Features

- [ ] Automatic changelog generation on merge
- [ ] GitHub Actions for CI validation before PR merge
- [ ] Agent for generating App Store screenshots
- [ ] Voice mode integration (if Claude gets better audio)
- [ ] Better conflict resolution when PR analysis fails

Contributions welcome for any of these!

## 📞 Contact / Questions

Feel free to open an issue if you:
- Run into agent setup problems
- Want to share your project built with this template
- Have ideas for new agents/MCP integrations

Happy building! 🚀

# iOS Agent Template
AI-Powered Multi-Agent Development Workflow for Complex iOS Swift Projects

![Swift](https://img.shields.io/badge/Swift-6.0+-orange?logo=swift&logoColor=white)
![Claude 4.5 Opus](https://img.shields.io/badge/Claude-4.5%20Opus-9F70D1?logo=anthropic)
![CrewAI](https://img.shields.io/badge/CrewAI-0.67%2B-FF6B6B?logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

Template repository for building complex iOS / Swift applications using a multi-agent AI workflow 
powered by Claude 4.5 Opus, CrewAI, and free-tier MCP integrations.

## Features

- Claude 4.5 Opus as core reasoning & code generation model
- CrewAI for autonomous agent orchestration & task delegation
- Strict Git workflow enforced by dedicated GitAgent:
  • Feature branches only (feature/task-xxx-description)
  • No direct pushes to main
  • Automatic PR creation with rich documentation
  • Claude-powered PR analysis + auto-merge when checks pass
- Shared project state via status.json + file locking
- Automatic docs ingestion — agents read /docs/ on startup
- Free MCP integrations (LangChain RAG, CrewAI queuing)
- Supports iOS apps + SaaS landing pages (Vercel/Netlify/Firebase)
- Easy to extend with new agents

## Project Structure

project_root/
├── docs/                  # Documentation — agents read automatically
├── agents/                # All agent implementations
│   ├── base_agent.py
│   ├── architect_agent.py
│   ├── coder_agent.py
│   ├── tester_agent.py
│   ├── integrator_agent.py
│   └── git_agent.py
├── tasks/                 # CrewAI tasks (optional)
├── src/                   # Generated Swift code
├── tests/                 # XCTest files
├── landing/               # SaaS landing page files
├── status.json            # Project state
├── status.lock            # File lock
├── crew.py                # Main orchestrator
├── requirements.txt
├── swiftlint.yml
├── .gitignore
└── README.md

## Quick Start

1. Clone template
   git clone https://github.com/YOUR_USERNAME/ios-agent-template.git my-project
   cd my-project

2. Install dependencies
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. Set secrets
   export ANTHROPIC_API_KEY=sk-ant-...
   export GITHUB_TOKEN=ghp_...

4. Add your project docs to /docs/

5. Initialize status
   echo '{"initialized": true, "phase": "planning", "git_status": "idle", "agents_ready": true}' > status.json

6. Run
   python crew.py

## Recommended free hosting / MCP services (2025)

Vercel     - landing pages, previews
Netlify    - static sites, forms
Firebase   - iOS backend, auth, realtime
Render     - static + services
Replicate  - AI model inference

MIT © 2025 [Your Name]
Happy agentic development! 🚀
