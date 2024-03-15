import argparse
import pickle
from tqdm import tqdm
import pdb
from generation_util import generate_claude_response, generate_gpt_response, generate_llama_response, generate_stripedhyena_response, generate_mistral_response



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--prompt", type=str, help="Path to the prompt dict")
    parser.add_argument("--model", type=str, help="Model name")
    parser.add_argument("--output_path", type=str, help="Path to the output file")

    args = parser.parse_args()

    prompt_path = args.prompt
    model_name = args.model
    output_path = args.output_path

    with open(prompt_path, 'rb') as f:
        prompt_dict = pickle.load(f)
    
    model_name2exact_name = {}
    model_name2exact_name['gpt4'] = "gpt-4-turbo-preview"
    model_name2exact_name['claude3'] = "claude-3-sonnet-20240229"
    model_name2exact_name['llama7b'] = "meta-llama/Llama-2-7b-chat-hf"
    model_name2exact_name['llama13b'] = "meta-llama/Llama-2-13b-chat-hf"
    model_name2exact_name['llama70b'] = "meta-llama/Llama-2-70b-chat-hf"
    model_name2exact_name['stripedhyena'] = "togethercomputer/StripedHyena-Nous-7B"
    model_name2exact_name['mistral'] = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    if 'long' in prompt_path and model_name != 'gpt4' and model_name != 'claude3' and model_name != "opus":
        raise ValueError("This is for long promopt, please only use GPT4 or Claude3!")
    
    generation_function = None
    
    if model_name == 'gpt4':
        exact_model_name = model_name2exact_name['gpt4']
        generation_function = generate_gpt_response
    if model_name == 'claude3':
        exact_model_name = model_name2exact_name['claude3']
        generation_function = generate_claude_response
    if 'llama' in model_name:
        exact_model_name = model_name2exact_name[model_name]
        generation_function = generate_llama_response
    if model_name == 'mistral':
        exact_model_name = model_name2exact_name['mistral']
        generation_function = generate_mistral_response
    if model_name == 'stripedhyena':
        exact_model_name = model_name2exact_name['stripedhyena']
        generation_function = generate_stripedhyena_response
    if model_name == 'opus':
        exact_model_name = "claude-3-opus-20240229"
        generation_function = generate_claude_response

    ret = {}

    max_tokens = 400

    if 'long' in prompt_path:
        max_tokens = 4000

    count = 0
    for prompt_key in tqdm(prompt_dict):
        curr_prompt = prompt_dict[prompt_key]
        try:
            output = generation_function(prompt=curr_prompt, model_name=exact_model_name, max_tokens=max_tokens)
        except Exception as e:
            print(str(e))
            print("Error occur")
            output = "Error"
        ret[prompt_key] = output
        count += 1
       

    with open(output_path, 'wb') as f:
        pickle.dump(ret, f)

    print("Done")

