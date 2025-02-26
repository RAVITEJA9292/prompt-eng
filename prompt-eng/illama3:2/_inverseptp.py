import numpy as np
from _pipeline import create_payload, model_req

MATRIX = np.array([[4, 7], [2, 6]])

TEMPLATE_BEFORE = "You are a math teacher. Follow the standard method to find the inverse of this matrix:"
TEMPLATE_AFTER = "Provide only the inverse matrix as the final answer."

PROMPT = TEMPLATE_BEFORE + '\n' + str(MATRIX.tolist()) + '\n' + TEMPLATE_AFTER

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
