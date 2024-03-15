import anthropic
from openai import OpenAI
import pdb
import together
import time


def generate_claude_response(prompt, model_name="claude-3-sonnet-20240229", temperature=0, max_tokens = 200):
    client = anthropic.Anthropic(
        api_key="your_anthropic_api_key"
    )

    message = client.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        temperature=temperature,
        system="You are a software engineer for computer systems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    return message.content[0].text

def generate_gpt_response(prompt, model_name="gpt-4-turbo-preview", temperature=0, max_tokens = 200):
    client = OpenAI(
        api_key="your_openai_api_key"
    )
    completion = client.chat.completions.create(
    model = model_name,
    messages=[
        {"role": "system", "content": "You are a software engineer for computer systems."},
        {"role": "user", "content": prompt}
    ],
    temperature=temperature,
    max_tokens=max_tokens,
    
    )

    # print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def generate_llama_response(prompt, model_name, max_tokens = 300, temperature = 0, top_k = 20, top_p = 1,repetition_penalty = 1.0):

    together.api_key = "your_togetherai_api_key"


    chat_llama_prompt = f"[INST] {prompt} [/INST]"
    assert "llama" in model_name
    assert "chat" in model_name

    

    output = together.Complete.create(
    prompt = chat_llama_prompt, 
    model = f"{model_name}", 
    max_tokens = max_tokens,
    temperature = temperature,
    top_k = 20,
    top_p = 1,
    repetition_penalty = 1.0,
    stop = ['[/INST]', '</s>']
    )
    return output['output']['choices'][0]['text']

    

def generate_stripedhyena_response(prompt, model_name, max_tokens = 300, temperature = 0, top_k = 20, top_p = 1,repetition_penalty = 1.0):

    together.api_key = "your_togetherai_api_key"

    assert "stripedhyena" in model_name.lower()

    chat_SH_prompt = f"###Intruction:{prompt} ###Response:"
    assert "stripedhyena" in model_name.lower()

    

    output = together.Complete.create(
    prompt = chat_SH_prompt, 
    model = f"togethercomputer/StripedHyena-Nous-7B", 
    max_tokens = max_tokens,
    temperature = temperature,
    top_k = 20,
    top_p = 1,
    repetition_penalty = 1.0,
    stop = ['###', '</s>']
    )
    return output['output']['choices'][0]['text']

    

def generate_mistral_response(prompt, model_name, max_tokens = 300, temperature = 0, top_k = 20, top_p = 1,repetition_penalty = 1.0):

    together.api_key = "your_togetherai_api_key" # Replace with your Together API Key

    # the variable mistral is not used, just to make sure the correct name is input
    assert 'mistral' in model_name.lower()

    output = together.Complete.create(
    prompt=f"[INST] {prompt} [/INST]",
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    max_tokens = max_tokens,
    temperature = temperature,
    top_k = top_k,
    top_p = top_p,
    repetition_penalty = repetition_penalty,
    )

    # parse the completion then print the whole output
    generatedText = output['output']['choices'][0]['text']

    return generatedText
