
from guitar import Guitar, CURRENT_YEAR


def run_tests():
    """Test the Guitar class methods."""

    # Test case 1: Vintage Guitar
    name_1 = "Gibson L-5 CES"
    year_1 = 1922
    cost_1 = 16035.40
    guitar_1 = Guitar(name_1, year_1, cost_1)
    expected_age_1 = CURRENT_YEAR - year_1

    # Test case 2: Modern Guitar
    name_2 = "Another Guitar"
    year_2 = 2013
    cost_2 = 500.00
    guitar_2 = Guitar(name_2, year_2, cost_2)
    expected_age_2 = CURRENT_YEAR - year_2

    print(f"Testing {CURRENT_YEAR} as the current year.")
    print("-" * 30)

    # Test get_age()
    print(f"{name_1} get_age() - Expected {expected_age_1}. Got {guitar_1.get_age()}")
    print(f"{name_2} get_age() - Expected {expected_age_2}. Got {guitar_2.get_age()}")

    print("-" * 30)

    # Test is_vintage()
    expected_vintage_1 = True
    expected_vintage_2 = False

    print(f"{name_1} is_vintage() - Expected {expected_vintage_1}. Got {guitar_1.is_vintage()}")
    print(f"{name_2} is_vintage() - Expected {expected_vintage_2}. Got {guitar_2.is_vintage()}")

    # Test a 50-year-old guitar (boundary case)
    name_3 = "50-Year Old Guitar"
    year_3 = CURRENT_YEAR - 50
    guitar_3 = Guitar(name_3, year_3, 1000)
    print("-" * 30)
    print(f"{name_3} is_vintage() - Expected True. Got {guitar_3.is_vintage()}")


if __name__ == "__main__":
    run_tests()