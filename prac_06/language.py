"""
Module: languages.py
Estimated time to complete: 15 minutes
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print the ProgrammingLanguage instances to verify the __str__ method
print(python)
print(ruby)
print(visual_basic)

# Create a list containing the ProgrammingLanguage objects
languages_list = [python, ruby, visual_basic]

# Print the list to confirm it contains the objects
for language in languages_list:
    print(language)
