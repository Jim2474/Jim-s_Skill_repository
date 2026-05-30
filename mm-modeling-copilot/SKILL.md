---
name: mm-modeling-copilot
description: End-to-end mathematical modeling copilot inspired by LLM-MM-Agent (NeurIPS 2025). Use this skill whenever the user asks for math modeling, MCM/ICM/CUMCM-style problems, open-ended quantitative analysis, model selection, computational solving, sensitivity analysis, or generating a modeling paper/report. It implements the full MM-Agent pipeline (problem analysis → decomposition → modeling → solving → reporting) as a Claude Code-native workflow.
---

# MM Modeling Copilot

This skill turns a mathematical modeling task into a Claude Code-native workflow. It adapts the core ideas from the NeurIPS 2025 MM-Agent — Actor-Critic self-correction, hierarchical method retrieval, DAG-based task decomposition, iterative code debugging — into a workflow that runs entirely inside Claude Code without external infrastructure.

## Use Cases

- Mathematical modeling competitions (MCM/ICM/CUMCM)
- Course assignments requiring models and code
- Data-driven decision analysis and consulting
- Optimization, simulation, prediction, evaluation, or ranking problems
- Writing complete modeling reports or LaTeX papers

## Core Workflow (4 Stages)

### Stage 1: Problem Analysis

1. **Data Description**: If data files exist, read and summarize shape, columns, types, missing values, basic stats.
2. **Problem Understanding** (Actor-Critic):
   - Write initial analysis to `problem.md`: background, questions, variables, constraints, objectives, deliverables, ambiguities.
   - Critique the analysis: Are assumptions hiding uncertainty? Are interdependencies captured? Are there alternative framings?
   - Revise based on critique. Do NOT mention the critique in the final output.
3. **Problem Decomposition**:
   - Decompose into N subtasks (typically 3-5 for competition problems, fewer for simple tasks).
   - For each subtask: description, inputs, outputs, dependencies.
   - Build dependency DAG. If unsure, default to linear dependency.
   - Write decomposition to `model_plan.md`.

### Stage 2: Mathematical Modeling (Per Subtask)

For each subtask, in DAG topological order:

1. **Method Retrieval**: Consult `references/hmml-methods.md` for candidate methods. Match problem characteristics to method core ideas and applications.
2. **Model Construction** (Actor-Critic):
   - Define assumptions, variables, objective functions, constraints, equations.
   - Critique: Do assumptions match the data? Is the model solvable? Are there better alternatives?
   - Revise based on critique.
3. Record: chosen method, mathematical formulation, why it fits.

### Stage 3: Computational Solving (Per Subtask)

For each subtask, in DAG order:

1. **Code Generation**: Write Python code in `src/`.
2. **Iterative Debugging**: Run code → check output → fix errors → rerun. Budget up to 5 tries × 3 debug rounds = 15 maximum attempts per subtask.
3. **Result Interpretation**: Interpret outputs in the language of the original problem.
4. **Dependency Passing**: Pass results, generated files, and key decisions to downstream subtasks.
5. **Chart Generation**: When the subtask has data or numerical results, create at least 2 useful figures per substantial subtask. For pure symbolic/theoretical subtasks, use tables, equations, or diagrams instead. Save figures to `figures/`.

### Stage 4: Solution Reporting

1. Run validation checklist (`references/validation-checklist.md`).
2. Perform sensitivity analysis for top 3-5 important parameters.
3. Write final report (`report.md` by default, or `report.tex` when the user asks for LaTeX/competition-paper output).
4. Use template from `references/report-template.md`.

## Default Directory Layout

Create this in the current workspace unless the user specifies another location:

```text
mm_modeling_output/
├── problem.md          # Problem analysis
├── assumptions.md      # Numbered assumptions with rationale
├── symbols.md          # Symbol table
├── model_plan.md       # Decomposition + model selection
├── data/               # Input data files
├── src/                # Python scripts
│   ├── load_data.py
│   ├── task_1_model.py
│   ├── task_1_solve.py
│   ├── task_2_model.py
│   ├── ...
│   ├── plot_results.py
│   ├── sensitivity.py
│   └── utils.py
├── figures/            # Generated plots
├── results/            # Tables, metrics, intermediate outputs
└── report.md           # Final report (or report.tex)
```

To initialize:

```powershell
python "$HOME\.claude\skills\mm-modeling-copilot\scripts\init_modeling_project.py" --output "mm_modeling_output"
```

## References

Read only the reference files needed for the task:

- `references/workflow.md`: detailed step-by-step workflow with Actor-Critic loops, debugging protocol, and dependency management.
- `references/hmml-methods.md`: hierarchical method library with core ideas and applications for 90+ modeling methods.
- `references/report-template.md`: Markdown and LaTeX report templates.
- `references/validation-checklist.md`: 5-dimension, 10-subcriteria evaluation checklist with self-scoring.

## Model Selection Decision Tree

```
Problem asks for...
├── Best allocation / schedule / route / plan
│   └── OPTIMIZATION: LP → MIP → nonlinear → metaheuristic
├── Future values / trends / forecasts
│   └── PREDICTION: regression → time series → ML regression
├── Rank / score / compare alternatives
│   └── EVALUATION: entropy weight + TOPSIS → AHP → PCA
├── Group / classify observations
│   └── CLASSIFICATION: logistic regression → tree-based → SVM
│   └── CLUSTERING: k-means → DBSCAN → hierarchical
├── Network / graph / connectivity
│   └── GRAPH: shortest path → flow → centrality → community
├── Randomness / uncertainty / queues
│   └── SIMULATION: Monte Carlo → discrete-event → agent-based
├── Change over time / dynamics
│   └── DIFF EQUATIONS: ODE → compartmental → control systems
├── Evidence / hypothesis / testing
│   └── STATISTICS: hypothesis tests → Bayesian → bootstrap
└── Multiple types combined
    └── Use baseline model per type, then integrate
```

## Coding Standards

- Use Python unless the user requests another language.
- Prefer simple, reproducible scripts over notebooks unless the user asks for notebooks.
- **Always set random seeds**: `np.random.seed(42)`, `random.seed(42)`.
- Save all charts to `figures/` with descriptive filenames.
- Save tables and metrics to `results/` as CSV or JSON.
- Include enough comments for reproducibility, not line-by-line narration.
- **Always run the code.** Never present code without execution.
- Handle missing data explicitly (don't silently drop rows).
- Use standard libraries: numpy, pandas, scipy, scikit-learn, matplotlib, statsmodels.

## Actor-Critic Protocol

At every major reasoning step (problem analysis, model selection, formula development):

1. **Generate** an initial output (the "actor").
2. **Critique** focusing ONLY on weaknesses. Do not offer solutions in the critique.
3. **Revise** to address the weaknesses. Do NOT mention the critique or previous version.

This produces a single polished output that reads as if it were written correctly the first time.

## Final Response

Tell the user:

- Which files were created.
- Which model(s) were selected and why.
- What the key results are, with specific numbers when the task produced numerical results.
- How to rerun the code (exact commands).
- Any assumptions or missing data that still matter.
- Self-evaluation score from the validation checklist.
