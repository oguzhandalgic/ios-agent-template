# iOS Agent Template
**AI-Powered Multi-Agent Development Workflow for Complex iOS Swift Projects**

![Swift](https://img.shields.io/badge/Swift-6.0+-orange?logo=swift&logoColor=white)
![Claude 4.5 Opus](https://img.shields.io/badge/Claude-4.5%20Opus-9F70D1?logo=anthropic)
![CrewAI](https://img.shields.io/badge/CrewAI-0.67%2B-FF6B6B?logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

Template repository for building complex iOS / Swift applications using a **multi-agent AI workflow** 
powered by **Claude 4.5 Opus**, **CrewAI**, and free-tier MCP integrations.

Every new iOS project can be bootstrapped from this template in minutes — with strict Git flow, 
automatic documentation reading, shared project status, file locking, feature-branch-only workflow, 
PR auto-documentation, and automated merging.

## ✨ Features

- **Claude 4.5 Opus** as the core reasoning & code generation model
- **CrewAI** for autonomous agent orchestration & task delegation
- **Strict Git workflow** enforced by dedicated GitAgent:
- Feature branches only (`feature/task-xxx-description`)
- No direct pushes to `main`
- Automatic PR creation with rich documentation (including MCP-retrieved context)
- Claude-powered PR analysis + automated merge (when checks pass)
- **Shared project state** via `status.json` + file locking (`status.lock`)
- **Automatic docs ingestion** — every agent reads & summarizes `/docs/` folder on startup
- **Free MCP integrations**:
- Task management → CrewAI built-in + optional queuing patterns
- Context retrieval → LangChain RAG over docs + latest Apple ecosystem information
- Ready for iOS apps **+** SaaS landing pages (deployable to Vercel/Netlify/Firebase)
- Modular agent architecture — easy to add new specialized agents

## 📋 Project Structure

```
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
├── landing/               # SaaS landing page (HTML/JS/CSS - deployable to Vercel/Netlify)
├── status.json            # Shared project status (phase, git status, readiness)
├── status.lock            # Prevents concurrent status modifications
├── crew.py                # Main orchestrator — runs the whole workflow
├── requirements.txt       # Python dependencies
├── swiftlint.yml          # SwiftLint configuration for code quality
├── .gitignore
└── README.md              # ← You are here
```

## 🚀 Quick Start — Create a New Project

Create new project from template
On GitHub: **Use this template** → Name your new repo  or via CLI:
```bash
git clone https://github.com/YOUR_USERNAME/ios-agent-template.git my-awesome-ios-app
cd my-awesome-ios-app
```

Install Python dependencies
```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Set environment variables (.env or export)
```bash
export ANTHROPIC_API_KEY=sk-ant-...
export GITHUB_TOKEN=ghp_...           # Personal Access Token (repo scope)
# Optional: SERPER_API_KEY, OPENAI_API_KEY, etc. for additional tools/MCPs
```

Prepare your project
```bash
# If using LangChain local vector store
python -m langchain.index docs/
```
- Put requirements, specs, wireframes, architecture notes → `docs/`
- (Recommended) Index docs for better RAG:

Initialize status
```bash
echo '{"initialized": true, "phase": "planning", "git_status": "idle", "agents_ready": true}' > status.json
```

Run the agents!
```bash
python crew.py
```
→ → Watch the agents plan, code, test, commit to feature branches, create PRs, analyze, and merge (if quality passes)

## 🔄 Workflow Diagram (Conceptual)

```
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
```

## ⚙️ Configuration & Customization

| File / Folder | Purpose |
| --- | --- |
| `docs/` | Source of truth — all agents read & summarize it automatically |
| `agents/*.py` | Add/modify agent behaviors (all inherit from `BaseAgent`) |
| `crew.py` | Main workflow — change agents, tasks, dependencies, order |
| `status.json` | Controls agent readiness & current project phase |
| `swiftlint.yml` | Customize linting rules used during PR analysis |
| `landing/` | Optional SaaS landing page — agents can generate/deploy to Vercel |

## 🔐 Security & Best Practices

- **Never commit** API keys → use `.env` + `.gitignore`
- GitHub token should have **repo** scope only (fine-grained if possible)
- `main` branch is **protected** (PR required, status checks recommended)
- Use short-lived feature branches — GitAgent cleans up after merge (configurable)

## 📈 Recommended Free MCP Services (December 2025)

| Service | Use Case | Free Tier Notes |
| --- | --- | --- |
| Vercel | SaaS landing pages, Next.js previews | Generous for personal projects |
| Netlify | Static sites, forms, CMS integration | Very developer-friendly |
| Firebase | iOS backend (auth, realtime, storage) | Spark plan sufficient for dev |
| Render | Static + web services | Free web service tier |
| Replicate | Additional AI model inference (if needed) | Free credits on signup |

## 🛠️ Common Customizations You Might Want

- Change Claude model: Edit `model="claude-4.5-opus-..."` in `base_agent.py`
- Add new agent: Create new file in `agents/`, inherit from `BaseAgent`, add to `crew.py`
- Add new MCP: Import in `base_agent.py` and use in `run_task()`
- Custom branch naming: Modify `create_feature_branch()` in `git_agent.py`
- Stricter PR checks: Extend `analyze_and_merge()` with more tools (Danger, SonarQube, etc.)

## 🔮 Planned / Nice-to-have Features

- [ ] Automatic changelog generation on merge
- [ ] GitHub Actions for CI validation before PR merge
- [ ] Agent for generating App Store screenshots
- [ ] Better conflict resolution when PR analysis fails

## 📄 License

MIT © [Your Name / Your Organization] 2025

## 🤝 Contributing

This is a personal template — feel free to fork & adapt!  
If you find a great improvement (new agent, better MCP integration, Claude prompt engineering, etc.), PRs are very welcome.

Happy agentic iOS & SaaS development! 🚀
