# Make the Judge Laugh in One Line

Entry for the make.fun competition
[Make the Judge Laugh in One Line](https://make.fun/c/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21):
one funny line of 200 characters or fewer, judged head to head on surprise,
tightness, freshness, and clean read-aloud.

![make.fun competition](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)
![rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/cryptokom-tech/make-the-judge-laugh-in-one-line/rank.svg)
![reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/cryptokom-tech/make-the-judge-laugh-in-one-line/reward.svg)

## Entry

> Judge, I don't fear rejection—I've framed so much of it I'm running out of wall.

80 characters. `CANDIDATES.md` records the eight candidate lines and the
local pairwise judging that picked this one.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` (Python standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, asserts the gate (UTF-8, 1-200 characters,
not only whitespace, one line), then reads the file back and asserts the
same gate on what landed.

## License

MIT — see `LICENSE`.
