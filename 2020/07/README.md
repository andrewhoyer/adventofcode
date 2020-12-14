# Day 7

This puzzle contains rules for hundreds of bag colors, and which colors those bags can contain. The problem is to figure out how many bags could eventually contain a 'shiny gold' bag.

The solution requires a recursive function to search the rules for each bag, and the rules for each bag that bag can hold, and so on.

[https://adventofcode.com/2020/day/4](https://adventofcode.com/2020/day/7)

```
$ python3 07.py
```

## Part 2

Use the same puzzle data to determine how may bags are required to fill a "shiny gold" bag.

```
$ python3 07-b.py
```