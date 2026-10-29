
# ResilienceLint

<p align="center">
  <strong>Define recovery requirements. Validate consistently. Improve readiness.</strong>
</p>

<p align="center">
  A lightweight Python tool for validating infrastructure recovery requirements.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Tests-7%20passing-brightgreen" alt="7 tests passing">
  <img src="https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white" alt="GitHub Actions">
  <img src="https://img.shields.io/badge/License-Apache--2.0-blue" alt="Apache 2.0">
  <img src="https://img.shields.io/badge/Status-Early%20development-orange" alt="Early development">
</p>

---

## About the project

Infrastructure resilience starts with clearly defined recovery requirements.

ResilienceLint is a lightweight, read-only validation tool that checks whether Recovery Time Objective (RTO) and Recovery Point Objective (RPO) values are defined in YAML workload configurations.

The goal is simple: help infrastructure teams identify missing recovery requirements early and improve the consistency of disaster recovery documentation.

## About the author

Hi, I'm **Neggazizaggen**, an IT infrastructure professional working with systems and networks.

I created ResilienceLint to explore a practical question from the infrastructure field: how can we identify missing recovery requirements before they become a problem?

This project connects my professional experience in infrastructure operations with my interest in Python, automation, and resilience engineering.

I'm developing it step by step, with a focus on practical use cases, simplicity, reliability, and continuous improvement.

**Areas of interest:** IT infrastructure, systems administration, networking, business continuity, disaster recovery, and automation.

## Key features

| Feature | Description |
|---|---|
| RTO validation | Detects missing or empty RTO values |
| RPO validation | Detects missing or empty RPO values |
| Structure validation | Detects invalid workload and recovery structures |
| Clear error messages | Reports validation failures with rule identifiers |
| Automated testing | Includes a Python unit test suite |
| Continuous integration | Runs tests through GitHub Actions |
| Read-only operation | Does not modify infrastructure or configuration files |

## Requirements

- Python 3.10 or later
- pip
- PyYAML 6.x

## Installation

Clone the repository:

```bash
git clone https://github.com/neggazizaggen/ResilienceLint.git
cd ResilienceLint
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Quick start

Run the validator against a valid configuration:

```bash
python src/resiliencelint.py examples/workload-valid.yaml
```

Expected output:

```text
PASS: RTO and RPO are defined.
```

## Configuration example

```yaml
workload:
  recovery:
    rto: "4h"
    rpo: "1h"
```

- **RTO — Recovery Time Objective:** the target time to restore a service after an incident.
- **RPO — Recovery Point Objective:** the maximum targeted period of data loss, measured in time.

These values are illustrative. Actual recovery objectives should be defined according to business requirements and business impact analysis.

## Example: detecting a missing RPO

Configuration:

```yaml
workload:
  recovery:
    rto: "4h"
```

Run the validator:

```bash
python src/resiliencelint.py examples/workload-missing-rpo.yaml
```

Expected output:

```text
FAIL: RL-LINUX-001: RPO is missing.
```

The validator returns exit code `1` when validation fails, allowing automated workflows to detect the problem.

## Running the tests

Execute the unit tests:

```bash
python -m unittest discover -s tests -v
```

The current test suite covers valid RTO/RPO values, missing values, empty or whitespace-only values, and invalid workload or recovery structures.

GitHub Actions automatically runs the tests on pushes and pull requests.

## Design principles

- **Simplicity:** straightforward execution with minimal dependencies.
- **Safety:** read-only validation without infrastructure changes.
- **Clarity:** understandable error messages and rule identifiers.
- **Automation:** repeatable checks suitable for development workflows.
- **Incremental improvement:** new validation capabilities introduced step by step.

## Roadmap

- [x] Validate the presence of RTO and RPO
- [x] Detect invalid workload and recovery structures
- [x] Add automated unit tests
- [x] Configure GitHub Actions
- [x] Provide sample workload configurations
- [ ] Validate recovery time-unit formats
- [ ] Add configurable validation rules
- [ ] Improve command-line reporting
- [ ] Explore integration with infrastructure documentation and CI pipelines

Planned items are future objectives and are not yet implemented.

## Current limitations

ResilienceLint currently checks whether RTO and RPO values are present and whether the relevant YAML structures are valid.

It does not yet validate time-unit syntax, assess whether recovery objectives are realistic, verify actual infrastructure recovery capabilities, or perform disaster recovery tests.

Dedicated Kubernetes, storage, and cloud-platform validators are not currently implemented.

## Contributing

Technical feedback, suggestions, and issue reports are welcome.

If you work in infrastructure operations, systems engineering, business continuity, or disaster recovery, your feedback can help improve future validation rules.

## Technology stack

- **Language:** Python
- **Configuration:** YAML
- **Testing:** Python `unittest`
- **Continuous integration:** GitHub Actions
- **License:** Apache License 2.0

## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

---

<p align="center">
  <em>Building practical tools for more reliable infrastructure, one step at a time.</em>
</p>

