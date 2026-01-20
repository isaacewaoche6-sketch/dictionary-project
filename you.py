#Q. write a program to create a dictionary mixed languages which include hausa,idoma and yoruba
#   words with value as this english tranction
#   provide user with an option too look it up

mydict = {
    "gashi": "take",
    "zo": "come",
    "ruwa": "waater",
    "nakwana": "good morning",
    "yaro": "good",
    "ecaso": "good afternooon",
    "gbefun": "shift",
    "ania": "thank you",
    "abole": "how are you"
    }


print("options are", mydict.keys())
a= input("enter the hindi word\n")

#none wa kizo
print("the meaning of the word is: ",  mydict.get(a))