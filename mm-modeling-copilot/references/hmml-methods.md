# HMML Method Library

This hierarchical method library provides structured guidance for mathematical modeling method selection. For each method, the core idea and typical applications are given to help match problem characteristics to appropriate techniques.

---

## Operations Research

### Programming Theory

#### Linear Programming (LP)
- **Core Idea**: Optimize a linear objective subject to linear equality/inequality constraints. Feasible region is a convex polytope; optimal solution is at a vertex.
- **Applications**: Resource allocation, production planning, diet problems, transportation problems, blending and mixing.

#### Integer Programming (IP)
- **Core Idea**: LP where some or all decision variables are restricted to integers. Models indivisible quantities and logical decisions (yes/no).
- **Applications**: Facility location, crew scheduling, capital budgeting, bin packing, fixed-charge problems.

#### Mixed-Integer Programming (MIP)
- **Core Idea**: Combines continuous and integer variables in a single optimization model, enabling both quantity and structural decisions.
- **Applications**: Supply chain design, production lot-sizing, network design with fixed costs, workforce scheduling with shifts.

#### Goal Programming
- **Core Idea**: Handles multiple, often conflicting objectives by minimizing weighted deviations from pre-set target values for each goal.
- **Applications**: Multi-criteria budget allocation, project planning with quality/cost/time trade-offs, educational resource distribution.

#### Multi-Objective Programming
- **Core Idea**: Simultaneously optimizes multiple objectives; produces a Pareto front of non-dominated solutions rather than a single optimum.
- **Applications**: Engineering design trade-offs (weight vs. strength), portfolio optimization (return vs. risk), environmental–economic policy analysis.

#### Dynamic Programming (DP)
- **Core Idea**: Decomposes a sequential decision problem into overlapping sub-problems; solves each once and stores results (optimal substructure + memoization).
- **Applications**: Knapsack problems, shortest paths (Bellman-Ford), sequence alignment, inventory replenishment, optimal stopping.

#### Network Optimization
- **Core Idea**: Models problems on graph structures with nodes and arcs, exploiting network structure for efficient algorithms (e.g., network simplex).
- **Applications**: Transportation/transshipment, assignment problems, minimum-cost flow, logistics network design.

---

#### Convex Programming
- **Core Idea**: Minimizes a convex objective over a convex feasible set. Any local minimum is the global minimum, guaranteeing tractability.
- **Applications**: Portfolio optimization, signal processing, machine learning loss minimization, optimal power flow approximations.

#### Quadratic Programming (QP)
- **Core Idea**: Optimizes a quadratic objective subject to linear constraints. Efficiently solvable when the objective is convex (positive semi-definite Hessian).
- **Applications**: Markowitz portfolio optimization, SVM dual formulation, model predictive control, least-squares with constraints.

#### Nonlinear Programming (NLP)
- **Core Idea**: Optimizes a nonlinear objective and/or nonlinear constraints. May have multiple local optima; requires gradient-based or global solvers.
- **Applications**: Chemical process design, structural engineering, curve fitting with nonlinear models, power systems dispatch.

#### Semidefinite Programming (SDP)
- **Core Idea**: Optimizes a linear objective over the cone of positive semidefinite matrices. Generalizes LP and QP; solvable in polynomial time via interior-point methods.
- **Applications**: Relaxations of combinatorial problems (Max-Cut), robust control, sensor network localization, quantum information bounds.

#### Penalty Methods
- **Core Idea**: Converts a constrained problem into a sequence of unconstrained problems by adding penalty terms for constraint violations.
- **Applications**: General-purpose NLP solving, engineering optimization with complex constraints, augmented Lagrangian methods for large-scale problems.

---

#### Fuzzy Optimization
- **Core Idea**: Handles imprecise or vague parameters by representing them as fuzzy numbers or fuzzy sets, then optimizing over membership degrees.
- **Applications**: Decision-making under linguistic uncertainty, fuzzy transportation, supplier selection with qualitative criteria.

#### Stochastic Optimization
- **Core Idea**: Optimizes expected performance (or risk measures) when some parameters are random variables with known or estimated distributions.
- **Applications**: Two-stage planning under demand uncertainty, stochastic inventory, financial hedging, energy scheduling with renewable variability.

#### Robust Optimization
- **Core Idea**: Finds solutions that remain feasible and near-optimal for all realizations within an uncertainty set, without requiring probability distributions.
- **Applications**: Portfolio immunization, supply chain design under demand ambiguity, telecommunications network design, worst-case engineering design.

