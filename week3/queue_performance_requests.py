from collections import deque

def process_performance_requests(requests):
    dq = deque()
    
    for i in range(len(requests)):
        max = 0
        max_performance = ""
        max_index = 0
        index = 0
        for priority, request in requests:
            if priority > max:
                max = priority
                max_performance = request
                max_index = index - 1
                index -= 1
            else:
                index += 1
        requests.pop(max_index)
        dq.append(max_performance)
    return dq

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))


# Understand
 # create queue
 # iterate through list and pull highest priority add to queue (enqueue) (remove form list as variable and add to queue)
 # return queue

 