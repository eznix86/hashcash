import hashcash
import time
difficulty = 18

# validate_time = time.perf_counter_ns()

# token = hashcash.make_token('Denmark', difficulty)
# # print(token)
# print("PoW Duration is: ")
# print((time.perf_counter_ns() - validate_time) // 1000000, "ms")

# validate_time = time.perf_counter_ns()
# difficulty_output = hashcash.verify_token('Denmark', token)
# # print(difficulty_output)
# print(difficulty == difficulty_output)
# print("Verification Duration is: ")
# print((time.perf_counter_ns() - validate_time) // 1000000, "ms")

validate_time = time.perf_counter_ns()

t = hashcash.make_cluster('Denmark', 22)
print(t)

diff = hashcash.verify_cluster('Denmark', t)
print(diff)

print((time.perf_counter_ns() - validate_time) // 1000000, "ms")
