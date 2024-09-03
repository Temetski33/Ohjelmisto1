def do_something():
    print("Jotain: ")
    return "Tämä on funktion palauttama merkkijono"

return_value = do_something()
print(return_value)

#funktio jolla parametreja (argumentteja)
#parametri muuttuja on käytössä vain funktion sisällä
def say_hello(to):
    #print("Moi " + to)
    return "Moi " + to

say_hello("Matti")
print(say_hello("Matti"))

def create_greetings(to, count):
    greetings = []
    for i in range(1, count+1):
        #print(f"{i}. kerran Moi " + to)
        greetings.append(f"{i}. kertaa moi " + to)
    return greetings

greetings = create_greetings("Jorma", 3)
print(greetings)

#Tässä kaksi vaihtoehtoa printata lista allekkain
#listan kaikkien arvojen käsittely for-silmukalla
for i in range(len(greetings)):
    print(greetings[i])

for greeting in greetings:
    print(greeting)