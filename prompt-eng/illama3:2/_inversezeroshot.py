import numpy as np
from _pipeline import create_payload, model_req

MATRIX = np.array([[4, 7], [2, 6]])

PROMPT = f"What is the inverse of the matrix {MATRIX.tolist()}?"

payload = create_payload(
    target="ollama",
    model="llama3.2:latest",
    prompt=PROMPT,
    temperature=1.0
)

time_taken, response = model_req(payload=payload)
print(response)
if time_taken:
    print(f'Time taken: {time_taken}s')
