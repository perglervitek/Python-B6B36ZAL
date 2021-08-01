class Node:
    def __init__(self, nextNode, prevNode, data):
        self.nextNode = None
        self.prevNode = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None


class Car:
    def __init__(self, identification, name, brand, price, active):
        self.identification = int(identification)
        self.name = name
        self.brand = brand
        self.price = int(price)
        self.active = active


db = LinkedList()


def init(cars):
    for car in cars:
        add(car)


def add(car):
    if getDatabaseHead() is None:
        db.head = Node(None, None, car)
    elif car.price >= db.head.data.price:
        new = Node(None, None, car)
        current = db.head
        while current.nextNode is not None and current.nextNode.data.price <= car.price:
            current = current.nextNode
        new.nextNode = current.nextNode
        current.nextNode = new
        new.prevNode = current
        if current.nextNode is None:
            new.nextNode.prevNode = new
    else:
        new = Node(None, None, car)
        db.head.prevNode = new
        new.nextNode = db.head
        db.head = new


def updateName(identification, name):
    current = db.head
    while current.data.identification != identification:
        if current.nextNode is None:
            break
        else:
            current = current.nextNode
    if identification == current.data.identification:
        current.data.name = name

def updateBrand(identification, brand):
    current = db.head
    while current.data.identification != identification:
        if current.nextNode is None:
           break
        else:
            current = current.nextNode
    if identification == current.data.identification:
        current.data.brand = brand


def activateCar(identification):
    current = db.head
    while current.data.identification != identification:
        if current.nextNode is None:
            break
        else:
            current = current.nextNode
    if identification == current.data.identification:
        current.data.active = True


def deactivateCar(identification):
    current = db.head
    while current.data.identification != identification:
        if current.nextNode is None:
            break
        else:
            current = current.nextNode
    if identification == current.data.identification:
        current.data.active = False


def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    car = db.head
    price = 0
    while car is not None:
        if car.data.active:
            print(car.data.name)
            price += car.data.price
        car = car.nextNode
    return price


def clean():
    db.head = None

# add(Car(23, 'Octavia2', 'Skoda', 120000, True))
# updateName(1, 'Octavia2015')