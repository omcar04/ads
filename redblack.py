BLACK = True
RED = False

class Node:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.key = rideNumber
        self.cost = rideCost
        self.time = tripDuration
        self.p = None 
        self.color = RED
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0,0,0)
        self.NIL.color = BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL
        self.rides = set()

    def l_rotate(self, x):
        y = x.right
        x.right = y.left 

        if y.left != self.NIL:
            y.left.p = x
        
        y.p = x.p 

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y 

        y.left = x 
        x.p = y

    def r_rotate(self, x):
        y = x.left 
        x.left = y.right 

        if y.right != self.NIL:
            y.right.p = x

        y.p = x.p 

        if x.p is None:
            self.root = y 
        elif x == x.p.right:
            x.p.right = y 
        else:
            x.p.left = y 

        y.right = x 
        x.p = y


    def insert(self, rideNumber, rideCost, tripDuration):
        # print(self.rides)
        if rideNumber not in self.rides:
            z = Node(rideNumber, rideCost, tripDuration)
            self.rides.add(rideNumber)
            # print((rideNumber, rideCost, tripDuration))
            z.left = self.NIL
            z.right = self.NIL
            y = None
            x = self.root

            while x != self.NIL:
                y = x
                if z.key < x.key:
                    x = x.left 
                else:
                    x = x.right 
            
            z.p = y 
            if y == None:
                self.root = z 
            elif z.key < y.key: 
                y.left = z 
            else:
                y.right = z

            self.insertionFix(z)
        else:
            return "Duplicate RideNumber"

    def insertionFix(self, z):
        while z.p and z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right 
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK 
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p 
                        self.l_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED 
                    self.r_rotate(z.p.p)
            else:
                y = z.p.p.left 
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p 
                        self.r_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED 
                    self.l_rotate(z.p.p)
            if z == self.root:
                break
        self.root.color = BLACK

    def printRide(self, rideNumber):
        node = self.findNode(rideNumber)
        return ((node.key,node.cost,node.time))


    def printRides(self, rideNumber1, rideNumber2):
        stack = []
        res = []
        curr = self.root

        while curr != self.NIL or len(stack) > 0:
            while curr != self.NIL:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if rideNumber1 <= curr.key <= rideNumber2:
                res.append((curr.key, curr.cost, curr.time))

            curr = curr.right
        if not res:
            return (0, 0, 0)
        output_str = ",".join([str(x) for x in res])
        return output_str


    def updateTrip(self, rideNumber, new_tripDuration):
        node = self.findNode(rideNumber)
        if node.key == 0:
            # print("Ride not found.")
            return
        if new_tripDuration <= node.time:
            self.cancel(node.key)
            self.insert(rideNumber, node.cost, new_tripDuration)
        elif node.time < new_tripDuration <= 2 * node.time:
            penalty = 10
            rideCost = node.cost
            new_rideCost = rideCost + penalty
            # print("Ride cancelled with a penalty of 10 on existing ride cost.")
            self.cancel(node.key)
            self.insert(rideNumber, new_rideCost, new_tripDuration)

        elif new_tripDuration > 2 * node.time:
            self.cancel(node.key)
            # print("Ride automatically declined.")



    def cancel(self, k):
        z = self.findNode(k)

        if z == self.NIL:
            return "Key not found!"
        
        self.rides.remove(k)
        y = z
        y_orig_color = y.color 
        
        # case 1
        if z.left == self.NIL:
            x = z.right 
            self.transplant(z, z.right)
        # case 2
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        # case 3
        else:
            y = self.findMin(z.right)
            y_orig_color = y.color
            x = y.right 
            
            if y.p == z:
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            
            self.transplant(z, y)
            y.left = z.left 
            y.left.p = y 
            y.color = z.color 
        
        if y_orig_color == BLACK:
            self.cancelFix(x)

    def cancelFix(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.p.left:
                w = x.p.right
                # type 1
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.l_rotate(x.p)
                    w = x.p.right
                # type 2
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED 
                    x = x.p 
                else:
                    # type 3
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.r_rotate(w)
                        w = x.p.right
                    # type 4
                    w.color = x.p.color 
                    x.p.color = BLACK 
                    w.right.color = BLACK 
                    self.l_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                # type 1
                if w.color == RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.r_rotate(x.p)
                    w = x.p.left
                # type 2
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED 
                    x = x.p 
                else:
                    # type 3
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.l_rotate(w)
                        w = x.p.left
                    # type 4
                    w.color = x.p.color 
                    x.p.color = BLACK 
                    w.left.color = BLACK 
                    self.r_rotate(x.p)
                    x = self.root
        x.color = BLACK

    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v 
        else:
            u.p.right = v
        v.p = u.p 

    def findMin(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def findNode(self, k):
        x = self.root
        while x != self.NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x



# RB = RedBlackTree()
# RB.insert(1, 10, 20)
# RB.insert(2, 5, 30)
# # RB.insert(2, 6, 30)
# RB.insert(4, 3, 15)
# RB.insert(7, 5, 20)
# RB.insert(5, 10, 10)
# # RB.printRide(8)
# # print(RB.printRides(8,9))
# # print(RB.findNode(6).key)
# RB.updateTrip(2,66)
# print(RB.findNode(2))

