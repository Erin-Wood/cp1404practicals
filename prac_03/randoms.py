import random

#Line 1
print(random.randint(5, 20))
# What did you see on line 1?
# Answer: I saw numbers between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number was 5, and the largest was 20.

# Line 2
print(random.randrange(3, 10, 2))
# What did you see on line 2?
# Answer: I saw odd numbers between 3 and 9.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number was 3, and the largest was 9.
# Could line 2 have produced a 4?
# Answer: No, because the step is 2, which generates odd numbers only.

# Line 3
print(random.uniform(2.5, 5.5))
# What did you see on line 3?
# Answer: I saw floating-point numbers between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number was 2.5, and the largest was 5.5.

# Code to produce a random number between 1 and 100 inclusive:
random_number = random.randint(1, 100)
print(random_number)