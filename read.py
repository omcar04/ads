
import heap
import redblack
hp = heap.MinHeap()
rb = redblack.RedBlackTree()

with open('input.txt', 'r') as f, open('output_file.txt', 'w') as output_file:
    for line in f:
        command = line.strip().split('(')
        if command[0] == 'Insert':
            args = command[1][:-1].split(',')
            hp.insert((int(args[0]), int(args[1]), int(args[2])))
            res = rb.insert(int(args[0]), int(args[1]), int(args[2]))
            if res != None:
                output_file.write(str(res) + '\n')
        elif command[0] == 'GetNextRide':
            next_ride = hp.getNextRide()
            rb.cancel(next_ride[0])
            output_file.write(str(next_ride) + '\n')
        elif command[0] == 'Print':
            args = command[1][:-1].split(',')
            if len(args) == 2:
                res = rb.printRides(int(args[0]), int(args[1]))
                output_file.write(str(res) + '\n')
            else:
                res = rb.printRide(int(args[0]))
                output_file.write(str(res) + '\n')
        elif command[0] == 'UpdateTrip':
            args = command[1][:-1].split(',')
            hp.updateTrip(int(args[0]), int(args[1]))
            rb.updateTrip(int(args[0]), int(args[1]))
        elif command[0] == 'CancelRide':
            args = command[1][:-1]
            hp.cancel(int(args))
            rb.cancel(int(args))


