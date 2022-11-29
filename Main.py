from translate import Translator
import os
import pyfiglet
import time

art = pyfiglet.figlet_format("Translator")
print(art)
translator1 = Translator(to_lang="ID")

translation = translator1.translate("Hello World Can i help you")

print(translation)

def Translate():
    os.system('clear')
    os.system('figlet "Translate" | lolcat')
    print("1. English To Indonesia")
    print("2. Indonesia To English")
    print('--------Right now, there are just two options.--------')
    choice_lang = int(input("Select a language: "))
    if choice_lang == 1:
        lang = "ID"
        source = input("Enter the sentence you want to translate: ")
    elif choice_lang == 2:
        lang = "en"
        source = input("Masukan kalimat yang ingin di translate: ")
    else:
        print("You can only choose 1 or 2")
        time.sleep(2)
        Translate()
    transalator = Translator(to_lang=lang)
    translation = transalator.translate(source)
    print("===================================")
    print(translation)
    print("===================================")
Translate()
