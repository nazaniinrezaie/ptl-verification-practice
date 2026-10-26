from led_logic import get_led_state, complete_work_order


def test_operator_completion():
    active_operators = {
        "operator_1": "RED",
        "operator_2": "BLUE"
    }

    result = complete_work_order(active_operators, "operator_1")

    assert result == "SOLID:BLUE"


def test_shared_location_after_first_operator_completes():
    active_operators = {
        "operator_A": "RED",
        "operator_B": "BLUE"
    }

    result = complete_work_order(active_operators, "operator_A")

    assert result == "SOLID:BLUE"
    assert len(active_operators) == 2

def test_full_led_workflow():
    operators = {}

    assert get_led_state(operators) == "OFF"

    operators["operator_A"] = "RED"
    assert get_led_state(operators) == "SOLID:RED"

    operators["operator_B"] = "BLUE"
    assert get_led_state(operators) == "FLASHING:RED:BLUE"

    state = complete_work_order(operators, "operator_A")
    assert state == "SOLID:BLUE"

    state = complete_work_order(
        {"operator_B": "BLUE"}, "operator_B"
    )
    assert state == "OFF"
import pytest


def test_too_many_operators():
    operators = {
        "operator_A": "RED",
        "operator_B": "BLUE",
        "operator_C": "GREEN"
    }

    with pytest.raises(ValueError, match="Too many operators"):
        get_led_state(operators)

def test_unknown_operator_completion():
    operators = {
        "operator_A": "RED",
        "operator_B": "BLUE"
    }

    result = complete_work_order(
        operators, "operator_C"
    )

    assert result == "FLASHING:RED:BLUE"
    assert len(operators) == 2