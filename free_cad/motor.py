import FreeCAD as App
from PySide import QtCore

#retrieve parts:
#These parts must be named exaxtly the same in the FreeCAD model. If more than one part has the same name, the first coincidence will be taken.
Piston = App.ActiveDocument.getObjectsByLabel("PistonFinal")[0]
ConnRod = App.ActiveDocument.getObjectsByLabel("ConnRodFinal")[0]
MainShaft = App.ActiveDocument.getObjectsByLabel("MainShaft")[0]
Balls1 = App.ActiveDocument.getObjectsByLabel("Balls1")[0]
Balls2 = App.ActiveDocument.getObjectsByLabel("Balls2")[0]
CrankShaftSketch= App.ActiveDocument.getObjectsByLabel("CrankShaftAnimationSketch")[0]#Sketch to calculate the kinematics of piston and connecting rod.
Valve1Sketch=App.ActiveDocument.getObjectsByLabel("Valve1CalculationSketch")[0]#Sketch to calculate the kinematics of valve 1 components
Valve2Sketch=App.ActiveDocument.getObjectsByLabel("Valve2CalculationSketch")[0]#Sketch to calculate the kinematics of valve 2 components
Valve1Rod=App.ActiveDocument.getObjectsByLabel("Valve1RodFinal")[0]
Valve2Rod=App.ActiveDocument.getObjectsByLabel("Valve2RodFinal")[0]
SecondaryShaft=App.ActiveDocument.getObjectsByLabel("SecondaryShaft")[0]
ScapeValve=App.ActiveDocument.getObjectsByLabel("ScapeValve")[0]
IntakeValve=App.ActiveDocument.getObjectsByLabel("IntakeValve")[0]
Lever1=App.ActiveDocument.getObjectsByLabel("ExaustValveLeverFinal")[0]

#declare a class to animate the model:
class Animation(object):
    def __init__(self):
        #required global variables
        self.angle = 180.0#The angle starts in 180 deg because of the way the model was created in FreeCAD. The original positions is arbitrary rotated 180 deg at the initial possition.
        self.pistonposs=0#Piston possition
        self.connrodangle=0#Connecting rod angle
        self.valve1rod=0#Valve 1 possition
        self.valve2rod=0#Valve 2 possition
        self.timer = QtCore.QTimer()# a timer
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.my_update)#Connect the timeout signal with my update method.
        self.timer.start(0)#start the timer

    def my_update(self):
        #return the angle to 0 after two revolutions.
        if(self.angle>=900.0):
            self.angle=180.0
        #set the piston-crankshaft sketch angle:
        #To animate the piston, a sketch is used. The rotation angle is set and the piston and connecting rod positions are then read from the same sketch. (the sketch contains the adequate cosntruction geometry and reference constraints)
        CrankShaftSketch.setDatum(6,App.Units.Quantity(str(self.angle)+' deg'))
        #Read the piston possition and the connecting rod angle from the same skech. The same method can be used to animate many different mechanisms.
        self.pistonposs=float(CrankShaftSketch.getDatum(4))
        self.connrodangle=float(CrankShaftSketch.getDatum(5))-180
        #ser the parts possitions:
        MainShaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),-(self.angle-180)), App.Vector(0,0,0))
        Balls1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),-(self.angle-180)/2), App.Vector(0,0,0))
        Piston.Placement=App.Placement(App.Vector(-self.pistonposs-40,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        ConnRod.Placement=App.Placement(App.Vector(-self.pistonposs-40,0,-45), App.Rotation(App.Vector(0,0,1),self.connrodangle), App.Vector(40,0,0))
        SecondaryShaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),(self.angle-180)/2), App.Vector(56,0,0))
        Balls2.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),(self.angle-180)/4), App.Vector(56,0,0))
        #To animate the valves the same method has been used:
        #animate Valve1:
        if((self.angle>=180)and(self.angle<=246)):
            Valve1Sketch.setDatum(25,App.Units.Quantity(str((self.angle-180)/2)+' deg'))
            self.valve1rod=float(Valve1Sketch.getDatum(26))-15
        if((self.angle>246)and(self.angle<=292)):
            Valve1Sketch.setDatum(31,App.Units.Quantity(str((self.angle-180)/2)+' deg'))
            self.valve1rod=float(Valve1Sketch.getDatum(32))-15
        if((self.angle>292)and(self.angle<=360)):
            Valve1Sketch.setDatum(35,App.Units.Quantity(str((self.angle-180)/2)+' deg'))
            self.valve1rod=float(Valve1Sketch.getDatum(36))-15
        #Move parts:
        Valve1Rod.Placement=App.Placement(App.Vector(71+self.valve1rod,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        ScapeValve.Placement=App.Placement(App.Vector(115-self.valve1rod,0,-50-(self.valve1rod/4)), App.Rotation(App.Vector(1,0,0),90), App.Vector(0,0,0))
        Lever1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),(self.valve1rod+0.5)*4), App.Vector(157.5,0,-12.5))
        #animate valve 2:
        if((self.angle>=360)and(self.angle<=426)):
            Valve2Sketch.setDatum(26,App.Units.Quantity(str(180-((self.angle-360)/2))+' deg'))
            self.valve2rod=float(Valve2Sketch.getDatum(33))-15
        if((self.angle>426)and(self.angle<=472)):
            Valve2Sketch.setDatum(29,App.Units.Quantity(str(180-((self.angle-360)/2))+' deg'))
            self.valve2rod=float(Valve2Sketch.getDatum(34))-15
        if((self.angle>472)and(self.angle<=538)):
            Valve2Sketch.setDatum(32,App.Units.Quantity(str(180-((self.angle-360)/2))+' deg'))
            self.valve2rod=float(Valve2Sketch.getDatum(35))-15
        #move parts:
        Valve2Rod.Placement=App.Placement(App.Vector(71+self.valve2rod,0,11), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        IntakeValve.Placement=App.Placement(App.Vector(115-self.valve2rod,0,-50-(-self.valve2rod/4)), App.Rotation(App.Vector(1,0,0),-90), App.Vector(0,0,0))
        #increase the angle:
        self.angle=self.angle+1

    def stop(self):
        self.timer.stop()
        #put all the parts back to the original possition:
        self.angle=180.0
        CrankShaftSketch.setDatum(6,App.Units.Quantity('180.000000 deg'))
        Piston.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        ConnRod.Placement=App.Placement(App.Vector(0,0,-45), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        MainShaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        Balls1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        Valve1Rod.Placement=App.Placement(App.Vector(71,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        SecondaryShaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(56,0,0))
        Balls2.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(56,0,0))
        ScapeValve.Placement=App.Placement(App.Vector(115,0,-50), App.Rotation(App.Vector(1,0,0),90), App.Vector(0,0,0))
        Valve2Rod.Placement=App.Placement(App.Vector(71,0,11), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))
        IntakeValve.Placement=App.Placement(App.Vector(114.998,0,-49.9994), App.Rotation(App.Vector(-1,0,0),90), App.Vector(0,0,0))
        Lever1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(157.5,0,-12.5))

a = Animation() #Start the animation.
#To run the animation simply copy and paste this code into the Python console. To stop the animation call the stop() method by tiping "a.stop()" in the Python console.
