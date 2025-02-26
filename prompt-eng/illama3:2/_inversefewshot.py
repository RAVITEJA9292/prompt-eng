import numpy as np
from _pipeline import create_payload, model_req

MATRIX = np.array([[4, 7], [2, 6]])

FEW_SHOT_PROMPT = """
You are a math teacher. Follow the matrix inversion method:
Example 1:
Matrix: [[2, 3], [1, 4]]
Inverse: [[0.8, -0.6], [-0.2, 0.4]]

Example 2:
Matrix: [[1, 2], [3, 4]]
Inverse: [[-2, 1], [1.5, -0.5]]

Now, find the inverse of the given matrix.
Matrix: {MATRIX.tolist()}
Provide only the inverse matrix as the final answer.
"""

payload = create_payload(
    target="ollama",
    model="llama3.2:latest",
    prompt=FEW_SHOT_PROMPT,
    temperature=1.0
)

time_taken, response = model_req(payload=payload)
print(response)
if time_taken:
    print(f'Time taken: {time_taken}s')
