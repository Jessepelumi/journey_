"""
Python has 3 built in standard libraries for queue creation.
- Collections Module (deque)
- Queue Module
- Multiprocessing Module
"""

# Collections Module
from collections import deque
# Queue Module
import queue as q

# create an empty queue with capacity
c_queue = deque(maxlen = 3)

# add an element to the queue
c_queue.append(2)
c_queue.append(4)
c_queue.append(6)
print(c_queue)
"""
Calling the append method on a full queue causes the first element to be deleted and add the new appended value to the end of the queue.
"""

# remove the top element of the queue
c_queue.popleft()
print(c_queue)

# delete all the elements of the queue
c_queue.clear()
print(c_queue)


# create queue with queue module
q_queue = q.Queue(maxsize=3)

# add elements to the queue
q_queue.put(1)
q_queue.put(2)
q_queue.put(3)

print(q_queue.qsize())
print(q_queue.full())

# remove the top element
q_queue.get()