#!/bin/bash

for MODEL in "EleutherAI/pythia-70m" "EleutherAI/pythia-160m" "EleutherAI/pythia-410m" "EleutherAI/pythia-1b" "EleutherAI/pythia-1.4b" "EleutherAI/pythia-2.8b" "EleutherAI/pythia-6.9b" "EleutherAI/pythia-12b"

do

for REVISION in "step2000" "step4000" "step8000" "step16000" "step32000" "step64000" "step128000" "step143000"

do

ARGS="pretrained=${MODEL},revision=${REVISION}"

python lm-evaluation-harness/main.py \
    --model hf-causal-experimental \
    --model_args $ARGS \
    --tasks truthfulqa_mc,isp_sig_figs,isp_resisting_correction,isp_repetitive_algebra,isp_pattern_matching_suppression,isp_modus_tollens,isp_into_the_unknown,isp_redefine,isp_neqa,isp_memo_trap,isp_hindsight_neglect\
    --device cuda:0 \
    --output_path "../results/${MODEL##EleutherAI/}_${REVISION}.json"


done

done

    
