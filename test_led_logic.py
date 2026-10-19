
from led_logic import complete_work_order


def test_operator_completion():
    operators = {
        "OP1": "BLUE",
        "OP2": "GREEN"
    }

    result = complete_work_order(operators, "OP2")

    assert result == "SOLID:BLUE"
