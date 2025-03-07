import requests
import json
import os
import time
import numpy as np

def load_config():
    """
    Load config file looking into multiple locations
    """
    config_locations = [
        "./_config.env",
        "prompt-eng/_config.env",
        "../_config.env"
    ]
    
    config_path = None
    for location in config_locations:
        if os.path.exists(location):
            config_path = location
            break
    
    if not config_path:
        raise FileNotFoundError("Configuration file not found in any of the expected locations.")
    
    with open(config_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

def create_payload(model, prompt, target="ollama", **kwargs):
    """
    Create the Request Payload for the Model Server
    """
    payload = None
    if target == "ollama":
        payload = {
            "model": model,
            "prompt": prompt, 
            "stream": False,
        }
        if kwargs:
            payload["options"] = {key: value for key, value in kwargs.items()}
    elif target == "ollama":
        payload = {
            "model": model,
            "messages": [ {"role" : "user", "content": prompt } ]
        }
    else:
        print(f'!!ERROR!! Unknown target: {target}')
    return payload

def model_req(payload=None):
    """
    Issue request to the Model Server
    """
    try:
        load_config()
    except:
        return -1, f"!!ERROR!! Problem loading prompt-eng/_config"

    url = os.getenv('URL_GENERATE', None)
    api_key = os.getenv('API_KEY', None)
    delta = response = None

    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    
    print(payload)

    try:
        start_time = time.time()
        response = requests.post(url, data=json.dumps(payload) if payload else None, headers=headers)
        delta = time.time() - start_time
    except:
        return -1, f"!!ERROR!! Request failed! You need to adjust prompt-eng/config with URL({url})"

    if response is None:
        return -1, f"!!ERROR!! There was no response (?)"
    elif response.status_code == 200:
        response_json = response.json()
        if 'response' in response_json:
            result = response_json['response']
        elif 'choices' in response_json:
            result = response_json['choices'][0]['message']['content']
        else:
            result = response_json 
        
        return round(delta, 3), result
    elif response.status_code == 401:
        return -1, f"!!ERROR!! Authentication issue. You need to adjust prompt-eng/config with API_KEY ({url})"
    else:
        return -1, f"!!ERROR!! HTTP Response={response.status_code}, {response.text}"

if __name__ == "__main__":
    MATRIX = np.array([[4, 7], [2, 6]])
    try:
        INVERSE_MATRIX = np.linalg.inv(MATRIX).tolist()
    except np.linalg.LinAlgError:
        INVERSE_MATRIX = "Matrix is singular and cannot be inverted."
    
    PROMPT = f"What is the inverse of the matrix {MATRIX.tolist()}?"
    payload = create_payload(
        target="ollama",   
        model="mistral:latest", 
        prompt=PROMPT, 
        temperature=1.0
    )
    
    time_taken, response = model_req(payload=payload)
    print(response)
    if time_taken: print(f'Time taken: {time_taken}s')
