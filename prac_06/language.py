"""
Module: languages.py
Estimated time to complete: 30 minutes
Current time: 2pm
Time to complete: 45 minutes (including programming_language.py)
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)
print(ruby)
print(visual_basic)

languages_list = [python, ruby, visual_basic]

# new code that was written on paper
print("The dynamically typed languages are:")
for language in languages_list:
    if language.is_dynamic():  # Use the is_dynamic method
        print(language.name)  # Print the name of the dynamically typed language
