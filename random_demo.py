import random

def main():
    #create a random number generator

    random_generator = random.Random()

    for _ in range(20):
        print(random_generator.randint(1,100))


main()