#### Cooperative Game Theory
- **Core Idea**: Studies how rational players form coalitions and fairly distribute collective payoffs (Shapley value, core, nucleolus).
- **Applications**: Cost/profit sharing in logistics alliances, airport runway fees, collaborative procurement, voting power analysis.

#### Simulated Annealing (SA)
- **Core Idea**: Metaheuristic inspired by metallurgical annealing; accepts worse solutions with decreasing probability to escape local optima.
- **Applications**: VLSI circuit layout, TSP, job-shop scheduling, image reconstruction, any combinatorial optimization with complex landscapes.

#### Genetic Algorithm (GA)
- **Core Idea**: Population-based search using selection, crossover, and mutation operators inspired by biological evolution.
- **Applications**: Scheduling, vehicle routing, neural network architecture search, multi-objective optimization (NSGA-II), feature selection.

#### Particle Swarm Optimization (PSO)
- **Core Idea**: Swarm of candidate solutions moves through the search space guided by personal and global best positions found so far.
- **Applications**: Neural network training, antenna design, power system optimization, continuous parameter tuning, function optimization.

#### Ant Colony Optimization (ACO)
- **Core Idea**: Artificial ants deposit pheromones on solution components; iteratively reinforcing good components converges toward strong solutions.
- **Applications**: TSP, vehicle routing, network routing, job-shop scheduling, feature selection on graphs.

---

### Graph Theory

#### Shortest Path — Dijkstra's Algorithm
- **Core Idea**: Greedy BFS on a graph with non-negative edge weights; maintains a priority queue of tentative distances from the source.
- **Applications**: Road navigation (GPS), network routing (OSPF), robot motion planning on grids, single-source logistics.

#### Shortest Path — A* Algorithm
- **Core Idea**: Extends Dijkstra with an admissible heuristic to guide search toward the goal, dramatically reducing explored nodes.
- **Applications**: Game pathfinding, robotic navigation, route planning with geographic heuristics.

#### Shortest Path — Bellman-Ford Algorithm
- **Core Idea**: Relaxes all edges V−1 times; handles negative edge weights and can detect negative cycles.
- **Applications**: Currency arbitrage detection, network routing with variable costs, shortest paths in graphs with penalties.

#### Travelling Salesman Problem (TSP)
- **Core Idea**: Find the minimum-cost Hamiltonian cycle visiting all cities exactly once. NP-hard; solved via exact (branch-and-cut) or heuristic methods.
- **Applications**: Delivery route optimization, PCB drilling, telescope scheduling, genome sequencing (shortest superstring).

#### Vehicle Routing Problem (VRP)
- **Core Idea**: Generalization of TSP with multiple vehicles, capacity constraints, and time windows. Solved via branch-and-price or metaheuristics.
- **Applications**: Last-mile delivery, waste collection, school bus routing, field service scheduling.

#### Path Planning
- **Core Idea**: Find a collision-free path from start to goal in a continuous or discretized space, often under kinematic constraints.
- **Applications**: Autonomous vehicle navigation, drone flight planning, warehouse robot movement, surgical robot arm trajectories.

---

#### Minimum Spanning Tree — Prim's Algorithm
- **Core Idea**: Greedily grows the MST from a starting vertex by always adding the cheapest edge connecting the tree to a non-tree vertex.
- **Applications**: Network cable layout, cluster analysis (single-linkage), approximation algorithms for Steiner tree, image segmentation.

#### Minimum Spanning Tree — Kruskal's Algorithm
- **Core Idea**: Sorts all edges by weight and adds them if they don't form a cycle (union-find); produces the MST for the entire graph.
- **Applications**: Same as Prim's; preferred when edge list is available and graph is sparse.

#### Steiner Tree
- **Core Idea**: Find the minimum-weight tree spanning a required subset of vertices (terminals), optionally using additional Steiner vertices. NP-hard in general.
- **Applications**: VLSI interconnect design, telecommunications network design, pipeline layout, phylogenetic tree reconstruction.

---

#### Max-Flow — Ford-Fulkerson Method
- **Core Idea**: Iteratively finds augmenting paths from source to sink in the residual graph; flow increases until no path exists.
- **Applications**: Network bandwidth allocation, bipartite matching (via reduction), project selection, image segmentation (graph cuts).

#### Max-Flow — Edmonds-Karp Algorithm
- **Core Idea**: Implements Ford-Fulkerson using BFS to find shortest augmenting paths, guaranteeing O(VE²) time complexity.
- **Applications**: Same as Ford-Fulkerson; preferred for guaranteed polynomial runtime on dense graphs.

