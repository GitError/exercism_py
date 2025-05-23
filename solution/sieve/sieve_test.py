import unittest
from sieve import primes

class SieveTest(unittest.TestCase):
    def test_no_primes_under_2(self):
        """Test that there are no prime numbers under 2"""
        self.assertEqual(primes(1), [])
        
    def test_find_first_prime(self):
        """Test that 2 is the first prime number"""
        self.assertEqual(primes(2), [2])
        
    def test_find_primes_up_to_10(self):
        """Test finding primes up to 10"""
        self.assertEqual(primes(10), [2, 3, 5, 7])
        
    def test_limit_is_prime(self):
        """Test when the limit itself is a prime number"""
        self.assertEqual(primes(13), [2, 3, 5, 7, 11, 13])
        
    def test_find_primes_up_to_1000(self):
        """Test finding primes up to 1000"""
        expected = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
            67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 
            139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 
            223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 
            293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 
            383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 
            463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 
            569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 
            647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 
            743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 
            839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 
            941, 947, 953, 967, 971, 977, 983, 991, 997
        ]
        self.assertEqual(primes(1000), expected)
        
    def test_boundary_conditions(self):
        """Test boundary conditions"""
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(-10), [])
        
    def test_performance(self):
        """Basic performance test"""
        # This is not a thorough performance test, but ensures the algorithm can handle larger inputs
        result = primes(10000)
        self.assertEqual(len(result), 1229)  # There are 1229 primes less than 10,000

if __name__ == "__main__":
    unittest.main()
