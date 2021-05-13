import math

class Leg:
    def DefineLeg(self, dist_angle, curbature, printing, speed):
        self.dist_angle = dist_angle
        self.curbature = curbature
        self.printing = printing
        self.speed = speed
        return self
    def InputLegInfo(self):
        self.dist_angle = float(input('Enter distance or angle '))
        self.curbature = float(input('Enter Curbature '))
        self.printing = int(input('Enter 1 if print '))
        self.speed = float(input('Enter Speed '))  
    def PrintLegInfo(self):
        print(self.dist_angle, "\t",self.curbature, "\t", self.printing, "\t", self.speed)

class Trajectory:
    def __init__(self):
        
        self.traj = []
    def AppendLeg(self, dist_angle, curbature, printing, speed):#dist_angle = \u00b0 or mm, curbature=1/mm, printing=01, speed=\u00b0/s or mm/s
        leg = Leg()
        leg.DefineLeg(dist_angle, curbature, printing, speed)
        self.traj.append(leg)      
    def CreateSample(self):
        self.AppendLeg(90, 999, 1, 10) #rotation 90\u00b0
        self.AppendLeg(500, 0, 1, 100) #ligne droite
        self.AppendLeg(500, 1/128, 1, 100) #courbe
    def Print(self):
        for leg in self.traj:
            leg.PrintLegInfo()

class Cmd:
    def abss(self, x):
        return max(abs(x), 0.01)
    def dir_sign(self,x):
        if (x >= 0):
            return 1
        else:
            return 0
    def ConvertLegToCmd(self, leg, r): #leg=class Leg; r=class robot for robot configuration
        self.t = leg.dist_angle/leg.speed
        self.print = leg.printing
        if abs(leg.curbature) == 999:
            print("this is a rotation")
            self.DirL = self.dir_sign(leg.curbature)
            self.DirR = self.dir_sign(-leg.curbature)
            self.FreqL = self.abss(leg.speed*r.nbsteps*r.l/(r.phiwheel*2*math.pi))
            self.FreqR = self.abss(leg.speed*r.nbsteps*r.l/(r.phiwheel*2*math.pi))
        else:
            print("this is a straight line or curve")
            self.DirL = self.dir_sign(leg.speed*(1-leg.curbature*r.l))
            self.DirR = self.dir_sign(leg.speed*(1+leg.curbature*r.l))
            self.FreqL = r.nbsteps/(r.phiwheel*2*math.pi)*self.abss(leg.speed*(1-leg.curbature*r.l))
            self.FreqR = r.nbsteps/(r.phiwheel*2*math.pi)*self.abss(leg.speed*(1+leg.curbature*r.l))
    def PrintCmdInfo(self):
        print(self.t, "\t", self.DirL, "\t", self.FreqL, "\t", self.print, "\t", self.FreqR, "\t", self.DirR)     

        
class CmdSequence:
    def __init__(self):
        self.cmdseq = []
    def ConvertTrajectoryToCmdSequence(self, trajectory, config):
        for leg in trajectory.traj:
            self.CreateAndAppendCmd(leg, config)
    def CreateAndAppendCmd(self, leg, config):
        cmd = Cmd()
        cmd.ConvertLegToCmd(leg, config)
        if len(self.cmdseq)>1: #cumulate t with previous cumul
            cmd.t = cmd.t + self.cmdseq[len(self.cmdseq)-1].t 
        self.cmdseq.append(cmd)
    def Print(self):
        for cmd in self.cmdseq:
            cmd.PrintCmdInfo()
        
