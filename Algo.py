
from Building import Building
from Call import Call
from Elevator import Elevator
import json
import csv


def jsonToBuilding(file):
    f= open(file)
    data = json.load(f)
    building =Building(minFloor=data["_minFloor"] , maxFloor=data["_maxFloor"] , elevators=data["_elevators"])
    f2 = data["_elevators"]
    list1 = []
    for item in f2:
         list1.append(Elevator(id=item["_id"] , speed=item["_speed"], minFloor=item["_minFloor"] , maxFloor =item["_maxFloor"] , closeTime=item["_closeTime"] , openTime=item["_openTime"] , startTime=item["_startTime"] ,stopTime=item["_stopTime"]))
    building.elevators = list1
    return building
    

def jsonToCall(file):
    listCalls =[]  
    with open(r'Ex1/data/Ex1_input/Ex1_input/Ex1_Calls/Calls_a.csv','r') as f:
        calls = csv.reader(f)
        for row in calls:
            calld = Call(row[1],row[2],row[3])
            listCalls.append(calld)
    return listCalls        


def __main__(fileBuilding , fileCall , fileOut):
    Building = jsonToBuilding(fileBuilding)
    listCalls = jsonToCall(fileCall)
    

b = jsonToBuilding(r'/mnt/c/Users/avido/Documents/Universite/matalot/OOP_2021/Assignments/Ex1/data/Ex1_input/Ex1_input/Ex1_Buildings/B3.json')
print(b.maxFloor)