### Exercises "The Oldest Dog"
# Using the same Dog class, instantiate three new dogs, each with a different age.
# Then write a function called, get_biggest_number(), that takes any number of ages (*args) and
# returns the oldest one. Then output the age of the oldest dog like so:
#                                   The oldest dog is 7 years old.



class Dog:

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        return f"{self.name} says {sound}"


# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print(f"{philo.name} is {philo.age} and {mikey.name} is {mikey.age}.")

# Is Philo a mammal?
if philo.species == "mammal":
    print(f"{philo.name} is a {philo.species}!")

print(philo.speak("Woof Woof"))
print(mikey.speak("Waf Waf"))
