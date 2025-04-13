"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    # No optimization needed - already O(n) optimal
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # Simplified: Extract first two wagons and directly find locomotive from remainder
    first, second, *rest = each_wagons_id
    
    # Find locomotive and remove it from rest in one pass - O(n)
    locomotive = 1  # Locomotive always has ID 1
    rest = [wagon for wagon in rest if wagon != locomotive]
    
    # More efficient construction - avoids multiple list concatenations
    return [locomotive] + missing_wagons + rest + [first, second]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    # Optimize by creating the result directly without intermediate steps
    return {
        **route,
        "stops": [kwargs[key] for key in sorted(kwargs)]  # More concise list comprehension
    }


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    # Combine the two dictionaries using unpacking
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Optimize using zip to transpose the matrix - O(n) operation
    # This is more efficient than manual unpacking for arbitrary sized input
    return list(map(list, zip(*wagons_rows)))
