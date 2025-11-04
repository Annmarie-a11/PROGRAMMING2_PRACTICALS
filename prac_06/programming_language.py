# programming_language.py

class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the language is dynamically typed."""
        # Checks the internal 'typing' attribute
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        # Format: Python, Dynamic Typing, Reflection=True, First appeared in 1991
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"



# languages.py

from programming_language import ProgrammingLanguage

def main():
    """Create ProgrammingLanguage objects and demonstrate their methods."""
    # The objects
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Test __str__ method
    print(python)

    # Create the list
    languages = [python, ruby, visual_basic]

    print("\nThe dynamically typed languages are:")

    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()