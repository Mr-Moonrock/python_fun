"""Word Finder: finds random words from a dictionary."""
import random


""" Path to the file containing the words to be searched"""
file_path = r"C:\Users\User\Desktop\words.txt"

class WordFinder:
    
    def __init__(self, file_path):
        """
        Initializes the WordFinder with a path to a file containing the words

        """
        self.file_path = file_path
        self.words = self._read_words_from_file()
        self.num_words = len(self.words)
        print(f"{self.num_words} words read")

    def _read_words_from_file(self):
        """
        Reads words from the file and returns a list of words.
        
        """
        with open(self.file_path, 'r') as file:
            words = [line.strip() for line in file.readlines()]
        return words
    
    def random(self):
        """
        Returns a random word from the list of words. 
        """
        return random.choice(self.words)
    