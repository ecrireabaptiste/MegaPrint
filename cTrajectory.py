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
        print(self.dist_angle, self.curbature, self.printing, self.speed)

class Trajectory:
    def __init__(self):
        self.traj = []
    def AppendLeg(self, dist_angle, curbature, printing, speed):
        leg = Leg()
        leg.DefineLeg(dist_angle, curbature, printing, speed)
        self.traj.append(leg)      
    def CreateSample(self):
        self.AppendLeg(90, 999, 1, 10)
        self.AppendLeg(100, 0, 1, 10)   
    def Print(self):
        for leg in self.traj:
            leg.PrintLegInfo()
class Config:
    def __init__(self):
        self.nbsteps = 200
        self.l = 256/2
        self.phiwheel = 122 

class Cmd:
    def abss(self, x):
        return max(abs(x), 0.01)
    def dir_sign(self,x):
        if (x >= 0):
            return 1
        else:
            return 0
    def ConvertLegToCmd(self, leg, c):
        self.t = leg.dist_angle/leg.speed
        self.print = leg.printing
        if abs(leg.curbature) == 999:
            self.DirL = self.dir_sign(leg.curbature)
            self.DirR = self.dir_sign(-leg.curbature)
            self.FreqL = self.abss(leg.speed*c.nbsteps*c.l/(c.phiwheel*2*math.pi))
            self.FreqR = self.abss(leg.speed*c.nbsteps*c.l/(c.phiwheel*2*math.pi))
        else:
            self.DirL = self.dir_sign(leg.speed*(1-leg.curbature*c.l))
            self.DirR = self.dir_sign(leg.speed*(1+leg.curbature*c.l))
            self.FreqL = c.nbsteps/(c.phiwheel*2*math.pi)*self.abss(leg.speed*(1-leg.curbature*c.l))
            self.FreqR = c.nbsteps/(c.phiwheel*2*math.pi)*self.abss(leg.speed*(1+leg.curbature*c.l))
    def PrintCmdInfo(self):
        print(self.DirL, self.FreqL, self.print, self.FreqR, self.DirR)     

        
class CmdSequence:
    def __init__(self):
        self.cmdseq = []
    def ConvertTrajectoryToCmdSequence(self, trajectory, config):
        for leg in trajectory.traj:
            self.Append(leg, config)
    def Append(self, leg, config):
        cmd = Cmd()
        cmd.ConvertLegToCmd(leg, config)
        self.cmdseq.append(cmd)
    def Print(self):
        for cmd in self.cmdseq:
            cmd.PrintCmdInfo()
        
