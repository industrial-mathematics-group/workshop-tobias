# Results

Output of `python analysis/fit_cooling.py data/coffee-cooling.csv`:

```
cooling constant k  = 0.0459 +/- 0.0004 1/min
start temperature   = 86.8 C
half-life of excess = 15.1 min
drinkable (60 C) at = 11.5 min
```

- Newton's law of cooling fits the 21 readings well: ln(T − 21.5 °C) is a straight line in time.
- The difference to room temperature halves every **15 minutes**.
- The coffee reaches **60 °C after about 11.5 minutes**.
- The fitted start temperature (86.8 °C) is within the probe's accuracy of the first reading (85.9 °C).

Limits: one mug, one run, and the room temperature is taken as exact. Evaporation in the first minutes
(see the notes) cools faster than the law predicts, which the fit doesn't model.
