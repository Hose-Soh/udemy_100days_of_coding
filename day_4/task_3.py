import random

# using random.choice
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

# using random.randint

random_index = random.randint(0,4)
print(friends[random_index])
