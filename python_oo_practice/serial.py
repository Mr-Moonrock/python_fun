"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start):
        """Intializes the SerialGenerator with a starting value."""
        self.serial = start
        self.current = start -1 

    def generate(self):
        """Generates and retruns the next sequential number."""
        self.current += 1
        return self.current
    
    def reset(self):
        """Reset the generator back to the original start value."""
        self.current = self.serial -1


