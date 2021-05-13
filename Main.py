import cTrajectory
import cStepper

# Create trajectory
#config = Config()
traj = Trajectory()
traj.CreateSample()
traj.Print()

# Create stepper-command from trajectory
cmdseq = CmdSequence()
cmdseq.ConvertTrajectoryToCmdSequence(traj, config)
cmdseq.Print()

# Process stepper-command by steppers

# shut down
