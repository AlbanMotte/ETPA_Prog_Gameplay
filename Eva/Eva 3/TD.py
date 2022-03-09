class Personnage :
    #contructeur : (_init_)
    def __init__(self, name) :
        self.nom = name
        self.__pv = 100
    def pertePV (self,nombre):
        self.__pv = self.__pv - nombre
        print(self.nom + " perd " + str(nombre) + " PV !")
        if(self.__pv <=0) :
            self.__pv = 0
            print(self.nom + " est mort...")

class Item :
    def __init__ (self, name, qte, power) :
        self.nom = name
        self.__quantite = qte
        self.puissance = power
    def affiche (self) :
        print("Dovah possède" + " " + str(self.__quantite) + " " + str(self.nom))
    def utilisation (self) :
            self.__quantite = self.__quantite - 1
            if (self.puissance >0):
                print ("Dovah utilise" + " " + str(self.nom) + " " + "! Vous régénèrez " + str(self.puissance) + " PV !")
                print ("Il vous reste " + str(self.__quantite) + " " + str (self.nom))
            if (self.puissance <0) :
                print ("Dovah utilise" + " " + str(self.nom) + " " + "! Vous infligez " + str(self.puissance) + " Dégats!")
                print ("Il vous reste " + str(self.__quantite) + " " + str (self.nom))
            if (self.__quantite == 0) :
                print("Vous n'avez plus de " + str(self.nom))

dovah = Personnage("Dovah")
item_1 = Item("Potions de soin", 3, +5)
item_2 = Item("Epée en acier", 1 , -4)
item_3 = Item("Flèches nordiques", 2, -3)

#Inventaire =
Item.affiche (item_1)
Item.affiche (item_2)
Item.affiche (item_3)

#Action =
Item.utilisation  (item_1)
Item.utilisation  (item_2)
Item.utilisation  (item_3)

#boucle = while self.__quantite >0 :