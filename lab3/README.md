## Overview
We use a class ```Nim``` to create, store and decrease the heaps and a class ```Player``` to manage the players of the game. Each strategy implemented is tested in a *match* consisting of *100 games*. To offset the empirical advantage in making the first move, the player who starts first is decided randomly.

## Task 3.1 Nim-Sum
A strategy using the nim-sum technique according to the [nim Wikipedia article](https://en.wikipedia.org/wiki/Nim) that also manages the critical layouts where the nim-sum strategy fails. **It wins roughly 80% of the time against a *random strategy* opponent and 50% of the time against a *nim-sum strategy* one.**

## Task 3.2 Evolutionary Algorithm (v2)
We represented the strategy as a sequence of IF-ELSE statements, consisting in conditions and actions. A condition is a list of integers, an action is a tuple of integers; everything is mapped to an IF-ELSE statement in this way: <br/>
```
heaps : list # list of heaps
condition : list # list of int
action: tuple # tuple of int
decrease_heap(heap_index, quantity): function
if heap[0] == condition[0] and heap[1] == condition[1] and ... and heaps[n-1] == condition[n-1] then
    decrease_heap(action[0], action[1])
```
Both **conditions** and **actions** are part of the genome; also the **genome size**, that is the number of conditional statements, the **mutation rate** and the **step size** are part of it. The *fitness* is evaluated by testing the strategy against a nim-sum opponent for 100 games: the percentage of victories minus a *penalty* proportional to the *genome size* is the assigned value. The training time varies with the number of heaps, and so the approaches taken to find a suitable solution. **Niching, extinction, step-size adaptation** helped the evolution of a strategy able to dominate nim-sum.


## Task 3.3 MinMax
Just a classical implementation of the *minmax decision rule*. A game tree is generated enumerating each possible move in every ply, with a depth limited by a look ahead option. **After that, the nodes are evaluated using a *heuristic value* computed by playing a game against a nim-sum strategy opponent, using as inital state the node's heaps: the inverse of the number of plies is the absolute value, while the sign is positive if the player wins, negative viceversa.** The *minmax strategy* is competitive against a random one and itself, while completely losing against a nim-sum opponent.
