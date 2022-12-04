## Overview
We use a class ```Nim``` to create, store and decrease the heaps and a class ```Player``` to manage the players of the game. Each strategy implemented is tested in a *match* consisting of *100 games*. To offset the empirical advantage in making the first move, the player who starts first is decided randomly.

## Task 3.1 Nim-Sum
A strategy using the nim-sum technique according to the [nim Wikipedia article](https://en.wikipedia.org/wiki/Nim) that also manages the critical layouts where the nim-sum strategy fails. **It wins almost 100% of the time against a *random strategy* opponent and around 50% of the time against a *nim-sum strategy* one.**

## Task 3.2 Evolutionary Algorithm
We represented the strategy as a sequence of IF-ELSE statements, consisting in conditions and actions. A condition is a list of integers, an action is a tuple of integers; everything is mapped to an IF-ELSE statement in this way: <br/>
```
heaps : list # list of heaps
condition : list # list of int
action: tuple # tuple of int
decrease_heap(heap_index, quantity): function
if heap[0] == condition[0] and heap[1] == condition[1] and ... and heaps[n-1] == condition[n-1] then
    decrease_heap(action[0], action[1])
```
Both **conditions** and **actions** are part of the genome; also the **genome size**, that is the number of conditional statements, the **mutation rate** and the **step size** are part of it. The *fitness* is evaluated by testing the strategy against a nim-sum opponent for 100 games: the percentage of victories minus a *penalty* proportional to the *genome size* is the assigned value. The training time varies with the number of heaps, and so the approaches taken to find a suitable solution. **Niching, extinction, step-size adaptation** helped the evolution of a strategy able to compete with nim-sum, although it suffers from *overfitting* when tested against a never seen nim-sum opponent.


## Task 3.3 MinMax
Just a classical implementation of the *minmax decision rule*. A game tree is generated enumerating each possible move in every ply, with a depth limited by a look ahead option. A **heuristic function** evaluates a node based on whether its nim-sum is zero or not, or whether it represents a positive or negative critical situation (where the nim-sum strategy fails to determine the best action). The *minmax strategy* wins against a random one competes against a nim-sum opponent, but only for a look-ahead of 1 ply. This is probably due to the **horizon effect**.
