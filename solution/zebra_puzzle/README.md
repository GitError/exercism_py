# Zebra Puzzle

## Description

The Zebra Puzzle, also known as Einstein's Puzzle or Einstein's Riddle, is a well-known logic puzzle. The puzzle is often attributed to Albert Einstein, although there's no evidence that he created it.

## The Puzzle

There are five houses in a row, each painted a different color and inhabited by a person of a different nationality. Each person has a different pet, prefers a different drink, and enjoys a different hobby. The puzzle presents a series of clues, and the solver must determine who owns the zebra and who drinks water.

## The Clues

1. There are five houses.
2. The Englishman lives in the red house.
3. The Spaniard owns the dog.
4. The person in the green house drinks coffee.
5. The Ukrainian drinks tea.
6. The green house is immediately to the right of the ivory house.
7. The snail owner likes to go dancing.
8. The person in the yellow house is a painter.
9. The person in the middle house drinks milk.
10. The Norwegian lives in the first house.
11. The person who enjoys reading lives in the house next to the person with the fox.
12. The painter's house is next to the house with the horse.
13. The person who plays football drinks orange juice.
14. The Japanese person plays chess.
15. The Norwegian lives next to the blue house.

## Solution Approach

This implementation uses a constraint-based approach with permutations to find a valid assignment that satisfies all constraints. The algorithm systematically:

1. Tries all permutations of colors, nationalities, drinks, pets, and hobbies
2. Applies early pruning by checking constraints as soon as relevant variables are assigned
3. Returns the first valid solution found (the puzzle has a unique solution)

## Performance Considerations

The solution uses a caching mechanism to avoid recomputing the puzzle solution each time the `drinks_water()` or `owns_zebra()` functions are called.

## Running Tests

To run the tests, execute:

```bash
python -m unittest test_zebra_puzzle.py
```

## Expected Results

- The Norwegian drinks water
- The Japanese owns the zebra
