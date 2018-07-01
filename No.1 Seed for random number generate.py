import random
random.seed(1)
print('seed 1 generate 3 random int number:')
print(random.randint(1,10),random.randint(1,10),random.randint(1,10))


random.seed(2)
print('seed 2 generate 3 random int number:')
print(random.randint(1,10),random.randint(1,10),random.randint(1,10))

random.seed(10)
print('seed 10 generate 3 random int number:')
print(random.randint(1,10),random.randint(1,10),random.randint(1,10))

random.seed(1)
print('seed 1 generate 2 random int number:')
print(random.randint(1,10),random.randint(1,10))

random.seed(2)
print('seed 2 generate 2 random int number:')
print(random.randint(1,10),random.randint(1,10))

random.seed(10)
print('seed 10 generate 2 random int number:')
print(random.randint(1,10),random.randint(1,10))
