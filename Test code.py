#v1, v2, v3 = 3, True, "Hello world"

#svar = input("vad heter du? ")

#print("hej", svar )

#print(v1, v2, v3)

#################################################################

#Svar = input("skriv ett tal ")

#x = float(Svar)

#y = x * x

#print("talet i kvadrad är", f"{y:.2f}")

##################################################################

# uppgift 2.4

#svar = input("vad är kvadratens sida:")

#sida = float(svar) 

#y = sida * 4 

#x = sida * sida

#print("omkretsen är:", f"{y:.3f}" ,"arean är:", f"{x:.3f}")

##################################################################

# uppgift 2.5

#varan = input("Vad är varans pris:")

#pris = float(varan)

#moms = 1.25

#betalningmoms = pris * moms - pris
#betalningutan = pris 

#print("Momsen är:", f"{betalningmoms:.3f}", "Varan utan kostar:", f"{betalningutan:.2f}")

################################################################

#  uppgift 10 rea kalkylator

#pris = int(input("vad kostar varan ")) 
#rea = int(input("vad är rean "))

#rea2 = rea / 100
#slutpris = ( 1 - rea2) * pris


#print("varan kostar utan rea: ", pris)
#print("varan kostar med rea: ", slutpris)

################################################################

# Uppgift 14 Cirkel area skillnad

#import math



#cirkel_1_radie = int(input("vad är radien på den första cirkeln "))
#cirkel_2_radie = int(input("vad är radien på den andra cirkeln "))

#area_1 = cirkel_1_radie ** 2 * math.pi
#area_2 = cirkel_2_radie ** 2 * math.pi

#area_skillnad = area_1 - area_2 if area_1 > area_2  else area_2 - area_1

#print("cirkel_1 area ", f"{area_1:.2f}")
#print("cirkel_2 area ", f"{area_2:.2f}")

#print("area skillnaden är ",f"{area_skillnad:.2f}")
###################################################################

# uppgift 15 dice

#import random
#number_of_rolls = 10

#while number_of_rolls > 0:
    #val = input("roll the dice yes/no")
    

    #if val == "yes":
        #d100 = random.randint(1,100)
        #print("resultat på d100 ", d100 )

        #if d100 == 12:
            #print("x = 12")
        #else:
            #print("x ! = 12")
    #else: 
        #print("i guess that's a pass")

    #number_of_rolls = number_of_rolls -1 

###################################################################

#Enkel miniräknare

tal_1 = int(input("Välj ett tal: "))
tal_2 = int(input("Välj ett tal: "))

räknesätt = int(input("välj ett räknesätt, 1 för plus, 2 för minus, 3 för delat, 4 för gånger: "))

if räknesätt == 1:
    print( tal_1 + tal_2 )

elif räknesätt == 2:
    print( tal_1 - tal_2 )

elif räknesätt == 3:
    print( tal_1 / tal_2 )

elif räknesätt == 4:
    print( tal_1 * tal_2 )

else:
    print("felaktigt svar ")