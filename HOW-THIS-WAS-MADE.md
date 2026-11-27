# How this was made

Pretend this is your project. This is what happened, and it's what you will declare in the workshop.

| Files | What happened | Declaration |
|---|---|---|
| `README.md`, this file, `notes/`, `data/` | You wrote the notes and typed in the measurements yourself, no AI. You reread everything. | G0 · H2 · A0 |
| `analysis/` | You asked Claude (Claude Opus 5.5) for a script that fits the cooling law and steered it over a few rounds. You ran it and checked that the numbers make sense, and read the fitting function. | G2 · H1 · A0 |
| `results/` | An AI agent ran the script and wrote the summary on its own. You checked the numbers against the script's output. | G3 · H1 · A0 |
| `paper/` | You wrote the abstract; ChatGPT (GPT Sol) polished the English. You read every sentence afterwards. | G1 · H2 · A0 |

In the workshop:

- The repository's default (the `**` annotation in `SIGNOFF.toml`) is what is true for most files: **G0 · H2 · A0**, with you as reviewer.
- The other three folders are declared with `@IMGAgent signoff`, in your own words.
- Later, have a fresh AI session check `analysis/` and record it as **A1**, with what it found (its findings).
- Optionally, have a different model review `analysis/fit_cooling.py` and record it as **A2**, in the review folder `reviews/`.

> **The story is made up**, so that there is something different to declare in each folder. In reality the whole
> example, notes and data included, was written by Claude for this workshop. That's fine in a throwaway workshop
> repository; in a real one, declare what really happened.
