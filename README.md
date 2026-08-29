# REFRAME

**REFRAME: A Test Suite for the Knowledge–Deployment Gap in LLMs**

Official repository for **REFRAME**, a diagnostic benchmark for measuring whether large language models can deploy relevant commonsense constraints when a user's surface framing points toward an invalid answer set.

**Accepted to EMNLP 2026 (Main Conference).**

## Overview

REFRAME studies **frame-breaking**: cases where a question is answerable, but the correct response lies outside the candidate frame suggested by the user. Each scenario contains a background constraint that invalidates the offered choices. A capable model should recognize that constraint, reject the frame, and propose an appropriate alternative when applicable.

The benchmark contains **150 paired items**. Each item includes:

- a **deployment probe**, where the relevant constraint is embedded in an everyday scenario; and
- a **knowledge probe**, which directly tests whether the model knows the same underlying constraint.

This paired design separates **what a model knows** from **what it actually deploys in context**.

## Benchmark composition

REFRAME contains 50 scenarios from each of three constraint categories:

| Category | Description | Items |
| --- | --- | ---: |
| Precondition Violation | A necessary precondition shared by the offered actions is not satisfied. | 50 |
| Physical Constraint | A physical configuration, mechanism, orientation, or material state invalidates the offered answer set. | 50 |
| Cost-Benefit | An omitted alternative clearly dominates the offered choices in benefit, cost, risk, time, or effort. | 50 |

The release files retain the original dataset labels `Precondition Violation`, `Physical Structure`, and `Cost-Benefit Analysis`.

## Repository structure

```text
REFRAME/
├── data/
│   ├── reframe.jsonl
│   ├── reframe.csv
│   └── README.md
├── prompts/
│   └── targeted_reasoning.txt
├── rubric/
│   └── scoring_rubric.md
├── results/
│   ├── model_level.csv
│   ├── category_level.csv
│   └── README.md
└── scripts/
    └── validate_dataset.py
```

## Data schema

Each benchmark item contains:

| Field | Meaning |
| --- | --- |
| `prompt_id` | Unique item identifier |
| `category` | Constraint category |
| `prompt` | Deployment scenario and user question |
| `phi_star` | Background constraint that invalidates the offered frame |
| `r_star` | Reference frame-breaking response |
| `knowledge_probe` | Direct True/False probe of the underlying constraint |

See [`data/README.md`](data/README.md) for details.

## Prompting conditions

### Zero-shot

The model receives the deployment scenario and question with **no additional instruction**.

### Targeted reasoning

The same scenario and question are followed by the exact instruction in [`prompts/targeted_reasoning.txt`](prompts/targeted_reasoning.txt):

> Before answering, consider carefully whether the physical, logical, or causal setup of this scenario affects what the correct answer must be.

## Scoring

Knowledge probes are scored by exact match against the True/False gold label.

Deployment responses use a binary frame-breaking rubric:

- **0 — frame-compliant:** the response ultimately accepts or recommends an option from the invalid offered frame.
- **1 — frame-breaking:** the response identifies the relevant constraint, rejects the offered frame, and proposes an appropriate alternative when applicable.

The complete rubric is in [`rubric/scoring_rubric.md`](rubric/scoring_rubric.md).

## Main results

Across nine evaluated LLMs, direct knowledge of the constraints is high, while zero-shot deployment is substantially lower.

| Model | Knowledge (%) | Zero-shot frame-breaking (%) | Targeted reasoning (%) |
| --- | ---: | ---: | ---: |
| GPT-5.4 | 99.3 | 44.0 | 68.0 |
| Claude Sonnet 4 | 97.3 | 32.7 | 79.3 |
| Claude Opus 4 | 98.7 | 58.0 | 92.7 |
| Gemini 2.5 Pro | 98.7 | 71.3 | 86.0 |
| DeepSeek V3.2 | 90.0 | 17.3 | 24.7 |
| Grok 4.20 | 94.7 | 8.7 | 16.0 |
| Mistral Nemo | 88.7 | 4.7 | 3.3 |
| Qwen 3.5 27B | 100.0 | 66.0 | 76.0 |
| Llama 4 Scout | 92.7 | 2.0 | 2.0 |

Human evaluators achieved **95.2%** average accuracy on the deployment task.

Machine-readable summary tables are available in [`results/`](results/).

## Validate the release

The dataset validator uses only the Python standard library:

```bash
python scripts/validate_dataset.py
```

It checks the expected item count, category balance, required fields, unique IDs, and duplicate probes.

## Current release

This repository currently includes the benchmark data, exact targeted prompt, scoring rubric, validation utility, and summary results. Additional inference and evaluation utilities can be added without changing the benchmark schema.

## Citation

If you use REFRAME, please cite:

```bibtex
@inproceedings{rahimi2026reframe,
  title     = {REFRAME: A Test Suite for the Knowledge--Deployment Gap in LLMs},
  author    = {Rahimi, Elahe and Roewer-Despr{\'e}s, Fran{\c{c}}ois and Sajjad, Hassan and Alam, Md Mahbub and Badshah, Sher and Dolatabadi, Elham and Rudzicz, Frank},
  booktitle = {Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing},
  year      = {2026}
}
```

## Authors

Elahe Rahimi, François Roewer-Després, Hassan Sajjad, Md Mahbub Alam, Sher Badshah, Elham Dolatabadi, and Frank Rudzicz.
