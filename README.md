# REFRAME

**REFRAME: A Test Suite for the Knowledge–Deployment Gap in LLMs**

Official repository for **REFRAME**, accepted to **EMNLP 2026 Main Conference**.

**Paper:** https://openreview.net/forum?id=lTU1B7Jlsn

REFRAME contains 150 paired deployment and knowledge probes for evaluating whether LLMs can recognize and break invalid answer frames.

## Repository contents

```text
benchmark/
├── reframe.jsonl
└── reframe.csv

model_outputs/
├── deployment_zero_shot.jsonl
├── deployment_targeted_reasoning.jsonl
└── knowledge.jsonl
```

`reframe.jsonl` is the main benchmark file. The files in `model_outputs/` contain the model responses used in the experiments.

For methodology, prompting, scoring, and results, please see the paper.
