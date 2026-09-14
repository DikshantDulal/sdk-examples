# Optimization tutorials

Learning path for combinatorial optimization with Haiqu SDK:

1. **[`haiqu_solve_qubo.ipynb`](haiqu_solve_qubo.ipynb)** — Max-Cut on a 20-node reference graph. Build an `OptimizationProblem` with **qiskit-addon-opt-mapper**, then `build_lr_qaoa_circuit` → `run` → `postprocess`.
2. **[`haiqu_postprocess.ipynb`](haiqu_postprocess.ipynb)** — Same post-processing API on **120-qubit** pre-baked counts and an LP instance (`graph_optimization_120q/`).

**Migration:** `haiqu.solve_qubo()` and `haiqu.sdk.optimization.QUBO` are deprecated. Prefer `qiskit_addon_opt_mapper.problems.OptimizationProblem` and the explicit circuit → run → postprocess pipeline. See [Haiqu problem formulations](https://docs.haiqu.ai/optimization/problem.html).

Data files in this folder (`maxcut_graph_reference.json`, `graph_optimization_120q/`) are unchanged from earlier tutorials.
