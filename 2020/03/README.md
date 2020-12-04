# Day 3

The test data represents a hill of snow (.) and trees (#), which repeats endlessly to the right. Starting at the very top left space, follow a path moving three right and one down until the very bottom row is reached. Along the way, count how many trees are hit.

[https://adventofcode.com/2020/day/3](https://adventofcode.com/2020/day/3)

```
$ python3 03.py
```

## Part 2

Do the same as Part 1, but find the number of trees for paths:

- Right 1, down 1.
- Right 3, down 1.
- Right 5, down 1.
- Right 7, down 1.
- Right 1, down 2.

Multiply the number of trees for each of the paths for the answer.


```
$ python3 03-b.py
```