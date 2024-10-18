FILENAME = "wimbledon.csv"


def main():
    """Read the Wimbledon data and print champions and countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Read the file and return the records as a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Count how many times each champion won and collect the countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        country = record[1]
        champion = record[2]
        countries.add(country)

        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Print the list of champions with their win counts and the list of countries."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion}: {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
