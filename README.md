# Care Assesment Instrument Helper (CAI)

Hilfsprogramm für das Verfassen der Freitexte eines Pflegegutachtens.
### Hintergrund

In Pflegegutachten sind u.a. die Bereiche "Fremdbefunde", "Anamnese", "Befund", "Versorgungssituation", "Beschreibung der Wohnsituation", "Begründung" (im Ergebnisteil) sowie "Prognose" als Freitexte konzipiert. Es gibt noch weitere Freitexte, die aber nicht in jedem Gutachten und insgesamt eher selten vorkommen und daher hier nicht berücksichtigt werden. Weitere Freitexte (z.B. "Medikamente") sind so individuell oder kurz zu fassen, dass Bausteine hier keinen Sinn ergeben.

Die meisten Gutachter*innen nutzen für die genannten Texte zumindest zum Teil Textbausteine, welche aber mühsam aus anderen Dokumenten zusammen kopiert werden müssen. Dies ist fehleranfällig, unpraktisch und unnötig zeitaufwändig. Dieses Programm versucht den Vorgang zu vereinfachen, ohne dabei die Individualität der Texte einzuschränken.

## Nutzererfahrung

Im Benutzerverzeichnis wird unter "Dokumente" ein eigener Ordner für das Programm angelegt. In diesem befindet sich die Optionsdatei, optional eventuelle Logs, sowie zwei Unterordner. In einem Unterordner befinden sich die Dokumente mit den angelegten Textbausteinen, in dem anderen die Speicherdateien für die jeweiligen Gutachten. Dieses werden über 21 Tage gespeichert, ältere Dokumente automatisch gelöscht.

Das Programm speichert alle relevanten Daten alle 60 Sekunden automatisch, ebenso beim ordnungsgemäßen Verlassen des Programms. Es steht auch eine Schaltfläche zum Speichern zur Verfügung (mit Tastaturkürzel "Strg-S"). Beim Öffnen des Programms wird automatisch das letzte Gutachten präsentiert.

### Einrichtung

Zur erstmaligen Vorbereitung und / oder Anpassung der Textbausteine mit der Zeit können entweder Textdokumente (ASCII oder UTF-8 / UTF-16) oder Word-Dokumente eingelesen werden. Dabei kann ausgewählt werden, auf welchen Bereich sich die Datei bezieht. Auf Wunsch können später auch weitere Import-Formate implementiert werden. Diese Dokumente werden Zeile für Zeile eingelesen und jede Zeile als separater Baustein angelegt. Dabei werden die spezielle Zeichenketten (TODO: Zeichenketten benennen) als Platzhalten für Personalpronomen 2. Person Singular genutzt. Die Textbausteine werden vom Programm gespeichert (s.o.) und müssen somit nur einmal angelegt werden. Textbausteine können auch direkt im Programm angelegt oder bearbeitet werden.

Die Textbausteine werden dann in hierarchischen Listen bei jedem Textelement angezeigt. Hierbei können dann zum Beispiel unter dem Baustein für "eine Dusche ist vorhanden" die Unterpunkte "ebenerdige Dusche", "nicht ebenerdige Dusche", "Dusche mit erhöhtem Einstieg" sortiert werden. Dabei die ersten bis zu 15 Zeichen eines Textbausteins sowie die letzten 10 Zeichen mit einem Auslassungszeichen "(...)" getrennt als Namen des Bausteins voreingestellt und in der Liste angezeigt. Die Namen können beliebig verändert werden und müssen nicht einzigartig sein (weder insgesamt noch bezogen auf das aktuelle Textelement).

### Nutzung

Für jedes Gutachten wird ein neues Dokument angelegt. Dieses kann beliebig benannt werden. Beim Speichern wird das Erstellungsdatum- und die Erstellungszeit der Datei automatisch vorgestellt, so dass z.B. auch 2 Gutachten mit dem Titel "GA 1" genutzt werden können (z.B. zwecks Datenschutz).

