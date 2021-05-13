import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Robot:
  def __init__(self):
    self.nbsteps = 200
    self.l = 256/2
    self.phiwheel = 122
    self.stpr1 = Stepper(20, 15, 16, 12,  7,  8, False)
    self.stpr2 = Stepper(9,  11, 10, 22, 27, 17, True)
    
    
class Stepper:
  # requires "import RPi.GPIO as GPIO" and "GPIO.setmode(GPIO.BCM)"
  def __init__(self, pinDir, pinStep, pinSleep, pinM0, pinM1, pinM2, reverse):
    self.pinDir = pinDir
    self.pinStep = pinStep
    self.pinSleep = pinSleep
    self.pinMicrostep = (pinM0, pinM1, pinM2)
    self.dutycycle = 50
    self.microstep = 1
    self.reverse = reverse
    self.resolution =  {1 : (0, 0, 0),
                        2 : (1, 0, 0),
                        4 : (0, 1, 0),
                        8 : (1, 1, 0),
                        16: (0, 0, 1),
                        32: (1, 0, 1)}
    GPIO.setup(self.pinDir, GPIO.OUT)
    GPIO.setup(self.pinStep, GPIO.OUT)
    self.pwm = GPIO.PWM(self.pinStep, 1)
    GPIO.setup(self.pinSleep, GPIO.OUT)
    GPIO.setup(self.pinMicrostep, GPIO.OUT)

    GPIO.output(self.pinMicrostep, self.resolution[self.microstep])
    GPIO.output(self.pinStep, GPIO.LOW)
    GPIO.output(self.pinSleep, GPIO.HIGH)

  def SetMicroStep(self, microstep):
    self.microstep = microstep
    GPIO.output(self.pinMicrostep, self.resolution[self.microstep])
    
  def SetFreqDir(self, freq, dir):
    #self.pwm.ChangeDutyCycle(XXXXXXX)
    self.pwm.ChangeFrequency(freq)
    dir = 1-dir if self.reverse else dir
    GPIO.output(self.pinDir, dir)
    
  def Start(self):
    GPIO.output(self.pinSleep, GPIO.HIGH)
    self.pwm.start(self.dutycycle)
    
  def Stop(self):
    self.pwm.stop()
    GPIO.output(self.pinStep, GPIO.LOW)
    GPIO.output(self.pinSleep, GPIO.LOW)
    
  def Sleep(self, truefalse):
    if truefalse:
      GPIO.output(self.pinSleep, GPIO.LOW)
    else:
      GPIO.output(self.pinSleep, GPIO.HIGH)
       
   