#### Min-Cost Flow
- **Core Idea**: Finds the minimum-cost way to send a required amount of flow through a capacitated network with per-unit edge costs.
- **Applications**: Transportation with shipping costs, assignment problems, optimal matching, supply chain distribution.

#### Multi-Commodity Flow
- **Core Idea**: Routes multiple commodities (each with its own source-sink pair) simultaneously through a shared-capacity network.
- **Applications**: Telecommunications bandwidth allocation, airline fleet routing, freight logistics with multiple product types.

---

#### Bipartite Matching
- **Core Idea**: Finds a maximum or optimal-weight matching between two disjoint vertex sets. Solvable in polynomial time (Hungarian algorithm, Hopcroft-Karp).
- **Applications**: Job-worker assignment, student-school matching, organ donor matching, resource-task pairing.

#### Graph Coloring
- **Core Idea**: Assigns colors to vertices such that no two adjacent vertices share a color; minimizing colors used is NP-hard.
- **Applications**: Exam timetabling, register allocation in compilers, frequency assignment in wireless networks, map coloring.

#### Vertex Cover / Set Cover
- **Core Idea**: Find the smallest set of vertices (or sets) that covers all edges (or elements). NP-hard; greedy gives logarithmic approximation for set cover.
- **Applications**: Sensor placement, network monitoring, facility siting for coverage, minimal test suite selection.

#### Spectral Graph Theory
- **Core Idea**: Analyzes graph properties via eigenvalues and eigenvectors of adjacency or Laplacian matrices. Algebraic connectivity, clustering, and embedding.
- **Applications**: Community detection (spectral clustering), graph partitioning, network robustness analysis, dimensionality reduction on graphs.

---

### Stochastic Processes and Probabilistic Models

#### Markov Chains
- **Core Idea**: Memoryless stochastic process where the next state depends only on the current state (transition matrix). Steady-state analysis via eigenvectors.
- **Applications**: PageRank, weather modeling, customer behavior (churn prediction), text generation, population genetics.

#### Markov Decision Processes (MDP)
- **Core Idea**: Sequential decision-making framework combining Markov chains with actions and rewards. Solved via value iteration or policy iteration.
- **Applications**: Robot navigation, inventory management, treatment planning, game AI, dynamic pricing.

#### Queuing Theory — M/M/1
- **Core Idea**: Single-server queue with Poisson arrivals and exponential service. Closed-form expressions for waiting time, queue length, and utilization (ρ = λ/μ).
- **Applications**: Call center staffing, bank teller planning, simple service system capacity analysis.

#### Queuing Theory — M/G/1
- **Core Idea**: Single-server queue with Poisson arrivals and general service distribution. Pollaczek-Khinchine formula relates mean waiting time to service variance.
- **Applications**: Computer job scheduling, manufacturing workstations, healthcare patient flow with variable procedure times.

#### Inventory Theory — EOQ
- **Core Idea**: Economic Order Quantity balances fixed ordering cost against holding cost to find the optimal order size: Q* = √(2DS/H).
- **Applications**: Warehouse replenishment, retail stock management, raw material procurement planning.

#### Inventory Theory — Newsvendor Model
- **Core Idea**: Single-period stochastic inventory: order quantity balances overage cost (unsold) vs. underage cost (lost sales). Optimal quantile of demand distribution.
- **Applications**: Fashion retail, perishable goods, seasonal products, event ticket pricing, capacity reservation.

#### Monte Carlo Simulation
- **Core Idea**: Uses repeated random sampling to estimate quantities that are difficult to compute analytically (integrals, expectations, tail probabilities).
- **Applications**: Option pricing, risk analysis, reliability estimation, Bayesian posterior approximation, combinatorial counting.

#### Reliability Theory
- **Core Idea**: Analyzes system failure probability using component reliability, redundancy structures (series/parallel), and lifetime distributions (exponential, Weibull).
- **Applications**: Infrastructure maintenance planning, product warranty analysis, power grid reliability, aerospace system design.

