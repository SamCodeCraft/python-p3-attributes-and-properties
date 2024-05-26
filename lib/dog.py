#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Mutt"):
        self.set_name(name)
        self.set_breed(breed)
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Mutt"

    breed = property(get_breed, set_breed)

# Test cases to demonstrate functionality
# Creating an instance with valid name and breed
dog1 = Dog("Fido", "Beagle")
print(f"Dog1: Name={dog1.name}, Breed={dog1.breed}")

# Creating an instance with empty name and valid breed
dog2 = Dog("", "Pug")
print(f"Dog2: Name={dog2.name}, Breed={dog2.breed}")

# Creating an instance with non-string name and valid breed
dog3 = Dog(12345, "Pointer")
print(f"Dog3: Name={dog3.name}, Breed={dog3.breed}")

# Creating an instance with long string name and valid breed
dog4 = Dog("A very very very long name that exceeds limit", "Mastiff")
print(f"Dog4: Name={dog4.name}, Breed={dog4.breed}")
