from typing import Generator
import Elevator
class Building:

     
    
    def __init__( self  , minFloor:int , maxFloor:int , elevators=[]):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = elevators

    def minFloor(self)->int :
        return self.minFloor

    def maxFloor(self)->int :
        return self.maxFloor

    def numOfElevators(self)->int :
        return self.elevators.__len__() 

    def getElevator(self , i)->Elevator :
        return self.elevators[i]

    



    
