"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool:
    """Verify criticality is balanced.

    :param temperature: float - temperature value in kelvin.
    :param neutrons_emitted: float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500,000.
    """
    return (
        temperature < 800
        and neutrons_emitted > 500
        and (temperature * neutrons_emitted) < 500_000
    )


def reactor_efficiency(
    voltage: float, current: float, theoretical_max_power: float
) -> str:
    """Assess reactor efficiency zone.

    :param voltage: float - voltage value.
    :param current: float - current value.
    :param theoretical_max_power: float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black -> less than 30% efficient.

    The percentage value is calculated as:
    (generated power / theoretical max power) * 100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return "green"
    if 60 <= efficiency < 80:
        return "orange"
    if 30 <= efficiency < 60:
        return "red"
    return "black"


def fail_safe(
    temperature: float, neutrons_produced_per_second: float, threshold: float
) -> str:
    """Assess and return status code for the reactor.

    :param temperature: float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: float - neutron flux.
    :param threshold: float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    Status codes:
    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    reactor_output = temperature * neutrons_produced_per_second

    if reactor_output < 0.9 * threshold:
        return "LOW"
    if 0.9 * threshold <= reactor_output <= 1.1 * threshold:
        return "NORMAL"
    return "DANGER"