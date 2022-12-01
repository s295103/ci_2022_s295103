## Overview
We use a class ```Nim``` to create, store and decrease the heaps and a class ```Player``` to manage the players of the game. Each strategy implemented is tested in a *match* consisting of *100 games*. To offset the empirical advantage in making the first move, the player who starts first is decided randomly.

## Task 3.1
A strategy using the nim-sum technique according to the [nim Wikipedia article](https://en.wikipedia.org/wiki/Nim) that also manages the critical layouts where the nim-sum strategy fails. It wins roughly 80% of the time against a *random strategy* opponent and 50% of the time against a *nim-sum strategy* one.

## Task 3.2
We represented the action to take in each ply with two probabilities: *one to select the heap and one to select the quantity*, storing everything in a list long the maximum number of plies. The fitness was evaluated using the strategy stored in the individual to play a match of 100 games against a nim-sum strategy opponent: the percentage of wins was thus the fitness of the individual. The best implementation so far used an *island model* for diversity control, *(μ, λ) and elitism* for survivor selection, *arithmetic recombination* for binary crossover, *adaptive step size* for mutation and *extinction* when the mean fitness converged. The mean fitness, the best fitness and the standard deviation are plotted for each generation. 

