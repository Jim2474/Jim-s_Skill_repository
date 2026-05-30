#!/usr/bin/env python3
"""Initialize a Claude Code mathematical modeling project folder.

Creates a structured project directory with template files for
problem analysis, modeling, computation, and reporting.
"""

from __future__ import annotations

import argparse
import datetime
from pathlib import Path


FILES = {
    "problem.md": (
        "# Problem Analysis\n\n"
        "## Background\n\n"
        "## Questions to Answer\n\n"
        "1. \n\n"
        "## Inputs and Data\n\n"
        "## Decision Variables\n\n"
        "## Parameters\n\n"
        "## Constraints\n\n"
        "## Objectives\n\n"
        "## Deliverables\n\n"
        "## Ambiguities and Assumptions Needed\n\n"
    ),
    "assumptions.md": (
        "# Assumptions\n\n"
        "| ID | Assumption | Rationale | Impact if Violated |\n"
        "|---|---|---|---|\n"
        "| A1 | | | |\n"
    ),
    "symbols.md": (
        "# Notation\n\n"
        "| Symbol | Meaning | Unit | Type |\n"
        "|---|---|---|---|\n"
        "| | | | Decision / Parameter / Input / Output |\n"
    ),
    "model_plan.md": (
        "# Model Plan\n\n"
        "## Problem Decomposition\n\n"
        "### Subtask 1: [Title]\n"
        "- Description: \n"
        "- Inputs: \n"
        "- Outputs: \n"
        "- Dependencies: none\n\n"
        "### Subtask 2: [Title]\n"
        "- Description: \n"
        "- Inputs: \n"
        "- Outputs: \n"
        "- Dependencies: Subtask 1\n\n"
        "## Dependency DAG\n\n"
        "```\n"
        "Subtask 1 → Subtask 2 → ...\n"
        "```\n\n"
        "## Candidate Models\n\n"
        "| Subtask | Candidate Methods | Selected | Rationale |\n"
        "|---|---|---|---|\n\n"
        "## Evaluation Metrics\n\n"
        "## Validation Plan\n\n"
        "## Sensitivity Analysis Plan\n\n"
    ),
    "report.md": (
        "# Modeling Report\n\n"
        "## Abstract\n\n"
        "## Problem Restatement\n\n"
        "## Assumptions\n\n"
        "## Notation\n\n"
        "## Data Preparation\n\n"
        "## Model Construction\n\n"
        "### Subtask 1\n\n"
        "## Solution Method\n\n"
        "## Results\n\n"
        "## Validation\n\n"
        "## Sensitivity Analysis\n\n"
        "## Strengths and Weaknesses\n\n"
        "## Conclusion\n\n"
        "## References\n\n"
        "## Appendix: Code and Reproducibility\n\n"
    ),
}

LATEX_REPORT = r"""\documentclass[12pt]{article}
\usepackage{amsmath,amssymb,graphicx,booktabs,float,geometry,hyperref,listings,xcolor}
\geometry{a4paper,margin=1in}

\lstset{
  language=Python,
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red},
  breaklines=true,
  frame=single
}

\title{Modeling Report}
\date{\today}

\begin{document}
\maketitle

\begin{abstract}
% Problem, method, key results, conclusion.
\end{abstract}

\tableofcontents
\newpage

\section{Problem Restatement}

\section{Model Assumptions}

\section{Notation}

\section{Problem Analysis}

\section{Model Construction}

\section{Solution Method}

\section{Results}

\section{Sensitivity Analysis}

\section{Model Validation}

\section{Strengths and Weaknesses}

\section{Conclusions}

\begin{thebibliography}{99}
\bibitem{ref1} Add references here.
\end{thebibliography}

\appendix
\section{Code and Reproducibility}

\end{document}
"""

