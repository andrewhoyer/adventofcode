# Day 4

Input data is groups of passport data. Each passport is a sequence of key value pairs separated by spaces or newlines. Each passport are separated by a blank lines (two newlines).

Review each passport and count the number of passports that have all of the required fields. 

Required fields:

- byr (Birth Year)
- iyr (Issue Year)
- eyr (Expiration Year)
- hgt (Height)
- hcl (Hair Color)
- ecl (Eye Color)
- pid (Passport ID)


Optional fields:

- cid (Country ID)


[https://adventofcode.com/2020/day/4](https://adventofcode.com/2020/day/4)

```
$ python3 04.py
```

## Part 2

Add additional validation to the passport data check:

- byr (Birth Year) - four digits; at least 1920 and at most 2002.
- iyr (Issue Year) - four digits; at least 2010 and at most 2020.
- eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
- hgt (Height) - a number followed by either cm or in:
	- If cm, the number must be at least 150 and at most 193.
	- If in, the number must be at least 59 and at most 76.
- hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
- ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
- pid (Passport ID) - a nine-digit number, including leading zeroes.
- cid (Country ID) - ignored, missing or not.


```
$ python3 04-b.py
```