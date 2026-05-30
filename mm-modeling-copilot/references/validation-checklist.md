# Validation and Evaluation Checklist

Before finalizing a modeling task, systematically check each dimension.

## Dimension 1: Problem Analysis and Understanding

### 1.1 Problem Definition
- [ ] Problem is restated in your own words, not copied from the source.
- [ ] All questions to answer are explicitly listed.
- [ ] Decision variables, parameters, and unknowns are identified.
- [ ] Constraints are listed and classified (hard vs. soft, equality vs. inequality).
- [ ] Objective functions or evaluation metrics are defined.
- [ ] Problem type is identified (optimization, prediction, evaluation, simulation, etc.).

### 1.2 Scope and Coverage
- [ ] All sub-questions in the problem are addressed.
- [ ] No question is left unanswered or deferred without explanation.
- [ ] The scope matches the problem requirements (not over-simplified, not over-extended).

## Dimension 2: Rigor and Rationality of Modeling

### 2.1 Assumptions
- [ ] Assumptions are numbered and listed explicitly.
- [ ] Each assumption has a rationale.
- [ ] Assumptions are defensible (not arbitrary).
- [ ] Assumptions simplify without destroying the problem.
- [ ] Impact of each assumption is discussed (what happens if it's wrong?).

### 2.2 Model Rationality
- [ ] Model family matches the problem type and data characteristics.
- [ ] Mathematical formulation is complete (variables, parameters, objective, constraints, equations).
- [ ] Model is solvable with available methods and tools.
- [ ] Model choice is justified against at least one alternative.
- [ ] Symbols are defined before use.
- [ ] Equations are dimensionally consistent.

## Dimension 3: Practicality and Scientificity

### 3.1 Computational Practicality
- [ ] Code runs successfully from the project root.
- [ ] All scripts have been executed, not just written.
- [ ] Figures are saved to `figures/` and are readable.
- [ ] Tables and metrics are saved to `results/`.
- [ ] Random seeds are set where randomness matters.
- [ ] Errors and warnings from code execution were inspected.
- [ ] Dependencies are documented or standard (numpy, pandas, scipy, sklearn, matplotlib).

### 3.2 Scientific Correctness
- [ ] Results have plausible numerical scale and units.
- [ ] Optimization results satisfy stated constraints.
- [ ] Prediction errors or residuals are reported with standard metrics (RMSE, MAE, R², MAPE).
- [ ] Cross-validation or train/test split was used for prediction tasks.
- [ ] Statistical tests include p-values or confidence intervals.
- [ ] Extreme-case and boundary behavior was checked.

## Dimension 4: Results and Sensitivity

### 4.1 Result Analysis
- [ ] Results directly answer the original questions.
- [ ] Results are interpreted in the language of the problem (not just numbers).
- [ ] Key findings are highlighted with specific values.
- [ ] Figures and tables are referenced in the text.
- [ ] Comparison with baseline or naive method is provided when applicable.

### 4.2 Sensitivity and Bias Analysis
- [ ] Sensitivity analysis was performed for at least the top 3 important parameters.
- [ ] Parameter variation ranges are reasonable and justified.
- [ ] Sensitivity results are presented in a table or figure.
- [ ] Robustness of conclusions under parameter changes is discussed.
- [ ] Known biases or limitations are disclosed honestly.
- [ ] Data quality issues that could affect results are noted.

## Dimension 5: Report Quality

### 5.1 Structure and Completeness
- [ ] Report follows the standard template (Abstract through Appendix).
- [ ] All sections are present and substantive (not just placeholders).
- [ ] Equations, tables, and figures appear where they support the text.
- [ ] The report is self-contained — a reader doesn't need external files.

### 5.2 Reproducibility
- [ ] Code is included or referenced in an appendix.
- [ ] Data sources are documented.
- [ ] Instructions for re-running the analysis are included.
- [ ] Output file locations are specified.
- [ ] Python version and key package versions are noted.

## Quick Self-Score

After checking all items, rate each dimension 1-10:

| Dimension | Score | Notes |
|---|---|---|
| 1. Problem Analysis | /10 | |
| 2. Modeling Rigor | /10 | |
| 3. Practicality | /10 | |
| 4. Results & Sensitivity | /10 | |
| 5. Report Quality | /10 | |
| **Total** | **/50** | |

A score below 35/50 suggests major issues. Address items with the lowest scores first.
