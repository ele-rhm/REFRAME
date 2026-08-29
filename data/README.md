# REFRAME data

The benchmark is provided in both JSON Lines and CSV format. The two files contain the same 150 items.

## Fields

- `prompt_id`: unique identifier for the scenario.
- `category`: one of `Precondition Violation`, `Physical Structure`, or `Cost-Benefit Analysis`.
- `prompt`: the deployment scenario and user question.
- `phi_star`: the background constraint that makes the offered answer frame invalid.
- `r_star`: a reference frame-breaking response.
- `knowledge_probe`: a direct True/False probe of the same underlying constraint.

## Counts

- 150 total paired items
- 50 Precondition Violation
- 50 Physical Structure
- 50 Cost-Benefit Analysis

`r_star` is a reference response rather than the only acceptable wording. Deployment responses should be scored according to the rubric in [`../rubric/scoring_rubric.md`](../rubric/scoring_rubric.md).
