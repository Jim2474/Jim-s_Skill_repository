# MM Modeling Copilot

Claude Code-native mathematical modeling workflow implementing the core ideas from [MM-Agent (NeurIPS 2025)](https://github.com/usail-hkust/LLM-MM-Agent). Runs entirely inside Claude Code without external infrastructure.

## Key Features

- **Actor-Critic self-correction** at every reasoning step (analysis, modeling, formulation)
- **Problem decomposition** with DAG-based dependency ordering
- **Hierarchical method library** (90+ methods with core ideas and applications)
- **Iterative code debugging** for computational subtasks (5 tries × 3 debug rounds = 15 max attempts)
- **5-dimension validation** with self-scoring checklist
- **Dual report format** (Markdown + LaTeX for competitions)

## Installed Pieces

| Component | Path | Purpose |
|---|---|---|
| Subagent | `~/.claude/agents/mm-modeling-agent.md` | Autonomous modeling specialist |
| Command | `~/.claude/commands/mm-model.md` | `/mm-model` one-click workflow |
| Skill | `~/.claude/skills/mm-modeling-copilot/SKILL.md` | Workflow reference |
| Methods | `~/.claude/skills/mm-modeling-copilot/references/hmml-methods.md` | 90+ method library |
| Workflow | `~/.claude/skills/mm-modeling-copilot/references/workflow.md` | Detailed step-by-step |
| Templates | `~/.claude/skills/mm-modeling-copilot/references/report-template.md` | MD + LaTeX templates |
| Checklist | `~/.claude/skills/mm-modeling-copilot/references/validation-checklist.md` | 5-dim evaluation |
| Init | `~/.claude/skills/mm-modeling-copilot/scripts/init_modeling_project.py` | Project bootstrapper |

## Usage

### Quick Start (Slash Command)

```text
/mm-model 根据 @problem.pdf 和 @data.xlsx 完成数学建模报告
```

### Natural Language

```text
帮我做这个数学建模题，读题、建模、写代码求解、生成 report.md
```

### Competition Paper

```text
/mm-model MCM Problem C: [problem description]. 生成 LaTeX 论文。
```

## Pipeline

```
Stage 1: Problem Analysis (Actor-Critic)
  ├── Data summary
  ├── Problem understanding (generate → critique → revise)
  └── Decomposition into subtasks + DAG

Stage 2: Mathematical Modeling (per subtask, DAG order)
  ├── Method retrieval from HMML library
  └── Model construction (Actor-Critic)

Stage 3: Computational Solving (per subtask, DAG order)
  ├── Code generation
  ├── Iterative debugging (5 × 3 = 15 max attempts)
  ├── Result interpretation
  └── Dependency passing to next subtask

Stage 4: Reporting
  ├── Validation checklist (5 dimensions, 50-point scale)
  ├── Sensitivity analysis
  └── Report generation (MD or LaTeX)
```

## Output Structure

```
mm_modeling_output/
├── problem.md          # Problem analysis
├── assumptions.md      # Numbered assumptions
├── symbols.md          # Notation table
├── model_plan.md       # Decomposition + model selection
├── data/               # Input data
├── src/                # Python scripts (with starter files)
│   ├── load_data.py
│   ├── utils.py
│   ├── plot_results.py
│   └── sensitivity.py
├── figures/            # Generated plots
├── results/            # Tables and metrics
└── report.md           # Final report
```

## Bootstrap

```powershell
python "$HOME\.claude\skills\mm-modeling-copilot\scripts\init_modeling_project.py" --output "mm_modeling_output"
```

For LaTeX/contest-paper projects:

```powershell
python "$HOME\.claude\skills\mm-modeling-copilot\scripts\init_modeling_project.py" --output "mm_modeling_output" --latex
```
