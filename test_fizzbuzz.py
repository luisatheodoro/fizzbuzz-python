import unittest
import fizzbuzz 

class FizzBuzzTest(unittest.TestCase):
    def test_return_fizz_with_multiples_of_3(self):
        self.assertEqual('Fizz', fizzbuzz.FizzBuzz(3))
        
    def test_return_buzz_with_multiples_of_5(self):
        self.assertEqual('Buzz', fizzbuzz.FizzBuzz(5))
        
    def test_return_fizzbuzz_with_multiples_of_15(self):
        self.assertEqual('FizzBuzz', fizzbuzz.FizzBuzz(15))
        
    def test_return_number_when_not_multiples_of_3_5_15(self):
        self.assertEqual(4, fizzbuzz.FizzBuzz(4))
        
        
if __name__ == "__main__":
  unittest.main()
  