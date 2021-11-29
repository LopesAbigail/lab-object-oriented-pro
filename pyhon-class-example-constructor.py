class Wagen:
    def __init__(self, modell, jahr, farbe, maxGeschwindigkeit):
        self.modell = modell
        self.jahr = jahr
        self.farbe = farbe
        self.geschwindigkeit = 0
        self.maxGeschwindigkeit = maxGeschwindigkeit

    def drucken(self):
        if self.geschwindigkeit == 0:
            print("%s %s %d"%(self.modell, self.farbe, self.jahr))
        elif self.geschwindigkeit < self.maxGeschwindigkeit:
            print("%s %s fährt mit %d Km/h"%(self.modell, self.farbe, self.geschwindigkeit))
        else:
            print("%s %s fährt zuuuuuuuuu schnell"%(self.modell, self.farbe))
        
    def beschleunigen(self, geschwindigkeit):
        self.geschwindigkeit = geschwindigkeit
        if self.geschwindigkeit > self.maxGeschwindigkeit:
            self.geschwindigkeit = self.maxGeschwindigkeit
        self.drucken()

mein_wagen = Wagen('Ferrari', 1980, 'rot', 120)
