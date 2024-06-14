import random

# This code shows a multiplication problem broken down step by step 
# using successive refinement 

# Generate random 3-digit number (AA) and 2-digit number (BBBB)
AA = random.randint(100,999)
B = random.randint(10,99)
BBBB = B*10 + random.randint(0,9)

# Print the multiplication problem 
print(f"{AA}*{BBBB} = _______")

# Break down the problem into smaller and easier problems 
print(f"(R1) 100*{BBBB} = ?")
print(f"(A1) {AA//10}*{BBBB} = ?")
print(f"(R2) {AA+100}*{BBBB} = ?")
print(f"(A2) ({AA//10}+1)*{BBBB} = ?")
print(f"(R3) {AA}*{B} = ?")
print(f"(A3) {AA}*0 = ?")
print(f"(R4) {AA}*{BBBB} = ?")

