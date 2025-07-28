# 🎮🤖 AI Dev Tool Showdown: Catcher Game Challenge

[![YouTube Video](https://img.shields.io/badge/🎥%20Watch-YouTube-red)](https://youtu.be/NwgSDL2SWTc)  
Comparing **AI coding assistants** by having each build the same Pygame arcade game!

---

## 📋 Table of Contents

- [📖 Overview](#-overview)
- [🕹️ The Game: Catcher](#️-the-game-catcher)
- [🧠 AI Tools Tested](#-ai-tools-tested)
- [🎯 Project Goals](#-project-goals)
- [🏆 Results Summary](#-results-summary)
- [🚀 How to Run](#-how-to-run)
- [📁 Project Structure](#-project-structure)

---

## 📖 Overview

This repository is part of a **graduate project** and YouTube video: **_AI Dev Tool Showdown: GitHub Copilot vs Amazon Q & Gemini CLI vs Claude Code_**  

The challenge: Give multiple **AI coding assistants** the **same prompt** and evaluate their ability to plan, document, and implement a Pygame arcade game called **Catcher**.

---

## 🕹️ The Game: Catcher

A simple but addictive arcade game where:

- 🎯 **Goal:** Catch falling objects with a paddle at the bottom of the screen.
- 🎮 **Controls:** Move the catcher horizontally using **A/D keys** or **mouse movement**.
- ⭐ **Scoring:** Gain points for each caught object.

---

## 🧠 AI Tools Tested

This project compares implementations from:

- **🟡 Gemini CLI** → `catcher-gemini/`
- **💬 Claude Code** → `catcher-claude/`

Each AI tool was asked to provide:

1. 📄 **A documentation plan** (objectives, architecture, milestones)  
2. 🎮 **A user guide** (controls, scoring, instructions)  
3. 🐍 **A runnable Pygame app** implementing Catcher  

---

## 🎯 Project Goals

The showdown evaluates each tool on:

- **🧩 Code Quality** – Clean, readable, well-structured code  
- **✅ Feature Completeness** – Which tool delivers a more complete game?  
- **📝 Documentation** – Quality of docs and guides  
- **✨ Game Polish** – UX, graphics, and mechanics  
- **🏗️ Code Architecture** – Use of OOP and modular design  

---

## 🏆 Results Summary

**Key Takeaways:**

| Tool         | Strengths ✅                                           | Weaknesses ⚠️               |
|--------------|------------------------------------------------------|-----------------------------|
| **Claude Code** | Polished mechanics (combo multipliers, pause feature) | More complex, a few minor bugs |
| **Gemini CLI**  | Simpler, bug-free, clean core gameplay              | Lacks extra features & polish |

---

## 🚀 How to Run

### 📦 Prerequisites

Install Python 3.9+ and Pygame:

```bash
pip install pygame
```

### ▶️ Run the Game

Choose your preferred implementation:

```bash
# Gemini CLI version
cd catcher-gemini
python main.py

# Claude Code version
cd catcher-claude
python catcher.py
```

---

## 📁 Project Structure

```text
catcher/
├── catcher-gemini/        # Gemini CLI implementation
│   ├── main.py            # Entry point for Gemini version
│   └── ...                
├── catcher-claude/        # Claude Code implementation
│   ├── catcher.py         # Entry point for Claude version
│   └── ...
├── docs/                  # Docs, user guides, and plans
└── README.md              # This file
```

---

## 🎥 Related Content

📺 **Watch the full comparison on YouTube:** [AI Dev Tool Showdown](https://youtu.be/NwgSDL2SWTc)
