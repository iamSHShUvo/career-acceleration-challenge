import time 
from collections import deque

dataset = list(range(10000000))

start_time = time.time()

dataset.pop()

end_time = time.time()

print(f'Pop (End) Time: {end_time - start_time: .5f} seconds')

start_time = time.time()

dataset.pop(0)

end_time = time.time()

print(f'Pop (Start) Time: {end_time - start_time: .5f} seconds')

queue = deque(dataset)

start_time = time.time()

queue.popleft()

end_time = time.time()
print(f'Deque PopLeft Time: {end_time - start_time: .5f} seconds')