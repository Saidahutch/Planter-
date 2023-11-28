questions = [
    "What is the lighting in your or area out of 10?",
    "What is the temperature in your room out of 10?",
    "Do you want to hang your plant of put it on a flat surface, 1 for hang and 2 for surface"
]

#This indicates the begining of the game so the users understand
def begin():
    print("Start quiz")

begin()

#This function introduces the creator of the program, Saida Hutchinson, and gives an overview on what it is.
def introduction():
    print("My name is Saida Hutchinson and I love plants. Planter is a program that will help you find the plants that are perfect for your space.")



tryAgain = True

while tryAgain:

    introduction()

    question1 = questions[ 0 ]

    lighting = int(input( question1 + ": " ))

    if lighting < 5:
        print("Plants that need low light will be good for you, examples of low light plants are Peace Lily's (I have one of my own), Philodendron's, and Pothos. These are all low maintenece and don't need a ton of water. They are also good for people who are new plant parents.")
    else:
        print( "Plants that need bright light will be great for you. Examples of these are Aloe Vera, Sago Palms, and Croton. A thing to know about these plants is that they are also on the harder side to grow, so make sure to be fully prepared to care for their needs")

    temperature = int(input( questions[ 1 ] + ": " ))

    if temperature < 5:
        print("Then plants that do better with cold weather will be good for you. Examples of this are Snake plants, ZZ plants, and Fiddel-leaf Figs.")
    else:
        print( "These plants will do better with warmer temperatures. examples of these plants are, Cacti, Aloe Vera, and Palms." )
    

    surface = int(input( questions[ 2 ] + ": " ))

    if surface < 2:
        print("Since hanging plants are better for you, some examples of those are String of Pearls, English Ivy, and Spider Plant.")
    else:
        print( "If surface plants are better, the plants for you will be like Jade Plants, Philodendrons, and Begonias.")
    

    print( f"{lighting}, {temperature}, {surface}" )


    #print("User said: " + question)
    #lighting = 07

    
        

        
    
    userResponse = input( "Do you want to try again: y/n " )

    if userResponse.lower() == "n":
        tryAgain = False
    
print( "End of program!!! Thank you!!!" )

    









# elif lighting > 10:
#     print(")
# else:
#     print("Plants that need moderate light will be good for you. Examples of these are Spider Plants, Snake Plants, and Boston Ferns. These plants all do well with moderate light rooms but can also take brighter lights.")
# Temperature = (input("What is the temperature of your area?"))
# #print ("User said: " + question)
# #temperature = 10
# if Temperature < 5:
#     print("Then plants that do better with cold weather will be good for you. Examples of this are snake plants, ZZ plants, and Fiddel- leaf Figs.")
# elif Temperature > 10:
#     print("These plants will do better with warmer temperatures. examples of these plants are, Cacti, Aloe Vera, and Palms")
