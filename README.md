#FreeCAD animasjon

**FreeCAD_animation_mini.py**
**FreeCAD_animation_01.py**
er en Python scriptfiler som kan benyttes i 3D-tegneprogrammet FreeCAD.

Beskrivelsen er laget for Mac, men regner med den fungerer under Windows også.

Lagre scriptfilene på en katalog på Mac/PC.

**FreeCAD_animation_mini.py**
viser en forenklet animasjon med en sylinder som roterer rundt en sylinder.
Kan benytes for å forstå hvordan en animasjonsfil er bygget opp 


*Start FreeCAD*

Velg kommand på øverste linje: Macro/Macros
Nytt meny vindu kommer opp.
Finn katalog nederst på menyvindu: User macros location
Velg script-fil: FreeCAD_animation_01.py
Trykk på Execute

Voala animasjon vises i FreeCAD-vinduet

*Tips*
Det kan være nyttig å ha oppe Python console vindu.
Velg kommand på øverste linje: View/Panels/
og huk av for Python console

Dersom vindu lukkes/script stoppes ser det ut som timeren fortsetter å gå.
Dette skaper mulignes ekstra trafikk som medfører treghet.
Fra Python console vindu kan timer stoppes ved å skrive: timer.stop()

