# Advent of Code 2021

Solutions in Python (and maybe Rust) for [advent of code 2021](https://adventofcode.com/)


## Python

To run python solutions create the required environment and you'll need to retrieve your AoC cookie from your browser and store it either as a token or environment variable to utilise the [AoC Data](https://pypi.org/project/advent-of-code-data/) package.

Find your cookie via your browser after logging in to AoC by opening `Developer Tools>Storage>Cookies` and copying the content of the `session` cookie.

```bash
# either
$ echo "my-amazing-long-12309-token" > ~/.config/aocd/token
# or
$ export AOC_SESSION=my-amazing-long-12309-token
```

```bash
$ conda env create -f environment.yaml

$ conda activate aoc
```

Then run the `main.py` entrypoint file in `python/` passing arguments to specify the day.

```bash
# to get the solution to day1
$ python python/main.py day1
```
