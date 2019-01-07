import unittest
import fizzbuzz 

class FizzBuzzTest(unittest.TestCase):
    def test_return_fizz_with_multiples_of_3(self):
        self.assertEqual('Fizz', fizzbuzz.FizzBuzz(3))
        
        
if __name__ == "__main__":
  unittest.main()
  