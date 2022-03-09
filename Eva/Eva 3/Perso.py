class Personnage :
    #contructeur : (_init_)
    def __init__(self, name) :
        self.nom = name
        self._pv = 100
    def pertePV (self,nombre):
        self._pv = self._pv - nombre
        print(self.nom + " perd " + str(nombre) + " PV !")
        if(self._pv <=0) :
            self._pv = 0
            print(self.nom + " est mort...")