# guitars.py
from guitar import Guitar


def main():
    """Get guitar data from user until blank name, then display all guitars."""
    guitars =  []

    # Fast testing data - comment out when doing user input
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("My guitars!")


    if not guitars:
        print("No guitars added.")
        return

    print("\nThese are my guitars:")



    for i, guitar in enumerate(guitars, 1):
        # Ternary operator to set the vintage string
        vintage_string = " (vintage)" if guitar.is_vintage() else ""


        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()