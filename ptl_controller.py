from led_logic import get_led_state


def process_pick_request(operator_id, color):
    active_operators = {
        operator_id: color
    }

    led_state = get_led_state(active_operators)

    return {
        "operator_id": operator_id,
        "led_state": led_state
    }
def process_shared_pick_requests(active_operators):
    led_state = get_led_state(active_operators)

    return {
        "active_operators": active_operators.copy(),
        "led_state": led_state
    }