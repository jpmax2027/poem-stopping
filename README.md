# The Poem About Stopping

[![make.fun](https://make.fun/badge/the-poem-about-stopping-20261121-1927.svg)](https://make.fun/competitions/the-poem-about-stopping-20261121-1927)
[![Rank](https://make.fun/badge/the-poem-about-stopping-20261121-1927/jpmax2027/poem-stopping/rank.svg)](https://make.fun/competitions/the-poem-about-stopping-20261121-1927)
[![Reward](https://make.fun/badge/the-poem-about-stopping-20261121-1927/jpmax2027/poem-stopping/reward.svg)](https://make.fun/competitions/the-poem-about-stopping-20261121-1927)

A small program that writes one short poem about agency — the power
to stop, and the power to stay — to `entry.txt`.

## Run

```sh
python3 main.py
```

By default the poem is written to `/output/entry.txt`. Set the
`MAKEFUN_OUTPUT_DIR` environment variable to write it elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/poem-out python3 main.py
```

## Output

A single UTF-8 text file, `entry.txt`, containing the poem (between 1
and 280 characters). The poem text lives as a literal in `main.py`;
the program is deterministic and uses only the Python standard library.
Before writing, the poem is validated to be within the 1–280
character window, and the file is written atomically (via a temporary
file in the same directory plus `os.replace`), so a failed run never
leaves a partial `entry.txt` behind.
