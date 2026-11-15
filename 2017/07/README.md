# Day 7

[https://adventofcode.com/2017/day/7](https://adventofcode.com/2017/day/7)

## Part 1

```
$ php solve.php data-input.txt
```

Part 1 of this puzzle can be solved without any recursive functions or even with the use of any clever coding. All I did was look for any program that wasn't referenced at any higher point, meaning it was the very bottom program.

## Part 2

```
$ php solve-2.php data-input.txt
```

To solve Part 2, you need to enter the solution to Part 1 in the line: `list_weights('enter_p1_result', 0, '');`.

The output of this will be something like the following, but much larger:

```
% php solve-2.php data-test.txt
      gyxo 61
      ebii 61
      jptl 61
   ugml 251
      pbga 66
      havc 66
      qoyq 66
   padx 243
   IMBALANCE DETECTED name: tknk weight: 243 caller: 
      ktlj 57
      cntj 57
      xhth 57
   fwft 243
   IMBALANCE DETECTED name: tknk weight: 243 caller: 
tknk 778
```

Pipe the output to a text file for ease of searching if you like, but in any case locate the IMBALANCE DETECTED lines. Find the program that is off, and gets its original value from the data, subtract the amount it's off, and you have your answer for Part 2.