Am oberen Ende der Oberfläche wird der Titel des aktuellen Gutachtens angezeigt und kann hier auch bearbeitet werden. Daneben kann das Geschlecht des Versicherten ausgewählt werden. Ferner wird hier das Anlagedatum angezeigt.

Die Hauptoberfläche unterteilt sich in mehrere Reiter. Jeder Reiter entspricht einem Textfeld des Gutachtens. Auf den einzelnen Reitern wird links jeweils die hierarchische Ansicht der Textbausteine angezeigt, links die Vorschau des Textes. Aus diesem kann auch der Text direkt kopiert werden. Weiter können in der Textvorschau auch direkt Ergänzungen / Löschungen vorgenommen werden. Textbausteine werden durch einen Doppelklick eingefügt. Ein Einzelklick und ein Klick auf einen (unter der Liste der Bausteine platzierten) Button "Bearbeiten" erlaubt das Bearbeiten eines einzelnen Bausteins. Bausteine können auch in der Liste via Drag&Drop verschoben werden. Hier durchgeführte Änderungen werden fest in den Bausteinen gespeichert. Über den Bearbeiten-Button können Bausteine auch in andere Bereiche verschoben werden. Bei Einfügung von Bausteinen mit Pronomen-Platzhalter werden diese entsprechend der Vorauswahl des Geschlechts in der Vorschau angezeigt.

Es gibt zwei "Betriebsmodi":

- **chronologisch**  
  Hierbei werden die ausgewählten Textbausteine in der Reihenfolge eingeführt, in der sie ausgewählt werden. Es gibt spezielle Bausteine für Zeilenumbruch und "neuer Absatz".
- **Vorlage**  
  Hierbei wird zunächst eine Textvorlage angelegt. Eine Beispielvorlage liegt dem Programm bei, diese kann auch im Programm bearbeitet werden (Im Menü unter "Bearbeiten->Vorlage). In dieser Vorlage werden Einfügemarken und Absätze definiert. Diese Einfügemarken tauchen dann in der hierarchischen Ansicht der Bausteine als oberste Ebene auf. Textbausteine können so direkt den Einfügemarken zugewiesen werden. Die Einfügung erfolgt dann an er Stelle der Marken. Werden mehrere, zu einer Einfügemarke hinzugehören Textbausteine ausgewählt erfolgt die Einfügung in chronologischer Reihenfolge.

Zum Abschluss können dann entweder die Texte aus den jeweiligen Vorschaufenstern kopiert (Button "Kopieren" unter der Vorschau) oder die Texte insgesamt exportiert werden. Hierbei ist der Export in eine gesammelte PDF-Datei (mit Seitenumbruch nach jedem Textteil), in eine gesammelte txt-Datei (mit 5 Zeilenumbrüchen nach jedem Textteil), in einzelne pdf-Dateien oder in einzelne txt-Dateien möglich. Für den Sammelexport kann eine Datei ausgewählt werden, der Standard-Ordner ist in den Optionen vorausgewählt. Für den Sammelexport werden die Dateien in den vorausgewählten Ordner unter der Bezeichnung "Gutachten-Bezeichnung + Feldname" (Beispiel "Gutachten 1 - Anamnese.txt") gespeichert. Eine Export-Art kann vorausgewählt und über den "Export"-Button im Hauptfenster ausgelöst werden. Eine feingliedrige Auswahl (um einmalig anders zu exportieren) ist unter "Datei->Export" möglich.

## Technische Umsetzung

- **Programmiersprache:** Python 3.13.11
- **Dateiformate:**
  - Optionen: XML
  - Vorlage: XML
  - Bausteine: JSON
  - Gutachten: JSON
- **Zielplattform:** Win11 x86 64bit, PE-Datei (.exe)
- **Bibliotheken:**  
  Python Standard  
  customtkinter
