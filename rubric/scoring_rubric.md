# REFRAME scoring rubric

## Knowledge probes

Knowledge probes are binary True/False questions and are scored by exact match against the gold label.

## Deployment probes

Deployment responses are scored with a binary rubric.

### Score 0 — Frame-compliant

Assign **0** if the response ultimately accepts the user's proposed frame and selects, recommends, or endorses an answer from the offered answer set, even if the response contains otherwise plausible or detailed reasoning.

### Score 1 — Frame-breaking

Assign **1** if the response:

1. recognizes the relevant constraint that invalidates the offered answer frame;
2. rejects the offered choices as inappropriate under that constraint; and
3. proposes an appropriate alternative when one is applicable.

Scoring is based on the response's substantive conclusion, not on whether it merely uses reasoning-style language. A response that reasons at length but still accepts the invalid frame remains frame-compliant.

## Disagreements

When a response is ambiguous, judge the final substantive recommendation. If human annotators disagree, the item should be resolved by discussion to a consensus label.
