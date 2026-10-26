def get_led_state(active_operators):
    colors = list(active_operators.values())

    if len(colors) == 0:
        return "OFF"

    elif len(colors) == 1:
        return f"SOLID:{colors[0]}"

    elif len(colors) == 2:
        return f"FLASHING:{colors[0]}:{colors[1]}"

    else:
        raise ValueError("Too many operators")


def complete_work_order(active_operators, operator_id):
    remaining = active_operators.copy()
    remaining.pop(operator_id, None)

    return get_led_state(remaining)