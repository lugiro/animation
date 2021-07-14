from FreeCAD import Base,Placement
import FreeCAD
import Part
from time import sleep
import PySide
import math
import FreeCADGui

#FreeCAD animasjon v.hj.a. Python script

#Funksjon for konvertering fra hex-fargekode til desimalverdi mellom 0 og 1
def col(col_hex):
	r_hex = col_hex[0:2]
	g_hex = col_hex[2:4]
	b_hex = col_hex[4:6]
	#col_fl = 0.0
	col_int_r = int(r_hex, 16)
	col_float_r = float(col_int_r / 255.0)
	col_int_g = int(g_hex, 16)
	col_float_g = float(col_int_g / 255.0)
	col_int_b = int(b_hex, 16)
	col_float_b = float(col_int_b / 255.0)
	return col_float_r,col_float_g,col_float_b

#Definerer nytt dokumnet
App.newDocument()
myDocument=App.ActiveDocument

#Tegne skjoert
skirt1=myDocument.addObject("Part::Feature")
skirt1.Shape=Part.makeCone(35,10,80, App.Vector(0,0,-80),App.Vector(0,0,1))
r,g,b = col("E696E8")
skirt1.ViewObject.ShapeColor=(r,g,b)

#Tegne hode
head1=myDocument.addObject("Part::Feature")
head1.Shape=Part.makeSphere(18, App.Vector(0,0,106), App.Vector(0,0,1))
r,g,b = col("E8A84F")
head1.ViewObject.ShapeColor=(r,g,b)

#Tegne kropp
body1=myDocument.addObject("Part::Feature")
body1.Shape=Part.makeCylinder(10,80, App.Vector(0,0,0),App.Vector(0,0,1))
r,g,b = col("E83844")
body1.ViewObject.ShapeColor=(r,g,b)

#Tegne skulderparti
shoulder1=myDocument.addObject("Part::Feature")
shoulder1.Shape=Part.makeCylinder(10,100, App.Vector(-50,0,80),App.Vector(1,0,0))
r,g,b = col("E83844")
shoulder1.ViewObject.ShapeColor=(r,g,b)

#Tegne venstre overarm
upperarmL=myDocument.addObject("Part::Feature")
upperarmL.Shape=Part.makeCylinder(10,40, App.Vector(40,0,0),App.Vector(0,0,1))
r,g,b = col("E83844")
upperarmL.ViewObject.ShapeColor=(r,g,b)

#Tegne venstre underarm
forearmL=myDocument.addObject("Part::Feature")
forearmL.Shape=Part.makeCylinder(10,40, App.Vector(40,0,0),App.Vector(0,0,1))
r,g,b = col("E8A84F")
forearmL.ViewObject.ShapeColor=(r,g,b)

#Tegne hogre overarm
upperarmR=myDocument.addObject("Part::Feature")
upperarmR.Shape=Part.makeCylinder(10,40, App.Vector(-40,0,0),App.Vector(0,0,1))
r,g,b = col("E83844")
upperarmR.ViewObject.ShapeColor=(r,g,b)

#Tegne hogre underarm
forearmR=myDocument.addObject("Part::Feature")
forearmR.Shape=Part.makeCylinder(10,40, App.Vector(-40,0,0),App.Vector(0,0,1))
r,g,b = col("E8A84F")
forearmR.ViewObject.ShapeColor=(r,g,b)

#beregninger
myDocument.recompute()

i=0
a=1

#Oppdateringer som gaa i loop
def updatePlacement():
	global i
	global k
	global a

	x1 = 40*math.cos(math.radians(i))
	y1 = 40*math.sin(math.radians(i))

	upperarmL.Placement.Base = App.Vector(0,0,80)
	upperarmL.Placement.Rotation.Axis = App.Vector(1, 0, 0)
	upperarmL.Placement.Rotation.Angle = math.radians(i+90)

	forearmL.Placement.Base = App.Vector(0,-x1,-y1+80)
	forearmL.Placement.Rotation.Axis = App.Vector(1, 0, 0)
	forearmL.Placement.Rotation.Angle = math.radians(2*i)

	upperarmR.Placement.Base = App.Vector(0,0,80)
	upperarmR.Placement.Rotation.Axis = App.Vector(1, 0, 0)
	upperarmR.Placement.Rotation.Angle = math.radians(-(i+90))

	forearmR.Placement.Base = App.Vector(0,x1,-y1+80)
	forearmR.Placement.Rotation.Axis = App.Vector(1, 0, 0)
	forearmR.Placement.Rotation.Angle = math.radians(i/2+135)

	#Oppdatere 
	FreeCAD.Gui.updateGui()

	#Beregne rotasjonsvinkel
	if i >= 0 and i <= 90:
		i = i + a
	if i >= 90:
		a = -2
	if i <= 0:
		a = 2

#Viser oppstar-view
FreeCADGui.ActiveDocument.ActiveView.fitAll()
FreeCADGui.activeDocument().activeView().viewAxometric()

#Timer som gaar i loop
timer = PySide.QtCore.QTimer()
timer.timeout.connect(updatePlacement)
timer.start(20)