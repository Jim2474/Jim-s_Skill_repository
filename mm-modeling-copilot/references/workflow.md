# Mathematical Modeling Workflow

## 1. Intake

Collect:

- Problem statement (text, PDF, or image)
- Data files (CSV, Excel, JSON, etc.)
- Required output format (contest paper, course homework, technical report)
- Deadline or scope constraints
- Number of subtasks or questions to answer

If the task is underspecified, proceed with explicit assumptions rather than stopping unless the missing information changes the model completely.

## 2. Problem Analysis (Actor-Critic)

Write `problem.md` with:

- Background and decision context
- Questions to answer
- Decision variables
- Known inputs and available data
- Unknown parameters
- Constraints
- Objective functions or evaluation metrics
- Deliverables
- Ambiguities and assumptions

**Self-correction**: After the initial analysis, critique it by asking:

1. Are the assumptions too strong or hiding uncertainty?
2. Are there interdependencies between variables not captured?
3. Are there temporal dynamics or feedback loops?
4. What alternative framings exist?
5. What would break if any assumption is wrong?

Revise the analysis based on the critique. Do NOT mention the critique process in the final output.

## 3. Problem Decomposition

For problems with multiple questions or complex scope:

1. Decompose into N subtasks (typically 3-5).
2. For each subtask, write: description, inputs, outputs, dependencies on other subtasks.
3. Build a dependency graph (DAG) of subtasks.
4. Compute execution order via topological sort.
5. If unsure about dependencies, default to linear: task 2 depends on task 1, task 3 depends on tasks 1-2, etc.

Write the decomposition to `model_plan.md`.

For simple single-question tasks, skip decomposition and treat as one subtask.

## 4. Assumptions

Write `assumptions.md`.

Good assumptions should:

- Simplify the model without destroying the problem.
- Be defensible and cite domain knowledge when available.
- Be testable or at least discussable.
- Avoid hiding important uncertainty.
- Be numbered so validation can reference them.

## 5. Symbols

Write `symbols.md` with a table:

| Symbol | Meaning | Unit | Type |
|---|---|---|---|
| | | | Decision / Parameter / Variable |

## 6. Model Selection and Plan

Write `model_plan.md` with:

- Candidate model families (consult `references/hmml-methods.md`)
- For each candidate: core idea, why it fits, what assumptions it requires, limitations
- Selected baseline model and rationale
- Optional enhanced models for comparison
- Data requirements per model
- Evaluation metrics
- Validation plan
- Sensitivity analysis plan

**Self-correction**: After proposing models, critique:

1. Do the model assumptions match problem characteristics?
2. Can the chosen framework mirror the problem's logical structure?
3. Are the variable types compatible with the model?
4. Does the model handle the problem's temporal dynamics?
5. Is there a practical, implementable solution method?

Revise the model plan based on the critique.

## 7. Computation (Per Subtask, in DAG Order)

For each subtask, in dependency order:

### 7a. Task Analysis
Analyze the specific subtask in context of the overall problem and any dependent subtask results.

### 7b. Formula Development (Actor-Critic)
- Write mathematical formulations: objective functions, constraints, equations.
- Critique the formulations for correctness, completeness, and solvability.
- Revise based on critique.

### 7c. Code Generation
Use scripts under `src/`. Recommended structure:

- `src/load_data.py` — data loading and preprocessing
- `src/task_{i}_model.py` — model implementation for subtask i
- `src/task_{i}_solve.py` — solver/computation for subtask i
- `src/plot_results.py` — visualization
- `src/sensitivity.py` — sensitivity analysis
- `src/utils.py` — shared utilities

### 7d. Iterative Debugging
**Critical**: Do not accept the first code run. Use this loop:

```
for try in 1..5:
    run code
    if success:
        inspect output for sanity
        if output looks wrong:
            fix logic and retry
        else:
            break
    else:
        read error message
        for debug in 1..3:
            fix the specific error
            rerun
            if success: break
```

Maximum effort: 5 attempts × 3 debug rounds = 15 total runs per subtask.

### 7e. Result Interpretation
After successful execution:
- Interpret results in the language of the original problem.
- Check if results answer the subtask's question.
- Record results for downstream subtasks.

### 7f. Dependency Passing
When moving to the next subtask, provide context from completed subtasks:
- Task description and results summary
- Key modeling decisions made
- Generated files that can be reused (data files, utility functions)
- Explicit instruction: reuse existing outputs instead of redoing work.

## 8. Validation

Perform for each subtask and for the overall solution:

- Shape and missing-value checks on data
- Unit consistency checks
- Extreme-case and boundary checks
- Constraint violation checks
- Error metrics for predictions (RMSE, MAE, R², MAPE)
- Cross-validation where appropriate
- Stability checks under parameter perturbation
- Comparison with baseline or naive methods

## 9. Sensitivity Analysis

For each important parameter or assumption:

1. Define a reasonable range of variation (±10%, ±20%, or domain-specific).
2. Rerun the model with varied parameters.
3. Record how the objective/output changes.
4. Classify sensitivity: insensitive / moderately sensitive / highly sensitive.
5. Save sensitivity plots to `figures/` when the task has numerical parameters; otherwise explain why sensitivity analysis is qualitative.

## 10. Reporting

Write `report.md` as a self-contained final answer.

Include equations, tables, and figures. Link generated files using relative paths inside the report.

### Report Format Options

**Markdown report** (default):
Use the template in `references/report-template.md`.

**LaTeX paper** (for competitions):
When the user requests a contest paper or LaTeX output:
- Generate a `.tex` file using the MCM/ICM `mcmthesis` template or the fallback article template.
- Include proper sections: Abstract, Problem Restatement, Assumptions, Symbols, Model Construction, Solutions (per subtask), Sensitivity, Strengths/Weaknesses, Conclusions.
- Include figures as `\includegraphics` references.
- Include a notation table extracted from `symbols.md`.
- Append code in an appendix.

## Key Principles

1. **Actor-Critic at every stage**: Generate, critique, revise. Never accept first drafts for analysis, modeling, or formulations.
2. **Iterative debugging**: Code rarely works on the first try. Budget for multiple attempts.
3. **DAG-ordered execution**: Solve subtasks in dependency order and pass results forward.
4. **Reuse over redo**: Downstream subtasks should reuse files and results from upstream.
5. **Plain-text reasoning**: When doing analysis and modeling, write coherent paragraphs, not bullet lists. This forces deeper thinking.
6. **Sanity before polish**: Check that numbers make sense before formatting the report.
