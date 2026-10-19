
# Pick-to-Light Verification Practice

A Python-based testing project focused on functional verification and automated testing of Pick-to-Light system logic.

## Project Overview

This project simulates LED state management for a Pick-to-Light system used in industrial material picking workflows.

The objective is to verify that LED states are correctly updated when operators start or complete their work orders.

## Technologies

- Python
- pytest
- Git and GitHub

## Test Scenario

Two operators share the same picking location.

- Operator 1: Blue
- Operator 2: Green
- Initial LED state: Flashing Blue/Green
- Event: Operator 2 completes their work order
- Expected result: Solid Blue

## Running the Tests

Install pytest:

```bash
python3 -m pip install pytest
```

Run the tests:

```bash
python3 -m pytest -v
```

## Current Test Coverage

- Operator completion and LED state transition
- Verification of expected versus actual results

## Future Improvements

- MQTT communication testing using mocks
- Negative test cases
- Boundary testing
- Automated CI with GitHub Actions

## Note

This is an independent educational simulation inspired by industrial system integration and verification concepts. It does not contain proprietary company code.
