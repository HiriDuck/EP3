#vyrobte 5 aut. kazde auto bude mit : auto : barva:"", motor:"",rok: ,karoserie:"".
class Auto():
    def __init__(self,barva,rok,motor,karoserie,tachometr= None):
        #Parametry
        self.barva=barva
        self.rok=rok
        self.__motor=motor
        self.__karoserie=karoserie
        self.__tachometr=tachometr
    #gettry
    def get_motor(self):
        return self.__motor
    def get_karoserie(self):
        return self.__karoserie
    def get_tachometr(self):
        return self.__tachometr
    #settry
    def set_motor(self,motor):
        self.__motor = motor
    #Ostatni metody
    def snizit_tachometr(self,c):
        # c je %
        self.__tachometr *=((100-c)/100)

if __name__ == '__main__':
    a = int(input("zadej tachometr: "))
    b=input("vymenit motor")
    c= int(input("kolik %"))
    #zadavam to auto
    auto1= Auto("zluta","1998","V8","sedan",a)
    # nebo
    auto2 = Auto(barva="cervena",rok="1998",motor="1.8",karoserie="limuzina",)

    print(auto1.barva,auto1.rok,auto1.get_motor(),auto1.get_tachometr(),auto1.get_karoserie())
    auto1.barva = "zelana"
    print(auto1.barva)
    print(auto1.get_motor())
    auto1.set_motor(b)
    auto1.snizit_tachometr(c)
    print(auto1.get_motor())
    print(auto1.get_tachometr())
    d = int(input("kolik aut chccete vyrobit:"))
    barvy=["zluta","modra","oranzova","cervena","zelena"]
    motor=["V8","1.8","1.7","1.6","1.5"]
    roky=["2020","2021","2022","2019","2018"]
    karoserie=["sedan","limuzina","kombi","neco","k"]
    tachometr=[1246547,4178964,1487,24867,5485]
    listaut=[]
    for i in range(0,d,1):
        listaut.append(Auto(barvy[i],motor[i],roky[i],karoserie[i]))
        print("auto: {} ma barvu:{}, motor:{}, rok vydani:{}, karoserije:{}.".format(listaut[i].barva,motor[i],roky[i],karoserie[i],tachometr[i]))
    # for i in range(len(barvy)):
    #     print("auto: {} ma barvu:{}, motor:{}, rok vydani:{}, karoserije:{}.".format(i,barvy[i],motor[i],rok[i],karoserie[i]))
