class MinHeap:
    def __init__(self):
        self.heap = []
        self.rides = set()

    def insert(self, node):
        ride_number = node[0]
        if ride_number in self.rides:
            return "Duplicate RideNumber"
        else:
            self.heap.append(node)
            self.rides.add(ride_number)
            self.heapifyUp(len(self.heap) - 1)

    def getNextRide(self):
        if len(self.heap) < 1:
            return "No active ride requests"
        else:
            self.swap(0, len(self.heap) - 1)
            min_node = self.heap.pop()
            self.rides.remove(min_node[0])
            self.heapifyDown(0)
            return min_node

    def cancel(self, rideNumber):
        for idx, ride in enumerate(self.heap):
            if ride[0] == rideNumber:
                self.rides.remove(ride[0])
                self.heap.pop(idx)
                self.heapifyDown(idx)
                break

    def printRide(self, rideNumber):
        for ride in self.heap:
            if ride[0] == rideNumber:
                return ride
        return (0, 0, 0)
            
    def printRides(self, rideNumber1, rideNumber2):
            res = []
            flag = False
            for ride in self.heap:
                if rideNumber1 <= ride[0] <= rideNumber2:
                    res.append(ride)
                    flag = True
            if flag:
                output_str = ",".join([str(x) for x in res])
                return output_str
            else:
                return (0, 0, 0)

    def updateTrip(self, rideNumber, new_tripDuration):
        for index, ride in enumerate(self.heap):
            if ride[0] == rideNumber:
                existing_tripDuration = ride[2]
                if new_tripDuration <= existing_tripDuration:
                    updated_ride = (rideNumber, ride[1], new_tripDuration)
                    self.heap[index] = updated_ride
                    self.heapifyUp(index)
                    self.heapifyDown(index)
                elif existing_tripDuration < new_tripDuration <= 2 * existing_tripDuration:
                    new_ride_cost = ride[1] + 10
                    updated_ride = (rideNumber, new_ride_cost, new_tripDuration)
                    self.heap[index] = updated_ride
                    self.heapifyUp(index)
                    self.heapifyDown(index)
                else:
                    self.heap.pop(index)
                    self.heapifyDown(index)

    def heapifyUp(self, index):
        parent_index = (index - 1) // 2
        if parent_index < 0:
            return
        if self.heap[parent_index][1] > self.heap[index][1] or (self.heap[parent_index][1] == self.heap[index][1] and self.heap[parent_index][2] > self.heap[index][2]):
            self.swap(parent_index, index)
            self.heapifyUp(parent_index)

    def heapifyDown(self, index):
        l_index = 2 * index + 1
        r_index = 2 * index + 2
        min_index = index
        if l_index < len(self.heap) and self.heap[l_index][1] < self.heap[min_index][1]:
            min_index = l_index
        elif l_index < len(self.heap) and self.heap[l_index][1] == self.heap[min_index][1] and self.heap[l_index][2] < self.heap[min_index][2]:
            min_index = l_index
        if r_index < len(self.heap) and self.heap[r_index][1] < self.heap[min_index][1]:
            min_index = r_index
        elif r_index < len(self.heap) and self.heap[r_index][1] == self.heap[min_index][1] and self.heap[r_index][2] < self.heap[min_index][2]:
            min_index = r_index
        if min_index != index:
            self.swap(index, min_index)
            self.heapifyDown(min_index)

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

# heap = MinHeap()

# heap.insert((1, 10, 20))
# heap.insert((2, 5, 30))
# heap.insert((3, 15, 25))
# heap.insert((4, 5, 15))
# heap.insert((5, 10, 10))

# heap.printRides(2, 7)
# heap.print_ride(2)

# heap.getNextRide()
# heap.getNextRide()
# heap.getNextRide()


# rides = [    (1, 20, 30),    (2, 30, 45),    (3, 25, 20),    (4, 15, 50),    (5, 35, 15),    (6, 40, 35),    (7, 10, 25)]

# heap = MinHeap()
# for ride in rides:
#     heap.insert(ride)

# # heap.print_ride(3)
# # heap.printRide(2, 5)
# heap.updateTrip(1, 70)

# heap.printRide(1,5)

# heap.insert((25,98,46))
# heap.getNextRide()
# heap.getNextRide()
# heap.insert((42,17,89))
# heap.insert((9,76,31))
# heap.insert((53,97,22))
# heap.getNextRide()
# heap.insert((68,40,51))
# heap.getNextRide()
# heap.printRides(1,100)
# heap.updateTrip(53,15)
# heap.insert((96,28,82))
# heap.insert((73,28,56))
# heap.updateTrip(9,88)
# heap.getNextRide()
# heap.printRide(9)
# heap.insert((20,49,59))
# heap.insert((62,7,10))
# heap.cancel(20)
# heap.insert((25,49,46))
# heap.updateTrip(62,15)
# heap.getNextRide()
# heap.printRides(1,100)
# heap.insert((53,28,19))
# heap.printRides(1,100)