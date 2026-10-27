# Security policy

## Scope

This repository is a knowledge base. It has no runtime, ships no credentials, and collects nothing.

Every pattern carries an `authorization` field. Patterns describe mechanism, precondition and
verification. They do not target a named third party.

## Before you use a pattern

1. Confirm you own the target or hold written permission, and record it.
2. Read the wave's tree. Several branches say **stop**, and they mean it. W02 and W03 both contain
   branches where the correct action is to report the class closed rather than to continue.
3. Acknowledged risk is not consent. A production system you can reach is not a system you may test.

## Reporting a problem in this repository

- Incorrect claim, bad counter, wrong precondition: open an issue with the pattern id.
- A pattern you believe crosses from methodology into operational harm: open an issue titled
  `scope concern` and quote the id. That is a legitimate defect report and it gets treated as one.

## Known limits

- 0 patterns are marked OBSERVED. Nothing here has been lab verified by this project, which is stated in
  the README and enforced by the gate vocabulary.
- Counters are per attack class, not per individual tool.
