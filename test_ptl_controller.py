from ptl_controller import process_pick_request


def test_pick_request_activates_led():
    result = process_pick_request(
        "operator_A",
        "RED"
    )

    assert result["operator_id"] == "operator_A"
    assert result["led_state"] == "SOLID:RED"

from ptl_controller import process_shared_pick_requests


def test_shared_pick_requests():
    operators = {
        "operator_A": "RED",
        "operator_B": "BLUE"
    }

    result = process_shared_pick_requests(operators)

    assert result["led_state"] == "FLASHING:RED:BLUE"
    assert result["active_operators"] == operators