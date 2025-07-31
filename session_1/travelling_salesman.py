def dummy_travelling_salesman(cities):
    """
    Dummy function to solve the Travelling Salesman Problem.
    Returns the cities in the order given and a dummy total distance.
    """
    if not cities:
        return [], 0
    total_distance = len(cities) * 10  # Dummy distance calculation
    return