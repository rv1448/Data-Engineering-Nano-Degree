from collections import Counter 
import random
ll = [random.randrange(1,7) for i in range(1,200)]
counter = Counter(ll)
for key,count in counter.items():
    print(f'{key:<4}{count}')
