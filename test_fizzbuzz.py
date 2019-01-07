import unittest
import fizzbuzz 

class FizzBuzzTest(unittest.TestCase):
    def test_return_fizz_with_multiples_of_3(self):
        self.assertEqual('Fizz', fizzbuzz.FizzBuzz(3))
        
    def test_return_buzz_with_multiples_of_5(self):
        self.assertEqual('Buzz', fizzbuzz.FizzBuzz(5))
        
        
        
if __name__ == "__main__":
  unittest.main()
  