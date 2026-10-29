
# ResilienceLint

**A lightweight, read-only validation tool for infrastructure resilience readiness.**

ResilienceLint checks whether Recovery Time Objective (RTO) and Recovery Point Objective (RPO) values are defined in a YAML workload configuration.

The project aims to help infrastructure teams identify missing recovery requirements early and improve the consistency of disaster recovery documentation.

## Features

- Checks whether RTO and RPO are defined.
- Detects missing, empty, or whitespace-only values.
- Detects invalid `workload` and `recovery` data structures.
- Returns clear validation messages.
- Includes automated unit tests.
- Uses GitHub Actions to run tests on pushes and pull requests.

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

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Configuration example

Create a file named `workload.yaml`:

```yaml
workload:
  recovery:
    rto: "4h"
    rpo: "15m"
```

- **RTO (Recovery Time Objective):** the target time to restore a service after an incident.
- **RPO (Recovery Point Objective):** the maximum targeted period of data loss measured in time.

The values above are examples only. Actual recovery objectives should be defined according to business requirements.

## Usage

Run the validator from the repository root:

```bash
python src/resiliencelint.py workload.yaml
```

If both values are present, the expected output is:

```text
PASS: RTO and RPO are defined.
```

If a required value is missing or empty, the tool reports a validation failure and returns a non-zero exit code.

## Running the tests

Run the automated unit tests:

```bash
python -m unittest discover -s tests -v
```

The test suite covers valid RTO/RPO values, missing values, empty or whitespace-only values, and invalid workload or recovery structures.

## Continuous Integration

GitHub Actions automatically runs the unit tests on pushes and pull requests.

The workflow helps detect regressions when the code or tests change.

## Current limitations

- The tool checks whether RTO and RPO values are present; it does not yet validate their time-unit syntax or business suitability.
- It does not yet verify whether recovery objectives can be achieved by the actual infrastructure.
- Kubernetes, storage, and disaster recovery integrations are not yet implemented as dedicated validators.
- The tool does not modify infrastructure or configuration files.

## Project status

ResilienceLint is an early-stage open-source project intended to evolve through testing, documentation, and additional infrastructure resilience checks.

Contributions, suggestions, and technical feedback are welcome.

## License

Licensed under the Apache License 2.0. See the `LICENSE` file for details.
