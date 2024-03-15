#!/bin/bash

models=("gpt4" "claude3" "llama7b" "llama13b" "llama70b" "stripedhyena" "mistral")

for model in "${models[@]}"
do
    python3 generate.py --prompt ./prompts/code_generation_short.pickle --model "$model" --output_path "./outputs/${model}_code_generation_short.pickle"
done

# To run the shell, use:
# nohup bash generate_all_generation_short.sh > logs/generate_all_generation_short.log 2>&1 &