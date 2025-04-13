import unittest
from locomotive_engineer import (
    get_list_of_wagons, fix_list_of_wagons, 
    add_missing_stops, extend_route_information, 
    fix_wagon_depot
)

class LocomotiveEngineerTests(unittest.TestCase):
    def test_get_list_of_wagons(self):
        """Test that get_list_of_wagons returns a list of all wagons."""
        self.assertEqual(get_list_of_wagons(1, 7, 12, 3, 14, 8, 5), [1, 7, 12, 3, 14, 8, 5])
        self.assertEqual(get_list_of_wagons(1), [1])
        self.assertEqual(get_list_of_wagons(), [])

    def test_fix_list_of_wagons(self):
        """Test that fix_list_of_wagons correctly reorders the wagons."""
        self.assertEqual(
            fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]),
            [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
        )
        self.assertEqual(
            fix_list_of_wagons([1, 2, 3], [4, 5]),
            [1, 4, 5, 3, 1, 2]
        )
        self.assertEqual(
            fix_list_of_wagons([5, 9, 1], []),
            [1, 5, 9]
        )

    def test_add_missing_stops(self):
        """Test that add_missing_stops correctly adds stops to the route."""
        # Test with keyword arguments
        self.assertEqual(
            add_missing_stops({"from": "New York", "to": "Miami"},
                             stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                             stop_4="Jacksonville", stop_5="Orlando"),
            {"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}
        )
        
        # Test with no stops
        self.assertEqual(
            add_missing_stops({"from": "Berlin", "to": "Hamburg"}),
            {"from": "Berlin", "to": "Hamburg", "stops": []}
        )
        
        # Test with unsorted stops
        self.assertEqual(
            add_missing_stops({"from": "Paris", "to": "Lyon"}, stop_3="Dijon", stop_1="Orleans", stop_2="Bourges"),
            {"from": "Paris", "to": "Lyon", "stops": ["Orleans", "Bourges", "Dijon"]}
        )

    def test_extend_route_information(self):
        """Test that extend_route_information correctly merges route information."""
        self.assertEqual(
            extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}),
            {"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}
        )
        
        self.assertEqual(
            extend_route_information({"from": "Paris", "to": "London"}, {"type": "Eurostar", "wifi": True, "snacks": True}),
            {"from": "Paris", "to": "London", "type": "Eurostar", "wifi": True, "snacks": True}
        )
        
        # Test with empty second dict
        self.assertEqual(
            extend_route_information({"from": "Tokyo", "to": "Osaka"}, {}),
            {"from": "Tokyo", "to": "Osaka"}
        )

    def test_fix_wagon_depot(self):
        """Test that fix_wagon_depot correctly reorganizes the wagon depot."""
        self.assertEqual(
            fix_wagon_depot([
                [(2, "red"), (4, "red"), (8, "red")],
                [(5, "blue"), (9, "blue"), (13,"blue")],
                [(3, "orange"), (7, "orange"), (11, "orange")]
            ]),
            [
                [(2, "red"), (5, "blue"), (3, "orange")],
                [(4, "red"), (9, "blue"), (7, "orange")],
                [(8, "red"), (13,"blue"), (11, "orange")]
            ]
        )
        
        # Test with smaller depot
        self.assertEqual(
            fix_wagon_depot([
                [(1, "red"), (2, "red")],
                [(3, "blue"), (4, "blue")],
                [(5, "orange"), (6, "orange")]
            ]),
            [
                [(1, "red"), (3, "blue"), (5, "orange")],
                [(2, "red"), (4, "blue"), (6, "orange")]
            ]
        )

if __name__ == "__main__":
    unittest.main()
