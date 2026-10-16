# Random List
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
list_length = len(friends)
random_friends = random.randint(0, list_length)
print(friends[random_friends])

# Option 2
print(random.choice(friends))

