"""One-time offline helper: LP → polynomial_problem JSON for the postprocess tutorial.

Run from ``sdk-tutorials/optimization`` (or pass absolute paths). Requires
``qiskit-optimization`` for LP parsing only in this script; the notebook loads
``polynomial_problem_120q.json`` via ``deserialize_optimization_problem``.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo

from haiqu.sdk.optimization import from_hamiltonian, serialize_optimization_problem


def lp_to_polynomial_payload(lp_path: Path) -> dict:
    qp = QuadraticProgram()
    qp.read_from_lp_file(str(lp_path))
    qp = QuadraticProgramToQubo().convert(qp)
    hamiltonian, offset = qp.to_ising()
    op = from_hamiltonian(hamiltonian, offset=offset)
    return serialize_optimization_problem(op)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lp",
        type=Path,
        default=Path(__file__).resolve().parent / "seq_6434_c.lp",
        help="Source CPLEX LP file (default: seq_6434_c.lp next to this script)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).resolve().parent / "polynomial_problem_120q.json",
        help="Output polynomial_problem JSON path",
    )
    args = parser.parse_args()
    payload = lp_to_polynomial_payload(args.lp)
    args.out.write_text(json.dumps(payload, separators=(",", ":")))
    print(f"Wrote {args.out} ({args.out.stat().st_size} bytes, n_vars={payload['n_vars']})")


if __name__ == "__main__":
    main()
