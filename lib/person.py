#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", job="Unemployed"):
        self.set_name(name)
        self.set_job(job)
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"

    name = property(get_name, set_name)

    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Unemployed"

    job = property(get_job, set_job)


# Creating an instances with valid names and jobs
person1 = Person("john doe", "ITC")
print(f"Person1: Name={person1.name}, Job={person1.job}")

# Creating an instance with empty name and valid job
person2 = Person("", "Sales")
print(f"Person2: Name={person2.name}, Job={person2.job}")

# Creating an instance with non-string name and valid job
person3 = Person(12345, "Marketing")
print(f"Person3: Name={person3.name}, Job={person3.job}")

# Creating an instance with long string name and valid job
person4 = Person("A very very very long name that exceeds limit", "Finance")
print(f"Person4: Name={person4.name}, Job={person4.job}")

# Creating an instance with valid name and invalid job
person5 = Person("Jane Doe", "Musician")
print(f"Person5: Name={person5.name}, Job={person5.job}")