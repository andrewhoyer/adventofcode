# Advent of Code API

You can use the Advent of Code API to dynamically create content for private leaderboards. This is especially useful for things like a daily update during any year's December event.

**What you'll need**

* The leaderboard ID. You'll find this in the URL when viewing your private leaderboard.
* The year you want to report data from. This will usually be the current year, but it can be used for any event going back to 2015.
* The session cookie. It's a long string which you can find using browser debug tools. See this [GitHub issue](https://github.com/wimglenn/advent-of-code-wim/issues/1) for a nice screenshot that shows you where to look.

All you need to do now is plug these values into one of the scripts here and start using them.

Please note that it is requested that the Advent of Code API be used no more frequently than every 15 minutes.

## Leaderboard sorted by score

### Python

Use the `leaderboard-by-score.py` script if you want to use the API directly from the command line, on a server, a cron job, etc.

```python3 leaderboard-by-score.py```

Note that the output is formatted with markdown meant for posting to a Discord server. Alter the formatting for whatever your target audience is.

### Zapier

A version of the script is available in `leaderboard-by-score-zapier.py` that is meant to be used in a Zapier Code action. No inputs are necessary, just create the action, select Python, copy and paste the code, and plug in the values at the top of the script.

Note that the output is formatted with markdown meant for posting to a Discord server. Alter the output formatting for whatever the following actions require.

## Solve times

Use the `leaderboard-solve-times.py` script to produce a CSV file, sorted by local score descending, which shows the solve time in minutes for part 1 and 2 of each of the 25 days in an event.

```python3 leaderboard-solve-times.py```
