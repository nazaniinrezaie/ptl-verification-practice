
# Pick-to-Light Verification Practice

A Python-based project focused on functional verification and software integration testing of simulated Pick-to-Light system logic.

## Project Overview

This project simulates LED state management for industrial material-picking workflows.

It verifies LED behavior during operator assignment, shared picking locations, and work-order completion.

## Technologies

- Python
- pytest
- Git and GitHub

## System Components

- `led_logic.py` — LED state management and operator completion logic
- `ptl_controller.py` — Simulated picking request processing
- `test_led_logic.py` — Functional and negative tests
- `test_ptl_controller.py` — Software integration tests

## Implemented Test Scenarios

### Functional and Negative Testing (5 tests)

- Operator completion and LED state transition
- Shared picking location with two operators
- Complete LED workflow: OFF, SOLID, FLASHING, SOLID, OFF
- Rejection of more than two active operators
- Handling completion requests from unknown operators

### Software Integration Testing (2 tests)

- Picking request processing through the controller and LED logic
- Shared picking request processing for two operators

## Test Results

7 automated pytest tests passed in local testing.

## Running the Tests

Install pytest:

```bash
python3 -m pip install pytest
```

Run:

```bash
python3 -m pytest test_led_logic.py test_ptl_controller.py -v
```

## Future Improvements

- Stateful controller supporting multiple picking events
- MQTT communication testing using mocks
- Additional boundary and failure scenarios
- Automated CI using GitHub Actions

## Note

This is an independent educational simulation inspired by industrial system integration and verification concepts. It does not contain proprietary company code or use physical PTL hardware.