SRC_FILES = {
    "src/load_data.py": (
        '"""Data loading and preprocessing."""\n\n'
        "import pandas as pd\n"
        "import numpy as np\n\n\n"
        "def load_data(path: str) -> pd.DataFrame:\n"
        '    """Load and clean data from the given path."""\n'
        "    # TODO: implement data loading\n"
        "    pass\n"
    ),
    "src/utils.py": (
        '"""Shared utility functions."""\n\n'
        "import numpy as np\n"
        "import random\n\n"
        "# Reproducibility\n"
        "SEED = 42\n"
        "np.random.seed(SEED)\n"
        "random.seed(SEED)\n"
    ),
    "src/plot_results.py": (
        '"""Result visualization."""\n\n'
        "import matplotlib.pyplot as plt\n"
        "import os\n\n"
        "FIGURES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'figures')\n"
        "os.makedirs(FIGURES_DIR, exist_ok=True)\n\n\n"
        "def save_fig(fig, name: str, dpi: int = 300):\n"
        '    """Save figure to figures/ directory."""\n'
        "    path = os.path.join(FIGURES_DIR, name)\n"
        "    fig.savefig(path, dpi=dpi, bbox_inches='tight')\n"
        "    plt.close(fig)\n"
        f"    print(f'Saved: {{path}}')\n"
    ),
    "src/sensitivity.py": (
        '"""Sensitivity analysis utilities."""\n\n'
        "import numpy as np\n"
        "import pandas as pd\n\n\n"
        "def sensitivity_sweep(model_fn, param_name: str, base_value: float,\n"
        "                      variations=(-0.2, -0.1, 0, 0.1, 0.2)):\n"
        '    """Run model with parameter varied by given fractions.\n\n'
        "    Args:\n"
        "        model_fn: callable(param_value) -> result_value\n"
        "        param_name: name for reporting\n"
        "        base_value: baseline parameter value\n"
        "        variations: fractional changes to test\n\n"
        "    Returns:\n"
        "        DataFrame with columns: variation, param_value, result\n"
        '    """\n'
        "    records = []\n"
        "    for v in variations:\n"
        "        val = base_value * (1 + v)\n"
        "        result = model_fn(val)\n"
        "        records.append({'variation': f'{v:+.0%}', 'param_value': val, 'result': result})\n"
        "    df = pd.DataFrame(records)\n"
        f"    print(f'Sensitivity of {{param_name}}:')\n"
        "    print(df.to_string(index=False))\n"
        "    return df\n"
    ),
}

DIRS = ["data", "src", "figures", "results"]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Initialize a mathematical modeling project directory."
    )
    parser.add_argument(
        "--output", default="mm_modeling_output",
        help="Output project directory (default: mm_modeling_output)"
    )
    parser.add_argument(
        "--name", default=None,
        help="Project name for the README (default: derived from output dir)"
    )
    parser.add_argument(
        "--latex", action="store_true",
        help="Also create report.tex with a LaTeX paper template"
    )
    args = parser.parse_args()

    root = Path(args.output).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    for dirname in DIRS:
        (root / dirname).mkdir(exist_ok=True)

    # Create template files (skip if they already exist)
    for filename, content in FILES.items():
        path = root / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    for filename, content in SRC_FILES.items():
        path = root / filename
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    if args.latex:
        tex_path = root / "report.tex"
        if not tex_path.exists():
            tex_path.write_text(LATEX_REPORT, encoding="utf-8")

    # Create .gitignore
    gitignore = root / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(
            "# Python\n"
            "__pycache__/\n"
            "*.pyc\n"
            ".venv/\n"
            "\n"
            "# OS\n"
            ".DS_Store\n"
            "Thumbs.db\n"
            "\n"
            "# IDE\n"
            ".idea/\n"
            ".vscode/\n",
            encoding="utf-8",
        )

    # Create README
    project_name = args.name or root.name
    readme = root / "README.md"
    if not readme.exists():
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        readme.write_text(
            f"# {project_name}\n\n"
            f"Mathematical modeling project initialized on {now}.\n\n"
            "## Structure\n\n"
            "```\n"
            "├── problem.md          # Problem analysis\n"
            "├── assumptions.md      # Assumptions with rationale\n"
            "├── symbols.md          # Notation table\n"
            "├── model_plan.md       # Decomposition + model selection\n"
            "├── data/               # Input data files\n"
            "├── src/                # Python scripts\n"
            "│   ├── load_data.py    # Data loading\n"
            "│   ├── utils.py        # Shared utilities\n"
            "│   ├── plot_results.py # Visualization\n"
            "│   └── sensitivity.py  # Sensitivity analysis\n"
            "├── figures/            # Generated plots\n"
            "├── results/            # Tables and metrics\n"
            "└── report.md           # Final report\n"
            "    report.tex          # Optional LaTeX report if initialized with --latex\n"
            "```\n\n"
            "## Reproduce\n\n"
            "```bash\n"
            "pip install numpy pandas scipy scikit-learn matplotlib statsmodels\n"
            "python src/load_data.py\n"
            "# Run task scripts in order\n"
            "```\n",
            encoding="utf-8",
        )

    print(root)


if __name__ == "__main__":
    main()
