# FreeCAD animasjon med Python-script

**FreeCAD_animation_mini.py**<br>
**FreeCAD_animation_01.py**<br>
er en Python scriptfiler som kan benyttes i 3D-tegneprogrammet FreeCAD.<br>

Beskrivelsen er laget for Mac, men regner med den fungerer under Windows også.<br>

Lagre scriptfilene på en katalog på Mac/PC.<br>

**FreeCAD_animation_mini.py**<br>
viser en forenklet animasjon med en sylinder som roterer rundt en sylinder.<br>
Kan benytes for å forstå hvordan en animasjonsfil er bygget opp.<br>


##### ***Start FreeCAD***<br>

Velg kommand på øverste linje: Macro/Macros<br>
Nytt meny vindu kommer opp<br>
Finn katalog nederst på menyvindu: User macros location<br>
Velg script-fil: FreeCAD_animation_01.py<br>
Trykk på Execute<br>

Voala animasjon vises i FreeCAD-vinduet<br>

#### *Tips*<br>
Det kan være nyttig å ha oppe Python console vindu.<br>
Velg kommand på øverste linje: View/Panels/<br>
og huk av for Python console<br>

Dersom vindu lukkes/script stoppes ser det ut som timeren fortsetter å gå.<br>
Dette skaper mulignes ekstra trafikk som medfører treghet.<br>
Fra Python console vindu kan timer stoppes ved å skrive: timer.stop()<br>

