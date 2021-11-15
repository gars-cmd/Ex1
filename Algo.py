
from Building import Building
from Call import Call
from Elevator import Elevator
import json
import csv
import sys

count0=0
count1=0



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
    

def csvToCall(file):
    listCalls =[]  
    with open(file,'r') as f:
        calls = csv.reader(f)
        for row in calls:
            calld = Call(row[1],row[2],row[3] , 0)
            listCalls.append(calld)
    return listCalls        

def allocateAnElevator(b:Building , c:Call):    #efficient for multiplefloor and multiple elevators
    choosen=0
    if Building.numOfElevators(b)==1:
        return choosen
    else:
        Categories = Building.elevatorsCategories(b)
        
        listOfSpeeder = Categories[0]
        print(len(listOfSpeeder))
        listOfSlower = Categories[1]
        print(len(listOfSlower))
        q = abs((b.minFloor-b.maxFloor)+1)/b.numOfElevators()
        # print(q)
        if abs(int(Call.getSrc(c))-int(Call.getDest(c))) > q*2:
            # print("la")
            global count0,count1
            choosen = count0 % len(listOfSpeeder)
            count0=count0+1
            # print(count0)
        else:
            # print("la bas ")
            choosen = count1 % len(listOfSlower)
            count1 = count1 + 1
            # print(count1)
    # print(choosen)        
    return choosen

if __name__ == "__main__":
    print("coucou")
    fileBuild = sys.argv[1]
    fileCall = sys.argv[2]
    fileOut = sys.argv[3]

    b = jsonToBuilding(fileBuild)
    listCall = csvToCall(fileCall)   
    listUpCall = []
    listDownCall = []
    # for item in listCall:
    #     if (Call.getType(item) == 1):
    #         listUpCall.append(item)
    #     else:
    #         listDownCall.append(item)    
    
    
    for item in listCall:
        allocateAnElevator(b,item)
        
         

        
