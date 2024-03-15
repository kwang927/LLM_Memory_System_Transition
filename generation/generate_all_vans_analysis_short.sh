#!/bin/bash

models=("gpt4" "claude3" "llama7b" "llama13b" "llama70b" "stripedhyena" "mistral")

for model in "${models[@]}"
do
    python3 generate.py --prompt ./prompts/VANS_code_analysis_short.pickle --model "$model" --output_path "./outputs/${model}_analysis_vans.pickle"
done

# To run the shell, use:
# nohup bash generate_all_vans_analysis_short.sh > logs/generate_all_vans.log 2>&1 &