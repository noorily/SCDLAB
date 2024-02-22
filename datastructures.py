# data_structures.py

class DataProcessor:
    def __init__(self):
        # Initialize any necessary attributes
        pass

    def process_data(self, data):
        # Implement your data processing logic here
        # For example, you can manipulate the data, perform calculations, etc.
        processed_data = data.upper()  # Just an example; replace with your actual processing

        return processed_data

# Example usage:
if __name__ == "__main__":
    data_processor = DataProcessor()
    input_data = "Hello, World!"
    processed_result = data_processor.process_data(input_data)
    print(f"Processed result: {processed_result}")
2.5
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('grape')
fruits.sort()
print(fruits)  # Output: ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
student_scores['David'] = 95
print(student_scores)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}
colors1 = {'red', 'green', 'blue'}
colors2 = {'blue', 'yellow', 'green'}
common_colors = colors1.intersection(colors2)
print(common_colors)  # Output: {'green', 'blue'}
2.6
# Example class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Create instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Call methods
print(person1.greet())  # Output: "Hello, my name is Alice and I am 30 years old."
print(person2.greet())  # Output: "Hello, my name is Bob and I am 25 years old."
