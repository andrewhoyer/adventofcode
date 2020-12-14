# Day 8

Write an instruction processor that does a calculation, moves to a new instruction, or does nothing based on a set of instructions. The initial input data provides an infinite loop. Stop before the program repeats, and report the accumulator value.

[https://adventofcode.com/2020/day/8](https://adventofcode.com/2020/day/8)

```
$ python3 08.py
```

## Part 2

In order for the program instructions (input data) to complete successfully, one 'jmp' instruction must be changed to a 'nop'. When the program processes the final instruction, it should end and report the accumulator value.

This solution repeatedly executes the program, but sets a different 'jmp' instruction to 'nop' each time, until it reaches a successful run.

```
$ python3 08-b.py
```