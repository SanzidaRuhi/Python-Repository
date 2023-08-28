#implementation of Priority scheduling
process_queue=[]
n=int(input("enter number of process:"))
for i in range(n):#loop for inserting elements in queue
    process_queue.append([])
    process_queue[i].append(input("enter process name:"))
    process_queue[i].append(int(input("enter arrival time:")))
    process_queue[i].append(int(input("enter burst time:")))
    process_queue[i].append(int(input("enter priority:")))
    print(" ")
process_queue.sort(key=lambda process_queue:process_queue[0])#sort queue using lambda expression
print(process_queue)
print("ProcessName\tArrivalTime\tBurstTime\tPriority")
for i in range(n):
    print(process_queue[i][0],'\t\t',process_queue[i][1],'\t\t',process_queue[i][2],'\t\t',process_queue[i][3])
new_process_queue=[]
for i in range(n):
    if process_queue[i-1][3]>process_queue[i][3]:
        if process_queue[i-1] not in new_process_queue:
            new_process_queue.append(process_queue[i-1])
    else:
        if process_queue[i-1] not in new_process_queue:
            new_process_queue.append(process_queue[i])
for i in range(n):
    if process_queue[i] not in new_process_queue:
        new_process_queue.append(process_queue[i])
print(new_process_queue)
new_process_queue.sort(key=lambda x:x[3])#sorting the list using index 3 value
print(new_process_queue)
waiting_time=0
turn_around_time=0
starting_time=0
sum_waiting_time=0
sum_turn_around_time=0
for i in range(n):#loop for evaluating waiting time and turn around time
    waiting_time=starting_time
    burst=waiting_time+process_queue[i][2]
    turn_around_time=burst-process_queue[i][1]
    starting_time=starting_time+process_queue[i][2]
    sum_waiting_time=sum_waiting_time+waiting_time
    sum_turn_around_time=sum_turn_around_time+turn_around_time
    print("waiting time for ",new_process_queue[i][0]," is ",waiting_time)
    print("turn around time for ",new_process_queue[i][0]," is ",turn_around_time)
average_waiting_time=(sum_waiting_time/n)
print('average waiting time=',average_waiting_time)
average_turn_around_time=(sum_turn_around_time/n)
print('average turn around time:',average_turn_around_time)
#execution of gantt chart
print('gantt chart:')
for i in range(n):
    print(new_process_queue[i][0],'\t',end=' ')
print('')
waiting_time=0
turn_around_time=0
starting_time=0
value=0
print(value,end='')
for i in range(n):
    waiting_time=starting_time
    burst=waiting_time+new_process_queue[i][2]
    turn_around_time=burst-new_process_queue[i][1]
    starting_time=starting_time+new_process_queue[i][2]
    print('.....',burst,end='')
    value=burst