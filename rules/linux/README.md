# Linux Resilience Rules

This directory contains the initial rule definitions for assessing Linux infrastructure resilience.

## Scope

The first rules focus on configuration review and operational readiness, without connecting to production systems.

Planned checks include:

- Backup policy documentation
- Recovery objectives (RTO and RPO)
- Service recovery configuration
- Storage capacity thresholds
- Evidence of restoration testing

## Rule Design Principles

Each rule should provide:

- A unique identifier
- A clear description
- A severity level
- The evidence required for assessment
- A remediation recommendation
- A test case demonstrating expected behavior

## Safety

Rules must not modify system configurations or execute recovery actions.

Results must distinguish between a confirmed failure, a detected risk, and missing evidence.

## Status

Initial documentation. No automated checks are implemented in this directory yet.
