
import sys
from pathlib import Path

import yaml


def validate_workload(workload):
    """Check whether RTO and RPO are defined."""
    errors = []

    recovery = workload.get("workload", {}).get("recovery", {})

    for field in ("rto", "rpo"):
        value = recovery.get(field)

        if value is None or not str(value).strip():
            errors.append(f"RL-LINUX-001: {field.upper()} is missing.")

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/resiliencelint.py <workload.yaml>")
        return 2

    try:
        with open(sys.argv[1], encoding="utf-8") as file:
            workload = yaml.safe_load(file) or {}
    except (OSError, yaml.YAMLError) as exc:
        print(f"ERROR: Cannot read YAML file: {exc}")
        return 2

    if not isinstance(workload, dict):
        print("ERROR: Workload configuration must be a YAML mapping.")
        return 2

    errors = validate_workload(workload)

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: RTO and RPO are defined.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
