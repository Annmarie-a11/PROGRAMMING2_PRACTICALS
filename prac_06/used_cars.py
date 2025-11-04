# used_cars.py
"""
CP1404/CP5632 - Practical
Client code to use the Car class.
Note that the import has changed to be part of prac_06.
"""

from car import Car

def main():
    """Demo test code."""

    limo = Car("Limo", 100)

    limo.add_fuel(20)

    # Print amount of fuel in the car.
    print(f"Limo fuel: {limo.fuel} units")

    # Attempt to drive the car 115 km using the drive method.
    distance_driven = limo.drive(115)
    print(f"Limo drove {distance_driven}km")

    bus = Car("Bus", 180)

    # Test code (modified to use the new name)
    print("--- Original Car Tests ---")
    print(bus)  # Test __str__
    bus.drive(30)
    print(f"Bus fuel: {bus.fuel}")
    print(bus)

    print("--- Limo __str__ Test ---")
    print(limo)


main()