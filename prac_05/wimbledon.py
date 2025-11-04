"""
Wimbledon Champions
Estimate: 50 minutes
Actual:   45 minutes
"""

import csv

FILENAME = "wimbledon.csv"

COUNTRY_INDEX = 1
WINNER_INDEX = 2


def load_data(filename: str) -> list[list[str]]:
    """Reads the CSV file, cleans up the header, and returns a list of data rows."""
    records = []

    try:
        with open(filename, "r", encoding="utf-8-sig") as in_file:
            reader = csv.reader(in_file)
            # Skip header row
            next(reader)
            for row in reader:
                if len(row) > WINNER_INDEX:  # Skip empty rows
                    records.append(row)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Using simulated data.")

        records = [
            ["2023", "SRB", "Novak Djokovic", "Carlos Alcaraz", "6-3 7-5 6-7(4) 6-4"],
            ["2022", "SRB", "Novak Djokovic", "Nick Kyrgios", "4-6 6-3 6-4 7-6(3)"],
            ["2017", "SUI", "Roger Federer", "Marin Čilić", "6-3 6-1 6-4"],
            ["2016", "GBR", "Andy Murray", "Milos Raonic", "6-4 7-6(3) 7-6(2)"],
            ["2015", "SRB", "Novak Djokovic", "Roger Federer", "7-6(1) 6-7(10) 6-4 6-3"],
            ["2003", "SUI", "Roger Federer", "Mark Philippoussis", "7-6(5) 6-2 7-6(3)"],
            ["2002", "AUS", "Lleyton Hewitt", "David Nalbandian", "6-1 6-3 6-2"],
            ["1970", "AUS", "Rod Laver", "John Newcombe", "6-4 5-7 6-4 8-6"]
        ]
    return records


def process_records(records: list[list[str]]) -> tuple[dict[str, int], set[str]]:
    """Calculates the champion win counts and collects unique winning countries."""
    champion_wins = {}
    countries = set()

    for record in records:
        winner = record[WINNER_INDEX]
        country = record[COUNTRY_INDEX]

        # 1. Update champion win counts (dictionary)
        # Using EAFP approach (try-except)
        try:
            champion_wins[winner] += 1
        except KeyError:
            champion_wins[winner] = 1

        # 2. Add country to the set
        countries.add(country)

    return champion_wins, countries


def display_results(champion_wins: dict[str, int], countries: set[str]):
    """Prints the champion wins and the sorted list of unique countries."""

    # Sort champions by name for cleaner output
    sorted_champions = sorted(champion_wins.items())

    print("Wimbledon Champions:")
    for champion, wins in sorted_champions:
        print(f"{champion} {wins}")

    # Convert the set to a sorted list, then join to a single string
    sorted_countries = sorted(list(countries))
    country_string = ", ".join(sorted_countries)

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(country_string)


def main():
    """Main function to load, process, and display Wimbledon data."""
    print("Starting Wimbledon Data Processing...")

    records = load_data(FILENAME)

    champion_wins, countries = process_records(records)

    # Final results
    display_results(champion_wins, countries)

    print("Processing complete.")

if __name__ == "__main__":

    main()
