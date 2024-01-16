
"""
Example of a Hashcash implementation
for a login process example as a captcha
it can take from 2 to 5 seconds to compute on the client side
and less than 1 second to validate on the server side
"""

import hashlib
import time
import random


difficulty = random.randint(5, 5)
print(f"Difficulty {difficulty} leading zeros")

def generate_challenge(resource):
    timestamp = str(time.time())
    random_value = str(hashlib.sha256(str(time.time()).encode()).hexdigest())
    return f"{resource}-{timestamp}-{random_value}"

def is_valid_hashcash(challenge, counter, difficulty=4):
    hash_result = hashlib.sha256(f"{challenge}-{counter}".encode()).hexdigest()
    return hash_result.startswith("0" * difficulty)

# server logic
resource = "login"
challenge = generate_challenge(resource)
print(f"Challenge: {challenge}")


def compute_hashcash(challenge, difficulty=4):
    counter = 0
    while True:
        hash_result = hashlib.sha256(f"{challenge}-{counter}".encode()).hexdigest()
        if hash_result.startswith("0" * difficulty):
            return counter
        counter += 1


# Assume the challenge is received from the server
# Client computes hashcash

start = time.perf_counter_ns()
client_counter = compute_hashcash(challenge, difficulty=difficulty)
print(f"Hashcash: {client_counter}")

print((time.perf_counter_ns() - start) // 1000000, "ms")

validate_time = time.perf_counter_ns()


# Server Verification
if is_valid_hashcash(challenge, client_counter, difficulty=difficulty):
    print("Hashcash verified. Allowing resource access.")
else:
    print("Hashcash verification failed. Access denied.")

print((time.perf_counter_ns() - validate_time) // 1000000, "ms")
