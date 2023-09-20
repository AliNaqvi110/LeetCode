class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        guess = x/2  # Initial guess
        tolerance = 1e-6  # You can adjust the tolerance as needed.

        while True:
            new_guess = 0.5 * (guess + x / guess)
            if abs(new_guess - guess) < tolerance:
                return int(new_guess)
            guess = new_guess