#### Decision Trees (OR context)
- **Core Idea**: Graphical tool for sequential decisions under uncertainty; uses expected monetary value (EMV) or expected utility to choose optimal branches.
- **Applications**: R&D project selection, medical treatment decisions, oil exploration (drill/don't drill), investment staging.

---

## Machine Learning

### Supervised Learning

#### Linear Regression
- **Core Idea**: Models the relationship between features and a continuous target as a linear function; parameters estimated by minimizing sum of squared residuals (OLS).
- **Applications**: Price prediction, trend analysis, causal effect estimation (with careful design), baseline forecasting.

#### Logistic Regression
- **Core Idea**: Models probability of a binary outcome via the logistic (sigmoid) function applied to a linear combination of features. Trained by maximum likelihood.
- **Applications**: Credit scoring, disease diagnosis, customer churn prediction, spam detection, any binary classification baseline.

#### Decision Trees (ML)
- **Core Idea**: Recursively partitions feature space using axis-aligned splits that maximize information gain or minimize impurity (Gini/entropy).
- **Applications**: Interpretable classification/regression, feature importance analysis, rule extraction, medical diagnosis support.

#### Random Forest
- **Core Idea**: Ensemble of decorrelated decision trees trained on bootstrap samples with random feature subsets; predictions averaged (regression) or majority-voted (classification).
- **Applications**: Tabular data classification/regression, feature importance ranking, missing data imputation, anomaly detection.

#### Gradient Boosting — XGBoost
- **Core Idea**: Sequentially adds trees that correct residual errors of the ensemble; uses regularized objective, histogram-based splits, and efficient parallelization.
- **Applications**: Kaggle-winning tabular predictions, click-through rate, fraud detection, ranking, any structured data competition.

#### Gradient Boosting — LightGBM
- **Core Idea**: Gradient boosting with leaf-wise tree growth and gradient-based one-side sampling (GOSS) for speed on large datasets.
- **Applications**: Same as XGBoost; preferred for very large datasets, categorical feature handling, fast training iterations.

#### Support Vector Machine (SVM)
- **Core Idea**: Finds the maximum-margin hyperplane separating classes; kernel trick maps data to high-dimensional space for nonlinear boundaries.
- **Applications**: Text classification, image recognition, bioinformatics (gene expression), small-to-medium dataset classification with clear margins.

#### k-Nearest Neighbors (k-NN)
- **Core Idea**: Classifies (or regresses) a point by majority vote (or average) of its k closest neighbors in feature space. Non-parametric; no training phase.
- **Applications**: Recommendation systems, pattern recognition, imputation, anomaly detection (distance-based), baseline classifier.

#### Naive Bayes
- **Core Idea**: Applies Bayes' theorem with the (naive) assumption that features are conditionally independent given the class. Fast and effective for high-dimensional sparse data.
- **Applications**: Text classification (spam, sentiment), document categorization, real-time prediction, medical diagnosis screening.

#### Neural Networks — MLP
- **Core Idea**: Multi-layer perceptron: fully connected layers with nonlinear activations, trained by backpropagation. Universal function approximator.
- **Applications**: Tabular data regression/classification, function approximation, control systems, surrogate modeling.

#### Neural Networks — CNN
- **Core Idea**: Convolutional layers extract local spatial features via learned filters; pooling layers provide translation invariance. Hierarchical feature learning.
- **Applications**: Image classification, object detection, medical imaging, satellite imagery analysis, time series as images.

#### Neural Networks — RNN/LSTM
- **Core Idea**: Recurrent architecture processes sequential data; LSTM adds gating mechanisms to capture long-range dependencies and mitigate vanishing gradients.
- **Applications**: Time series forecasting, natural language processing, speech recognition, sequence-to-sequence translation, music generation.

---

### Unsupervised Learning

#### k-Means Clustering
- **Core Idea**: Partitions n observations into k clusters by iteratively assigning points to the nearest centroid and updating centroids. Minimizes within-cluster sum of squares.
- **Applications**: Customer segmentation, image compression (color quantization), document clustering, spatial data grouping.

#### DBSCAN
- **Core Idea**: Density-based clustering that groups points in dense regions and marks low-density points as noise. No need to specify k; finds arbitrarily shaped clusters.
- **Applications**: Geospatial clustering, anomaly/outlier detection, network intrusion detection, any data with noise and non-globular clusters.

#### Hierarchical Clustering
- **Core Idea**: Builds a tree (dendrogram) of nested clusters via agglomerative (bottom-up) or divisive (top-down) merging based on linkage criteria.
- **Applications**: Taxonomy construction, gene expression analysis, document organization, exploratory data analysis with unknown k.

#### Gaussian Mixture Model (GMM)
- **Core Idea**: Models data as a mixture of K Gaussian distributions; parameters estimated via EM algorithm. Provides soft (probabilistic) cluster assignments.
- **Applications**: Speaker recognition, image segmentation, density estimation, anomaly detection via low-likelihood thresholding.

#### PCA (as unsupervised)
- **Core Idea**: Projects data onto orthogonal directions of maximum variance (principal components). Linear dimensionality reduction preserving global structure.
- **Applications**: Data visualization, noise reduction, feature extraction, multicollinearity removal before regression, compression.

#### t-SNE
- **Core Idea**: Nonlinear dimensionality reduction that preserves local neighborhood structure by minimizing KL divergence between high-dimensional and low-dimensional probability distributions.
- **Applications**: Visualization of high-dimensional data (embeddings, gene expression), cluster exploration, quality assessment of learned representations.

#### UMAP
- **Core Idea**: Manifold learning technique using topological data analysis concepts; faster than t-SNE and better preserves global structure.
- **Applications**: Same as t-SNE but scales better; interactive visualization, preprocessing for clustering, exploring large datasets.

#### Autoencoders
- **Core Idea**: Neural network trained to reconstruct its input through a bottleneck; the bottleneck layer learns a compressed representation.
- **Applications**: Dimensionality reduction, denoising, anomaly detection (high reconstruction error = anomaly), generative modeling (VAE).

#### Anomaly Detection — Isolation Forest
- **Core Idea**: Isolates anomalies by random recursive partitioning; anomalies require fewer splits to isolate, yielding shorter average path lengths.
- **Applications**: Fraud detection, network intrusion, manufacturing defect detection, sensor fault identification.

---

### Ensemble Methods

#### Bagging (Bootstrap Aggregating)
- **Core Idea**: Trains multiple models on bootstrap samples of the data and averages predictions; reduces variance without increasing bias.
- **Applications**: Random Forest is the canonical example; stabilizing unstable learners, reducing overfitting in noisy datasets.

#### Boosting
- **Core Idea**: Sequentially trains weak learners, each focusing on errors of the previous ensemble; combines them with weighted votes. Reduces bias.
- **Applications**: AdaBoost for classification, gradient boosting for regression/classification, ranking tasks, imbalanced data handling.

#### Stacking
- **Core Idea**: Trains a meta-learner on the out-of-fold predictions of diverse base models; learns optimal combination weights automatically.
- **Applications**: Competition ensembles, combining heterogeneous models (tree + linear + NN), maximizing predictive performance.

#### Voting
- **Core Idea**: Combines predictions of multiple models by majority vote (classification) or averaging (regression). Simple but effective when base models are diverse.
- **Applications**: Quick ensemble baselines, combining models with different strengths, robust predictions with minimal tuning.

---

## Prediction and Time Series

### Statistical Methods

#### ARIMA / SARIMA
- **Core Idea**: Auto-Regressive Integrated Moving Average models linear temporal dependencies after differencing for stationarity. SARIMA adds seasonal differencing and seasonal AR/MA terms.
- **Applications**: Economic forecasting, demand forecasting, stock index trends, energy consumption, any univariate time series with trend and seasonality.

#### Exponential Smoothing (Holt-Winters)
- **Core Idea**: Weighted averages of past observations with exponentially decaying weights. Holt adds trend; Winters adds seasonality (additive or multiplicative).
- **Applications**: Short-term sales forecasting, inventory demand, production planning, simple and interpretable baseline forecasts.

#### Vector Autoregression (VAR)
- **Core Idea**: Multivariate time series model where each variable is a linear function of its own lags and lags of all other variables.
- **Applications**: Macroeconomic modeling (GDP, inflation, interest rates), Granger causality testing, impulse response analysis, multi-sensor systems.

#### GARCH
- **Core Idea**: Generalized Autoregressive Conditional Heteroskedasticity models time-varying volatility; variance depends on past squared residuals and past variances.
- **Applications**: Financial risk management (VaR), option pricing, volatility forecasting, portfolio risk estimation.

#### Kalman Filter
- **Core Idea**: Recursive Bayesian estimator for linear dynamic systems with Gaussian noise; optimally fuses noisy measurements with a state-space model.
- **Applications**: GPS tracking, robot localization, signal denoising, economic state estimation, sensor fusion.

---

### Regression Methods

#### Polynomial Regression
- **Core Idea**: Extends linear regression by adding polynomial terms (x², x³, …) of features; captures nonlinear relationships while remaining linear in parameters.
- **Applications**: Growth curve fitting, dose-response modeling, engineering stress-strain curves, simple nonlinear trend capture.

#### Ridge Regression (L2)
- **Core Idea**: Linear regression with L2 penalty on coefficients (λ∑β²); shrinks coefficients toward zero, reducing variance and handling multicollinearity.
- **Applications**: High-dimensional regression, multicollinear predictors, regularized forecasting, gene expression analysis.

#### Lasso Regression (L1)
- **Core Idea**: Linear regression with L1 penalty (λ∑|β|); produces sparse solutions by driving some coefficients exactly to zero (automatic feature selection).
- **Applications**: Feature selection, high-dimensional sparse regression, interpretable models, compressed sensing.

#### Elastic Net
- **Core Idea**: Combines L1 and L2 penalties (α controls mix); inherits Lasso's sparsity and Ridge's handling of correlated features.
- **Applications**: Genomics (many correlated predictors), text regression, situations where both feature selection and grouping are needed.

#### Quantile Regression
- **Core Idea**: Estimates conditional quantiles (e.g., median, 90th percentile) rather than the conditional mean; robust to outliers, captures distributional information.
- **Applications**: Risk analysis (VaR), income distribution modeling, environmental extremes, prediction intervals, heterogeneous effect estimation.

#### Generalized Additive Model (GAM)
- **Core Idea**: Extends linear models by replacing linear terms with smooth nonlinear functions (splines) of each predictor; additive structure retains interpretability.
- **Applications**: Ecological modeling, epidemiology (dose-response), interpretable nonlinear regression, time series trend decomposition.

---

### ML-Based Forecasting

#### Prophet
- **Core Idea**: Decomposable time series model (trend + seasonality + holidays) using piecewise linear or logistic growth; robust to missing data and outliers.
- **Applications**: Business metric forecasting (daily active users, revenue), capacity planning, forecasting with known events/holidays.

#### Random Forest Regression (for time series)
- **Core Idea**: Uses lagged features, rolling statistics, and calendar features as inputs to a random forest; captures nonlinear patterns without stationarity assumptions.
- **Applications**: Energy load forecasting, retail demand, sensor data prediction, when feature engineering can encode temporal structure.

#### Gradient Boosting Regression (for time series)
- **Core Idea**: Same feature-engineering approach as RF but with sequential boosting; typically achieves higher accuracy on structured time series features.
- **Applications**: Competition-grade time series forecasting, multi-step prediction with rich exogenous features, demand forecasting.

#### LSTM for Time Series
- **Core Idea**: Recurrent neural network with memory cells that learn long-range temporal dependencies directly from raw sequences without manual feature engineering.
- **Applications**: Multi-step-ahead forecasting, multivariate time series, anomaly detection in sequences, complex nonlinear temporal patterns.

---

## Evaluation and Ranking

### Weighting Methods

#### Analytic Hierarchy Process (AHP)
- **Core Idea**: Structures criteria hierarchically; pairwise comparison matrices yield priority weights via principal eigenvector. Consistency ratio checks logical coherence.
- **Applications**: Supplier selection, project prioritization, site selection, technology assessment, any multi-criteria decision with expert judgment.

#### Entropy Weight Method
- **Core Idea**: Derives objective weights from data dispersion: indicators with more variation (higher entropy contrast) receive higher weight. Purely data-driven.
- **Applications**: Objective weighting in TOPSIS/VIKOR, regional development evaluation, environmental quality assessment, when subjective weights are undesirable.

#### Coefficient of Variation Method
- **Core Idea**: Weights indicators proportionally to their coefficient of variation (σ/μ); indicators with greater relative dispersion are deemed more discriminating.
- **Applications**: Similar to entropy weight; simple alternative when data is positive-valued, performance benchmarking, index construction.

---

### Comprehensive Evaluation

#### TOPSIS
- **Core Idea**: Ranks alternatives by relative closeness to an ideal solution and distance from a negative-ideal solution in normalized weighted space.
- **Applications**: Supplier ranking, city livability ranking, project selection, water quality assessment, any multi-criteria ranking task.

#### VIKOR
- **Core Idea**: Compromise ranking method that maximizes group utility and minimizes individual regret; provides a compromise solution acceptable to all criteria.
- **Applications**: Similar to TOPSIS; preferred when a compromise between majority rule and minimum individual dissatisfaction is needed.

#### Grey Relational Analysis (GRA)
- **Core Idea**: Measures similarity between each alternative's indicator sequence and the ideal sequence using grey relational coefficients. Handles small samples and poor information.
- **Applications**: Manufacturing process optimization, material selection, performance evaluation with limited or uncertain data.

#### Fuzzy Comprehensive Evaluation
- **Core Idea**: Maps qualitative or imprecise evaluations to membership degrees in fuzzy sets, then aggregates them via fuzzy operators to produce an overall score.
- **Applications**: Risk assessment, teaching quality evaluation, environmental impact assessment, product quality evaluation with linguistic ratings.

#### Data Envelopment Analysis (DEA)
- **Core Idea**: Non-parametric LP-based method measuring relative efficiency of decision-making units (DMUs) with multiple inputs and outputs. No need for a functional form.
- **Applications**: Hospital efficiency, school performance, bank branch productivity, utility benchmarking, government program evaluation.

#### PROMETHEE
- **Core Idea**: Outranking method using pairwise comparisons of alternatives on each criterion with preference functions; produces partial (I) and complete (II) rankings.
- **Applications**: Environmental management, energy planning, logistics provider selection, R&D project ranking.

#### ELECTRE
- **Core Idea**: Outranking method using concordance and discordance indices to determine whether one alternative outranks another; handles incomparability.
- **Applications**: Large-scale public project evaluation, environmental policy comparison, military system selection, when strict compensation between criteria is undesirable.

---

### Dimensionality Reduction for Evaluation

#### PCA (for evaluation)
- **Core Idea**: Reduces correlated indicators to a smaller set of uncorrelated principal components while retaining most variance; component loadings aid interpretation.
- **Applications**: Constructing composite indices, removing redundant indicators before scoring, socioeconomic development indices, competitiveness rankings.

#### Factor Analysis
- **Core Idea**: Identifies latent factors underlying observed variables via a statistical model (common factor model); rotated loadings improve interpretability.
- **Applications**: Questionnaire validation, psychological constructs, economic composite indicators, identifying underlying dimensions of performance.

---

## Simulation

### Stochastic Simulation

#### Monte Carlo Simulation
- **Core Idea**: Generates large numbers of random scenarios to estimate distributions of outcomes; especially powerful when analytical solutions are intractable.
- **Applications**: Financial risk (VaR, CVaR), project cost/schedule risk, reliability estimation, Bayesian computation, option pricing.

#### Agent-Based Modeling (ABM)
- **Core Idea**: Simulates autonomous agents with defined rules interacting in an environment; emergent macro-behavior arises from micro-level interactions.
- **Applications**: Epidemic spread, traffic simulation, market dynamics, urban growth, social network evolution, ecological modeling.

#### Discrete-Event Simulation (DES)
- **Core Idea**: Models systems as sequences of events that change state at discrete points in time; tracks entities flowing through queues and servers.
- **Applications**: Manufacturing line optimization, hospital patient flow, call center staffing, airport operations, logistics hub throughput.

---

### System Dynamics

#### Stock-Flow Diagrams
- **Core Idea**: Models accumulations (stocks) and rates of change (flows) with feedback loops; continuous-time simulation of system behavior over time.
- **Applications**: Population growth, business growth modeling, resource depletion, policy analysis for long-term planning.

#### Causal Loop Diagrams
- **Core Idea**: Qualitative tool mapping feedback loops (reinforcing and balancing) among variables; identifies systemic leverage points before quantitative modeling.
- **Applications**: Problem structuring, stakeholder communication, policy debate, identifying unintended consequences, systems thinking education.

#### Compartmental Models (SIR/SEIR)
- **Core Idea**: Divides a population into compartments (Susceptible, Infected, Recovered, etc.) with flow rates governed by differential equations.
- **Applications**: Epidemic forecasting (COVID-19, influenza), vaccination strategy evaluation, disease intervention planning, endemic equilibrium analysis.

---

### Differential Equations

#### ODE — Euler's Method
- **Core Idea**: Simplest numerical ODE integrator: steps forward using the tangent line approximation y_{n+1} = y_n + h·f(t_n, y_n). First-order accurate.
- **Applications**: Educational demonstrations, quick prototyping of dynamic models, systems where high accuracy isn't critical.

#### ODE — Runge-Kutta Methods (RK4)
- **Core Idea**: Fourth-order method evaluating the derivative at four points per step for high accuracy; the workhorse of ODE numerical integration.
- **Applications**: Orbital mechanics, chemical kinetics, population dynamics, control system simulation, any smooth ODE system.

#### PDE — Finite Difference Method (FDM)
- **Core Idea**: Approximates partial derivatives with difference quotients on a regular grid; straightforward to implement for simple geometries.
- **Applications**: Heat conduction, wave propagation, diffusion processes, option pricing (Black-Scholes PDE), groundwater flow.

#### PDE — Finite Element Method (FEM)
- **Core Idea**: Divides the domain into small elements with piecewise polynomial basis functions; handles complex geometries and boundary conditions via variational formulation.
- **Applications**: Structural stress analysis, fluid dynamics, electromagnetic field simulation, geotechnical engineering, biomechanics.

#### Lotka-Volterra (Predator-Prey) Model
- **Core Idea**: Coupled nonlinear ODEs modeling predator-prey population dynamics with oscillatory solutions: prey grows exponentially, predator depends on prey abundance.
- **Applications**: Ecological modeling, biological population management, fisheries management, competitive market dynamics (by analogy).

#### Epidemic Models (SIR/SEIR as ODEs)
- **Core Idea**: ODE-based compartmental models with parameters β (transmission rate) and γ (recovery rate); basic reproduction number R₀ = β/γ determines outbreak threshold.
- **Applications**: Epidemic forecasting, herd immunity threshold calculation, intervention timing (lockdowns, vaccination), public health policy simulation.

#### Control Systems (ODE-based)
- **Core Idea**: Models plant dynamics as ODEs with feedback controllers (PID, LQR); analyzes stability, transient response, and steady-state error.
- **Applications**: Autonomous vehicles, industrial process control, robotics, HVAC systems, flight control, any regulated dynamic system.

---

## Statistical Analysis

### Hypothesis Testing

#### t-Test
- **Core Idea**: Tests whether the mean of one group (or difference between two groups) is significantly different from a hypothesized value, assuming approximately normal data.
- **Applications**: A/B testing, before-after treatment comparison, comparing experimental vs. control group means, quality control.

#### Chi-Square Test
- **Core Idea**: Tests association between categorical variables (independence test) or goodness-of-fit of observed frequencies to expected frequencies.
- **Applications**: Survey analysis, genetics (Hardy-Weinberg), market research (preference distributions), contingency table analysis.

#### ANOVA (Analysis of Variance)
- **Core Idea**: Tests whether means of three or more groups differ significantly by comparing between-group variance to within-group variance (F-test).
- **Applications**: Comparing treatments in experiments, product variant performance, educational method comparison, multi-factor experimental design.

#### Mann-Whitney U Test
- **Core Idea**: Non-parametric test comparing two independent groups' distributions via rank sums; no normality assumption required.
- **Applications**: Small sample comparisons, ordinal data, highly skewed data, when t-test assumptions are violated.

#### Kruskal-Wallis Test
- **Core Idea**: Non-parametric extension of one-way ANOVA; compares distributions of three or more independent groups using ranks.
- **Applications**: Same scenarios as ANOVA when normality cannot be assumed; ordinal response data, environmental monitoring comparisons.

---

### Statistical Inference

#### Maximum Likelihood Estimation (MLE)
- **Core Idea**: Finds parameter values that maximize the probability (likelihood) of observing the given data. Asymptotically efficient and normally distributed.
- **Applications**: Distribution fitting, regression parameter estimation, survival analysis, any parametric model calibration.

#### Bayesian Estimation
- **Core Idea**: Updates prior beliefs about parameters with observed data via Bayes' theorem to produce a posterior distribution. Incorporates domain knowledge.
- **Applications**: Small-sample inference, hierarchical models, clinical trials with prior studies, adaptive experimentation, uncertainty quantification.

#### Bootstrap
- **Core Idea**: Resamples observed data with replacement to empirically estimate the sampling distribution of a statistic; requires no distributional assumptions.
- **Applications**: Confidence intervals for complex statistics, standard error estimation, model validation, small-sample inference.

#### Confidence Intervals
- **Core Idea**: An interval estimate providing a range of plausible values for a parameter at a specified confidence level (e.g., 95%).
- **Applications**: Reporting uncertainty in any estimate, regulatory compliance (margin of error), sample size determination, meta-analysis.

---

### Correlation and Association

#### Pearson Correlation
- **Core Idea**: Measures the linear association between two continuous variables; ranges from −1 (perfect negative) to +1 (perfect positive).
- **Applications**: Exploratory data analysis, feature selection, collinearity diagnosis, initial relationship screening.

#### Spearman Rank Correlation
- **Core Idea**: Non-parametric measure of monotonic association using ranks; robust to outliers and does not require linearity.
- **Applications**: Ordinal data association, robustness check for Pearson, comparing rankings (judges, algorithms), ecological data.

#### Partial Correlation
- **Core Idea**: Measures association between two variables after removing the linear effect of one or more confounders.
- **Applications**: Identifying direct relationships in multivariate data, controlling for confounders, network inference (partial correlation networks).

#### Granger Causality
- **Core Idea**: Tests whether past values of one time series help predict another beyond its own past values (predictive causality, not true causation).
- **Applications**: Econometric analysis (do interest rates Granger-cause GDP?), neuroscience (brain region interactions), energy market analysis.
