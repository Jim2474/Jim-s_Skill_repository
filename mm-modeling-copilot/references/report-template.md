# Modeling Report Template

## Markdown Report Template

Use this structure for `report.md`:

```markdown
# [Problem Title]

## Abstract

State the problem in 1-2 sentences. Describe the approach (model type and key methods).
Summarize the main results with specific numbers. State the conclusion.
Keep to one paragraph, 150-250 words.

## Problem Restatement

Restate the task in your own words. Do NOT copy from the source.
List the specific questions answered, numbered.

## Assumptions

| ID | Assumption | Rationale | Impact if Violated |
|---|---|---|---|

## Notation

| Symbol | Meaning | Unit | Type |
|---|---|---|---|
| | | | Decision / Parameter / Input / Output |

## Data Preparation

Describe:
- Data sources and format
- Cleaning steps and missing value handling
- Transformations and derived variables
- Summary statistics (table or text)
- Data quality issues noted

## Model Construction

### Subtask 1: [Title]

#### Problem Formulation
Define the model mathematically:
- Variables and parameters
- Objective function(s)
- Constraints
- Governing equations

#### Method Justification
Explain why this model fits the problem and what alternatives were considered.

### Subtask 2: [Title]
(Repeat structure for each subtask)

## Solution Method

For each subtask:
- Algorithm used and why
- Software and libraries
- Computation steps
- Convergence criteria or stopping conditions

## Results

### Subtask 1 Results
- Tables of key outputs
- Figures (reference as `![caption](figures/filename.png)`)
- Interpretation in the language of the original problem

### Subtask 2 Results
(Repeat)

### Overall Results
Synthesize across subtasks. Answer the original questions directly with specific values.

## Validation

For each subtask:
- Sanity checks performed
- Error metrics (for predictions)
- Constraint satisfaction (for optimization)
- Comparison with baselines or naive methods
- Cross-validation results (if applicable)

## Sensitivity Analysis

For each important parameter:
- Range tested
- Impact on results (table or figure)
- Classification: insensitive / moderate / highly sensitive
- Robustness conclusion

## Strengths and Weaknesses

### Strengths
- What the model captures well
- Innovative aspects

### Weaknesses
- Limitations and where the model breaks down
- What additional data or methods would improve it

## Conclusion

Answer the original questions directly. State the key takeaways.
Suggest directions for future improvement.

## References

List external sources, data sources, textbooks, and methods references.

## Appendix: Code and Reproducibility

### How to Reproduce
1. Install requirements: `pip install numpy pandas scipy scikit-learn matplotlib`
2. Place data files in `data/`
3. Run: `python src/task_1_solve.py` (etc.)
4. Outputs appear in `figures/` and `results/`

### File Listing
| File | Purpose |
|---|---|
| `src/load_data.py` | Data loading and preprocessing |
| ... | ... |
```

## LaTeX Paper Template (for Competitions)

When the user requests a LaTeX paper (MCM/ICM/CUMCM), generate `report.tex`:

```latex
\documentclass[CtoC]{mcmthesis}
% If mcmthesis is not available, use:
% \documentclass[12pt]{article}
% \usepackage{amsmath,amssymb,graphicx,booktabs,float,geometry,hyperref}
% \geometry{a4paper,margin=1in}

\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{float}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{xcolor}

\lstset{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red},
  breaklines=true,
  frame=single
}

\title{[Problem Title]}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
[One paragraph: problem, method, results, conclusion]
\end{abstract}

\tableofcontents
\newpage

\section{Problem Restatement}
[Restate in own words. List questions.]

\section{Model Assumptions}
\begin{table}[H]
\centering
\begin{tabular}{clll}
\toprule
ID & Assumption & Rationale & Impact \\
\midrule
A1 & ... & ... & ... \\
\bottomrule
\end{tabular}
\end{table}

\section{Notation}
\begin{table}[H]
\centering
\begin{tabular}{clcc}
\toprule
Symbol & Meaning & Unit & Type \\
\midrule
$x_i$ & ... & ... & Decision \\
\bottomrule
\end{tabular}
\end{table}

\section{Problem Analysis}
[Overall analysis: background, data description, approach overview]

\section{Model for Subtask 1: [Title]}
\subsection{Model Setup}
[Variables, objective, constraints, equations]
\subsection{Solution Method}
[Algorithm, implementation details]
\subsection{Results}
[Tables, figures, interpretation]

% Repeat \section for each subtask

\section{Sensitivity Analysis}
[Parameter variation, impact tables/figures, robustness discussion]

\section{Model Validation}
[Sanity checks, error metrics, comparison with baselines]

\section{Strengths and Weaknesses}
\subsection{Strengths}
\subsection{Weaknesses}

\section{Conclusions}
[Direct answers to original questions. Key takeaways.]

\begin{thebibliography}{99}
\bibitem{ref1} ...
\end{thebibliography}

\appendix
\section{Code}
\lstinputlisting[caption={Data Loading}]{src/load_data.py}
% Or paste code inline with \begin{lstlisting}...\end{lstlisting}

\end{document}
```

## Tips for High-Quality Reports

1. **Abstract first**: Write the abstract last but place it first. It should stand alone.
2. **Figures speak**: Every result should have at least one figure. Tables support precision, figures support intuition.
3. **Justify everything**: Model choice, parameter values, assumption — all need rationale.
4. **Quantify quality**: Use standard metrics (RMSE, R², constraint slack, optimality gap) not just "good" or "reasonable."
5. **Honest limitations**: Judges and reviewers respect honest discussion of weaknesses more than pretending there are none.
6. **Reproducibility**: A reader should be able to rerun your code and get the same results.
