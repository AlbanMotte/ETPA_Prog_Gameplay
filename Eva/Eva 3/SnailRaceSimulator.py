class Escargot:
    def __init__(self, name, motivation, speed, number, distance ):
        self.__nom = name
        self.__motivation = motivation
        self.__vitesse = speed
        self.__numero = number
        self.__distance = distance
    def getName(self):
        return self.__nom
    def getLook(self):
        return "@" + self.__numero
    def getDistance(self):
        return self.__distance
    def getMotivation(self):
        return self.__motivation
    def avancer(self):
        self.__distance += self.__vitesse
        self.__motivation -= 1
        if self.__motivation < 0:
            self.__motivation = 0
    def motive(self):
        self.__motivation += 1

escargot1 = Escargot("Joe", 2, 4, 1, 0)
escargot2 = Escargot("Mama", 4, 2, 2, 0)

while (escargot1.getDistance() < 10) and (escargot2.getDistance() < 10):
    choix = int(input("Que va faire l'Escargot 1 ? Avancer(1) ? Ou Motiver(2) ?"))
    if (choix == 1) and (escargot1.getMotivation() > 0) :
        escargot1.avancer()
    else :
        escargot1.motive()

    choix = int(input("Que va faire l'Escargot 2 ? Avancer(1) ? Ou Motiver(2) ?"))
    if (choix == 1) and (escargot2.getMotivation() > 0) :
        escargot2.avancer()
    else :
        escargot2.motive()

    print (escargot1.getDistance(), escargot1.getMotivation())
    print (escargot2.getDistance(), escargot2.getMotivation())

if (escargot1.getDistance() > escargot2.getDistance()):
    print("L'Escargot vainqueur n'est nul autre que", escargot1.getName(), "!")
else:
    print("L'Escargot vainqueur n'est nul autre que", escargot2.getName(), "!")