# ElusiveRabbit
A simulation and algorithm application to find an elusive rabbit that hops from hole to hole
Inspired by the [Ben Awad Mock Coding Interview with Redux Co-Creator Dan Abramov](https://www.youtube.com/watch?v=XEt09iK8IXs)

## Here are the rules of the simulation:
- The rabbit is randomly placed in a collection of holes, whose collection size is determined by the ```NUM_HOLES``` variable.
- You may only search one hole at a time.
- When a hole is searched, the rabbit leaves it's current hole and hops to a hole adjacent to it's previous hole. That is left or right of whatever hole it was currently at

## Solution
What is the best method to deterministically find this pesky, small mammal?
- Well, as is demonstrated in the mock interview, the best method is to make several passes through the collection of holes and on each pass either search only odd or even holes.
- This simple python script showcases this idea!

## Contribution
Feel free to contribute, reuse, and distribute any of the code in this repository, free of charge!
