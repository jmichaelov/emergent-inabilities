# Emergent Inabilities? Inverse Scaling Over the Course of Pretraining
This repository contains the code, results, and statistical analysis scripts for 'Emergent Inabilities? Inverse Scaling Over the Course of Pretraining'.

The experiments in the paper can be run in the following way:

1. Download and install the [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness). This code has been designed to work on v0.3.0.
2. Backup the `__init__.py` file in the `lm_eval/tasks` directory of your Language Model Evaluation Harness.
3. Move/copy the `__init__.py` and `isp_tasks.py` files in the `code/eval_harness_code` directory of this repository into the `lm_eval/tasks` directory of your Language Model Evaluation Harness.
4. Use the `code/full_version.sh` file to run the analyses in the paper (All 8 Pythia models at 8 checkpoints on all 10 multiple-choice Inverse Scaling Prize tasks). Edit line 13 of `code/full_version.sh` to point to the correct location of `main.py` in your Language Model Evaluation Harness installation. The output JSON files will be default be located in the `results` folder of this repository.
5. Run `process_output.py` to combine all results into a single TSV file, `results/all_results.tsv`.
5. Run `StatisticalAnalysis.Rmd` to plot the graph and run the statistical analyses on the accuracy scores that are in the paper.
