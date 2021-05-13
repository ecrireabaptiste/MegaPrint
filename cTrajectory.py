class Leg:
    def DefineLeg(self, dist_angle, curbature, printing, maxspeed):
        self.__dist_angle = dist_angle
        self.__curbature = curbature
        self.__printing = printing
        self.__maxspeed = maxspeed
        return self
      
    def InputLegInfo(self):
        self.__dist_angle = float(input('Enter distance or angle '))
        self.__curbature = float(input('Enter Curbature '))
        self.__printing = int(input('Enter 1 if print '))
        self.__maxspeed = float(input('Enter Max Speed '))
        
    def PrintLegInfo(self):
        print(self.__dist_angle, self.__curbature, self.__printing, self.__maxspeed)

    def dist_angle(self):
        return self.__dist_angle
    def curbature(self):
        return self.__curbature   
    def printing(self):
        return self.__printing
    def maxspeed(self):
        return self.__maxspeed

class Trajectory:
    def __init__(self):
        Trajectory = []
        
    def CreateSample(self):
        leg = Leg()
        leg.DefineLeg(100, 0, 1, 10)
        Trajectory.append(leg)
        leg.DefineLeg(90, 999, 1, 10)
        Trajectory.append(leg)
        leg.DefineLeg(100, 0, 1, 10)
        Trajectory.append(leg)
        leg.DefineLeg(90, 999, 1, 10)
        Trajectory.append(leg)
        leg.DefineLeg(100, 0, 1, 10)
        Trajectory.append(leg)
        leg.DefineLeg(90, 999, 1, 10)
        Trajectory.append(leg)

    def Print(self):
        for leg in Trajectory:
            leg.PrintLegInfo()

           
