#!/bin/bash

models=("gpt4" "claude3" "llama7b" "llama13b" "llama70b" "stripedhyena" "mistral")

for model in "${models[@]}"
do
    python3 generate.py --prompt ./prompts/CXL_code_analysis_short.pickle --model "$model" --output_path "./outputs/${model}_analysis_cxl.pickle"
done

# To run the shell, use:
# nohup bash generate_all_cxl_analysis_short.sh > logs/generate_all_cxl.log 2>&1 &