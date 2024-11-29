from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialize a Project instance with name, start date, priority, cost estimate, and completion percentage."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        """Return a string representation of a Project."""
        start_date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_date_str}, priority: {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def __lt__(self, other):
        """Less-than comparison for sorting by priority."""
        return self.priority < other.priority

    def is_completed(self):
        """Return True if the project is completed, otherwise False."""
        return self.completion == 100
