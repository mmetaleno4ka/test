import sys
import math

class Figure:
    def __init__(self, shape, value1, value2=None):
        self.__shape = shape.lower()
        self.__value1 = value1
        self.__value2 = value2 if value2 is not None else value1

    # getters for values
    @property
    def shape(self):
        return self.__shape

    @property
    def value1(self):
        return self.__value1
    
    @property
    def value2(self):
        return self.__value2
        
    def calculate(self):
        if self.__shape == "square":
            perimeter = 4 * self.__value1
            area = self.__value1 ** 2
            return f"Shape: Square\nPerimeter: {perimeter:.2f}\nArea: {area:.2f}"
        
        elif self.__shape == "circle":
            perimeter = 2 * math.pi * self.__value1
            area = math.pi * (self.__value1 ** 2)
            return f"Shape: Circle\nPerimeter: {perimeter:.2f}\nArea: {area:.2f}"
        
        elif self.__shape == "rectangle":
            height = self.__value1
            width = self.__value2
            perimeter = 2 * (height + width)
            area = height * width
            return f"Shape: rectangle\nPerimeter: {perimeter:.2f}\nArea: {area:.2f}"
        
        else:
            return f"Unknown shape: {self.__shape}"

def calculate_shapes(input_data):
    results = []
    for line in input_data:
        try:
            parts = line.strip().split()
            shape = parts[0]
            value1 = float(parts[1])
            value2 = float(parts[2]) if len(parts) > 2 else None
            figure = Figure(shape, value1, value2)
            results.append(figure.calculate())
        except ValueError:
            results.append(f"Invalid input: {line.strip()}")
    return results

if __name__ == "__main__":
    
    input_data = []
    while True:
        line = input("Enter a shape and its value(s): ")
        if not line:
            break
        input_data.append(line)
    
    if not input_data:
        sys.stdout.write("No input => exiting...\n")
    else:
        results = calculate_shapes(input_data)
        sys.stdout.write("\nResults:\n")
        sys.stdout.write("\n".join(results) + "\n")