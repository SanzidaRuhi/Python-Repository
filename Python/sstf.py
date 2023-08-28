#implementation of Shortest Seek Time First(SSTF) hard disk scheduling algorithm
def SSTF(head, sequence):#function for SSTF
    seek_sequence = []
    seek_operations = 0
    seek_sequence.append(head)
    for i in range(len(sequence)):
        near_num = sequence[min(range(len(sequence)), key=lambda i: abs(sequence[i] - head))]
        if head >= near_num:
            difference = head - near_num
            head = near_num
        if head <= near_num:
            difference = near_num - head
            head = near_num
        sequence.remove(near_num)
        seek_sequence.append(near_num)
    print("Seek Sequence: ", end=" ")
    for i in seek_sequence:
        if i == seek_sequence[len(seek_sequence) - 1]:
            print(i)
        else:
            print(i, " ==> ", end=" ")
    return seek_operations
Number_disk = int(input("Enter the number of disks: "))
if Number_disk > 0:
    head = int(input("Enter initial header position: "))
    while not head in range(Number_disk + 1):
        head = int(input("Please enter valid initial head position: "))
    sequence = []
    sequence = list(map(int, input("Enter the sequence: ").split()))
    for i in sequence:
        if i < 0 or i > Number_disk:
            print("Sequence out of range")
            exit(0)
    seek_operations = SSTF(head, sequence)#calling the function