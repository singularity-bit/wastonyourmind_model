# 🪐 spaCy Project: Programming Languages NER

This project attempts to detect programming languages. The goal of the project is to make a model that could be used generally but it will specifically be used as a sentiment analysis exercise.

We typically compare two models in this project; a pattern matching model and a spaCy NER model.

<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert the data to spaCy's binary format |
| `patternmod` | Generate a named entity recognition model based on rules. |
| `train` | Train a named entity recognition model |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model so it can be installed |
| `show-stats` | Show the statistics that compares both models. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `patternmod` &rarr; `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/admin.jsonl`](https://ibm.box.com/s/rlbkibdb98s1w9k2886po4p35s1n2g6j) | Local | JSONL-formatted training data |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
