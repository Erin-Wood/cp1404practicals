"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Initialize a ProgrammingLanguage with name, typing, reflection, year, and pointer arithmetic support."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a string representation of the programming language, including pointer arithmetic support."""
        return (f"{self.name}, Typing: {self.typing}, Reflection: {'Yes' if self.reflection else 'No'}, "
                f"Year: {self.year}, Pointer Arithmetic: {'Yes' if self.pointer_arithmetic else 'No'}")

    def supports_pointer_arithmetic(self):
        """Return True if the language supports pointer arithmetic."""
        return self.pointer_arithmetic


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    with open('languages.csv', 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            languages.append(language)

    for language in languages:
        print(language)


def csv_version():
    """CSV version that reads file and uses ProgrammingLanguage class with pointer arithmetic."""
    with open('languages.csv', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)
        languages = [ProgrammingLanguage(row[0], row[1], row[2] == "Yes", int(row[3]), row[4] == "Yes")
                     for row in reader]
    for language in languages:
        print(language)


def namedtuple_version():
    """namedtuple version that reads file and displays programming languages with pointer arithmetic."""
    ProgrammingLanguageTuple = namedtuple('ProgrammingLanguageTuple',
                                          'name, typing, reflection, year, pointer_arithmetic')
    with open('languages.csv', newline='') as in_file:
        reader = csv.reader(in_file)
        next(reader)
        languages = [ProgrammingLanguageTuple(row[0], row[1], row[2] == "Yes", int(row[3]), row[4] == "Yes")
                     for row in reader]
    for language in languages:
        print(language)


if __name__ == '__main__':
    main()
