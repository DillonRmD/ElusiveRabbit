import random

NUM_HOLES = 100
NUM_PASSES = 4

class Rabbit:
    def __init__(self):
        self.position = random.randint(0, NUM_HOLES - 1)

    def hop(self):
        if self.position == NUM_HOLES - 1:
            self.position -= 1
        elif self.position == 0:
            self.position += 1
        else:
            left = random.randint(0, 1)
            if left == 0:
                self.position += 1
            elif left == 1:
                self.position -= 1

class Hole:
    def __init__(self):
        self.hasRabbit = False
    def Enter(self):
        self.hasRabbit = True
    def Leave(self):
        self.hasRabbit = False

def main():
    
    # This will hold all of our Hole objects
    rabbit = Rabbit()
    holes = []
    # Create all of our holes
    for i in range(0, NUM_HOLES - 1):
        hole = Hole()
        holes.append(hole)

    # Place the rabbit in a random hole
    holes[rabbit.position].Enter()

    print("Rabbit started at: " + str(rabbit.position))

    doEven = True
    for currentPass in range(0, NUM_PASSES):
        print("============ Pass: " + str(currentPass) + " ============")
        if doEven:
            for i in range(0, NUM_HOLES - 1):
                if i % 2 == 0:
                    print("Rabbit currently at: " + str(rabbit.position))
                    if holes[i].hasRabbit == True:
                        print("Found rabbit at hole: " + str(i) + " on pass: " + str(currentPass))
                        exit(1)
                    elif holes[i].hasRabbit == False:
                        print("Searched: " + str(i))
                        holes[rabbit.position].Leave()
                        rabbit.hop()
                        holes[rabbit.position].Enter()
            doEven = False
        elif doEven == False:
            for i in range(0, NUM_HOLES - 1):
                if i % 2 != 0:
                    print("Rabbit currently at: " + str(rabbit.position))
                    if holes[i].hasRabbit == True:
                        print("Found rabbit at hole: " + str(i) + " on pass: " + str(currentPass))
                        exit(1)
                    elif holes[i].hasRabbit == False:
                        print("Searched: "+ str(i))
                        holes[rabbit.position].Leave()
                        rabbit.hop()
                        holes[rabbit.position].Enter()
            doEven = True


if __name__ == "__main__":
    main()