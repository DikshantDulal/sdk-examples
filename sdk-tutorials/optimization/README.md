# Optimization tutorials

**Learning path**

1. [haiqu_solve_qubo.ipynb](haiqu_solve_qubo.ipynb) — 20-qubit Max-Cut: `OptimizationProblem` → `build_lr_qaoa_circuit` → `run` → `postprocess`, with raw vs post-process metrics.
2. [haiqu_postprocess.ipynb](haiqu_postprocess.ipynb) — 120-qubit instance with frozen counts; LP → `OptimizationProblem` intake and `evaluate_problem_cost`.

**Migration:** Use `qiskit_addon_opt_mapper.problems.OptimizationProblem` (and `to_unconstrained_problem` when needed). The Haiqu `QUBO` class and `haiqu.solve_qubo()` remain as deprecated shortcuts only.

**Data in this folder:** `maxcut_graph_reference.json`, `graph_optimization_120q/seq_6434_c.lp`, `graph_optimization_120q/mps_counts_trained.json`.
