import cTrajectory
import cStepper

# Create Robot (steppers included)
robot = cStepper.Robot()

# Create trajectory
#config = Config()
traj = cTrajectory.Trajectory()
traj.CreateSample()
traj.Print()

# Create stepper-command from trajectory
cmdseq = cTrajectory.CmdSequence()
cmdseq.ConvertTrajectoryToCmdSequence(traj, robot)
cmdseq.Print()

# Process stepper-command by steppers

# shut down
