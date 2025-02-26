import numpy as np
from _pipeline import create_payload, model_req

MATRIX = np.array([[4, 7], [2, 6]])

PROMPT = f"""
You are designing a system for computing the inverse of a matrix.
To conduct a thorough requirement analysis, first generate a sequence of sub-questions necessary to define the solution requirements.
After generating sub-questions, answer them step by step.

Example:
1. What conditions determine if a matrix is invertible?
2. What is the standard method for computing the inverse of a 2x2 matrix?
3. How should the system handle singular matrices?
4. What are the computational challenges for large matrices?
5. What format should inputs and outputs follow?
6. what is the inverse of a matrix? 

Now, apply this structured approach to analyze the requirements for the given matrix: {MATRIX.tolist()}.
"""

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
