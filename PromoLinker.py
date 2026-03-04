import urllib.parse
import urllib.request
from time import sleep
from sys import stdout

def short_link(url):
    api_url = f"http://tinyurl.com/api-create.php?url={url}"
    try:
        with urllib.request.urlopen(api_url) as response:
            print("\n\033[34m Votre lien a été réduit avec succès ! \033[0m\n")
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"\n \033[31m!!! Échec de la réduction : {e} !!!\033[0m \n")
        return "!! Votre lien n'a pas pu être réduit... !!"

def loading(time , text):
    for i in range(time):
        if i % 3 == 0:
            stdout.write(f"\r \033[33m {text} \033[0m .")
        if i % 3 == 1:
            stdout.write(f"\r \033[33m {text} \033[0m ..")
        if i % 3 == 2:
            stdout.write(f"\r \033[33m {text} \033[0m ...")
        sleep(0.4)
    print()


def loading_init(time):
    loading(time , "Préparation")

def loading_request(time):
    loading(time , "Chargement du lien ... veuillez patienter quelques instants")

def loading_reductor(time):
    loading(time , "Réduction du lien ... veuillez patienter quelques instants")

print()
print("-"*50)
print(f"{'PROMO LINKER v1.0':^50}")
print("-"*50)

print("\n Bienvenue dans ce générateur de \033[34m CODE PROMO \033[0m !")
print("\n Il redirigera vos clients vers un numéro Wathsapp. \n\n")

loading_init(5)

print("\n\n -- Veuillez fournir quelques informations nécessaires --")

num_indicator = input("\n\n * Quel indicateur téléphonique utiliser pour le code promo ? (ex: 229) : ").strip()

base_num = input("\n\n * Vers quel numéro ce Code Promo doit-il rediriger vos clients ? (ex: 0197458520) : ").strip()

code_promo = input("\n\n * Quel nom donner au code promo ? : ").strip()

motif_promo = input("\n\n * Quel est le motif de votre Promotion ? : ").strip()

usable_num = num_indicator + base_num

print()
loading_request(5)

message_promo = f"Bonjour ! Voici votre CODE PROMO : *{code_promo}* --  {motif_promo}"

message_promo_encoded = urllib.parse.quote(message_promo)

lien_promo = f"https://wa.me/{usable_num}?text={message_promo_encoded}"

print(f"\n\n \033[34m ** Votre Code Promo est généré ! \033[0m \n\n ** Lien :  {lien_promo}")

print()
loading_reductor(10)

print(f"** Votre lien promo réduit (il peut transiter par un site intermédiaire): {short_link(lien_promo)}")