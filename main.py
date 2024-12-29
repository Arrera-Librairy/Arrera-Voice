from objet.arrera_voice import *

def main():
    av = CArreraVoice(jsonWork("conf/sixConfig.json"))
    av.say("Bonjour, je suis Arrera, votre assistant personnel")
    print("Ecoute en cours...")
    av.listen()
    print(av.getTextMicro())

if __name__ == "__main__":
    main()