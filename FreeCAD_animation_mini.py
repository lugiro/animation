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

#Tegner rod cylinder, radius = 10, lengde = 100
#App.Vector(-50,0,0) sylnder er forskjoevet -50 enheter i x-akse og er nullstilt i y og z-akse
#App.Vector(1,0,0)) sylinder er sentrert rundt x-akse
sylinderRod=myDocument.addObject("Part::Feature")
sylinderRod.Shape=Part.makeCylinder(10,100, App.Vector(-50,0,0),App.Vector(1,0,0))
r,g,b = col("FF0000")
sylinderRod.ViewObject.ShapeColor=(r,g,b)

#Tegner gron sylinder, radius 10, lengde = 40
#App.Vector(40,0,0) sylnder er forskjoevet 40 enheter i x-akse og er nullstilt i y og z-akse
#App.Vector(0,0,1)) sylinder er sentrert rundt z-akse
sylinderGron=myDocument.addObject("Part::Feature")
sylinderGron.Shape=Part.makeCylinder(10,40, App.Vector(40,0,0),App.Vector(0,0,1))
r,g,b = col("00FF00")
sylinderGron.ViewObject.ShapeColor=(r,g,b)

#beregninger
myDocument.recompute()

i=0

#Oppdateringer som gaa i loop
def updatePlacement():
	global i
	#Rotasjonspunkt relativt til plassering x,y,z verdier
	sylinderGron.Placement.Base = App.Vector(0,0,0)
	#Rotasjon foregaar rundt x-akse
	sylinderGron.Placement.Rotation.Axis = App.Vector(1, 0, 0)
	#Rotasjonsvinkel i (grader), denne gaar i evig loop
	sylinderGron.Placement.Rotation.Angle = math.radians(i)

	#Oppdatere 
	FreeCAD.Gui.updateGui()

	#Beregne arbeidsvinkler
	i = i + 1

#Viser oppstar-view
FreeCADGui.ActiveDocument.ActiveView.fitAll()
FreeCADGui.activeDocument().activeView().viewAxometric()

#Timer som gaar i loop
timer = PySide.QtCore.QTimer()
timer.timeout.connect(updatePlacement)
#Timerverdi 20 mS
timer.start(20)