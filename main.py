import json
import os
import time
from colorama import Fore, Style, init
import random
from datetime import datetime

# ---------------------------------------------------------
# PROGRAM: NAY-OS (Version 1.0)
# CREATOR: Nayane (N-CLAN)
# DATE: 2026
# LICENCE: Copyright © 2026 Nayane. All Rights Reserved.
# ---------------------------------------------------------
# Toute reproduction ou modification non autorisée est 
# strictement interdite.
# ---------------------------------------------------------


init(autoreset=True)
CONFIG_FILE = "system_vault.json"

# --- 1. OUTILS SYSTÈME ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return None

def save_config(user, password, apps_list):
    data = {
        "admin_user": user, 
        "admin_pass": password,
        "apps_installees": apps_list
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- 2. LES APPLICATIONS ---

def app_vault():
    clear_screen()
    print(Fore.YELLOW + "=== ECOLE VAULT : CIBLES DU JOUR ===")
    print(Fore.WHITE + "1. Sarah   [ ]\n2. Axel    [ ]\n3. Lucas   [ ]")
    input("\nAppuyez sur Entrée...")
    
def mini_jeu_nombre():
    clear_screen()
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    print(Fore.YELLOW + "=== 🎯 TROUVE LE NOMBRE (1-100) ===")
    

    
    while True:
        try:
            essai = input(Fore.WHITE + "\nDevine le nombre : ")
            if essai.lower() == "quitter": break
            
            essai = int(essai)
            tentatives += 1
            
            if essai < nombre_secret:
                print(Fore.CYAN + "C'est plus grand ! ↑")
            elif essai > nombre_secret:
                print(Fore.CYAN + "C'est plus petit ! ↓")
            else:
                print(Fore.GREEN + f"🎉 BRAVO ! Trouvé en {tentatives} coups.")
                time.sleep(2)
                break
        except:
            print(Fore.RED + "Entre un nombre valide ou 'quitter'.")

    
import os

def app_asponestore():
    while True:
        config = load_config()
        apps_installees = config.get("apps_installees", ["Vault", "Store"])
        
        clear_screen()
        print(Fore.BLUE + "=== 📦 ASPONE STORE ===")
        print(Fore.GREEN + Style.DIM + "1. Installer NayIA 1.1")
        print(Fore.GREEN + Style.DIM + "2. Installer 'Trouve le nombre'")
        print(Fore.RED + Style.BRIGHT + "3. Retour")
        
        choix = input(Fore.CYAN + "\nChoix > ")

        if choix == "1":
            if "NayIA" not in apps_installees:
                apps_installees.append("NayIA")
                save_config(config["admin_user"], config["admin_pass"], apps_installees)
                print(Fore.GREEN + "\n[+] Jeu installe !")
            else:
                print(Fore.YELLOW + "\n[!] Deja installe.")
            time.sleep(1)
            
        elif choix == "2":
            if "TrouveNombre" not in apps_installees:
                apps_installees.append("TrouveNombre")
                save_config(config["admin_user"], config["admin_pass"], apps_installees)
                print(Fore.GREEN + "\n[+] Jeu installe !")
            else:
                print(Fore.YELLOW + "\n[!] Deja installe.")
            time.sleep(1)
            
        elif choix == "3":
            print(Fore.YELLOW + "Retour au menu...")
            return # Utilise bien return pour quitter le store
            
def recovery_mode():
    clear_screen()
    config = load_config()
    real_pass = config["admin_pass"]
    
    print(Fore.MAGENTA + "=== 🔓 RÉCUPÉRATION SYSTÈME (ADMIN) ===")
    print(Fore.WHITE + f"Indice : Le mot de passe commence par '{real_pass[0]}'")
    
    old_pass = input("\nEntrez l'ancien mot de passe pour confirmer : ")
    
    if old_pass == real_pass:
        new_pass = input("Entrez le NOUVEAU mot de passe : ")
        save_config(config["admin_user"], new_pass, config["apps_installees"])
        print(Fore.GREEN + "\n[OK] Mot de passe mis à jour !")
    else:
        print(Fore.RED + "\n[!] Échec de vérification.")
    
    time.sleep(2)



def app_nayia():
    # --- CHARGEMENT DU NAYMOD (La nouveauté) ---
    cerveau_mod = {}
    if os.path.exists("nayia1.1.NayMOD"):
        with open("nayia1.1.NayMOD", "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ":" in ligne and not ligne.startswith("#"):
                    cle, valeur = ligne.split(":", 1)
                    if "|" in valeur:
                        cerveau_mod[cle.strip().lower()] = [v.strip() for v in valeur.split("|")]
                    else:
                        cerveau_mod[cle.strip().lower()] = [valeur.strip()]

    try:
        with open("memoire.json", "r") as f:
            memoire = json.load(f)
    except:
        memoire = {}

    clear_screen()
    print(Fore.MAGENTA + "Bonjour ! Je suis NayAI 🤖, ecris /aide")
    print(Style.DIM + "Tape 'stop' pour quitter.")

    while True:
        question = input(Fore.CYAN + "Toi : ").lower().strip()

        # 1. STOP (Ton code)
        if question == "stop":
            print(Fore.MAGENTA + "NayAI : Au revoir !")
            with open("memoire.json", "w") as f:
                json.dump(memoire, f)
            break 

        elif question in cerveau_mod:
            print(Fore.GREEN + "NayAI :", random.choice(cerveau_mod[question]))

        elif question in memoire:
            print(Fore.GREEN + "NayAI :", memoire[question])

        elif "bonjour" in question:
            reponses = ["Bonjour humain !", "Salut ! Comment ça va ?", "Hello ! Ravi de te voir !"]
            print(Fore.GREEN + "NayAI :", random.choice(reponses))

        elif "python" in question:
            reponses = ["Python est un langage de programmation.", "Python est très utilisé pour l'IA.", "Beaucoup de développeurs adorent Python.", "Moi meme je suis fait en Python !"]
            print(Fore.GREEN + "NayAI :", random.choice(reponses))

        elif "nayia" in question:
            reponses = ["Tu parles de moi ? Je suis encore en développement.", "Oui c'est moi !", "Je ne suis pas la meilleure IA mais on peut discuter."]
            print(Fore.GREEN + "NayAI :", random.choice(reponses))

        elif "nayane" in question:
            reponses = ["C'est lui qui m'a créé !", "Oui, c'est mon créateur.", "Grace à lui je peux parler."]
            print(Fore.GREEN + "NayAI :", random.choice(reponses))

        elif "salut" in question:
            reponses = ["Salut !", "Salut à toi aussi !"]
            print(Fore.GREEN + "NayAI :", random.choice(reponses))

        elif "/aide" in question:
            print(Fore.YELLOW + "#Nayane,salut,nayia,python,bonjour")

        # 5. APPRENTISSAGE (Priorité 3 de ton code)
        else:
            print(Fore.WHITE + "NayAI : Je ne connais pas ça. Apprends-moi !")
            nouvelle_reponse = input(Fore.YELLOW + "Quelle réponse je dois donner ? ")
            if nouvelle_reponse.lower() != "annuler":
                memoire[question] = nouvelle_reponse
                print(Fore.GREEN + "NayAI : Merci ! Je vais m'en souvenir.")
                
def app_secret():
    clear_screen()
    config = load_config()
    mdp = config.get("admin_pass", "Inconnu")
    print(Fore.MAGENTA + "=== 🛡️ RECOUVREMENT DE SÉCURITÉ ===")
    print(Fore.WHITE + f"Le mot de passe actuel est : {Fore.YELLOW}{mdp}")
    print(Fore.WHITE + "\nAppuie sur Entrée pour fermer...")
    input()
    
def app_matrix():
    clear_screen()
    print(Fore.GREEN + "Connexion au serveur satellite...")
    time.sleep(1)
    for i in range(20):
        # Génère des chiffres aléatoires pour le look hacker
        import random
        ligne = "".join(random.choice("01 ") for _ in range(60))
        print(Fore.GREEN + ligne)
        time.sleep(0.08)
    print(Fore.GREEN + "\nACCÈS AUTORISÉ. BIENVENUE DANS LE RÉSEAU.")
    input(Fore.WHITE + "\n[Entrée pour sortir du mode Hacker]")

def app_pete():
    clear_screen()
    print(Fore.YELLOW + "💨 BRUIT DE PROUT DÉTECTÉ 💨")
    print(Fore.LIGHTYELLOW_EX + "L'OS vient de lâcher un gaz électronique...")
    print(Fore.WHITE + "Félicitations au petit frère pour cette invention.")
    input("\n[Appuie sur Entrée pour aérer la pièce]")
    
def app_calculatrice():
    while True:
        clear_screen()
        print(Fore.YELLOW + "--- NAY-OS CALC ---")
        print(Fore.WHITE + "(Tape 'q' pour quitter)")
        
        calcul = input(Fore.CYAN + "\nCalcul : ").lower().strip()
        
        if calcul == 'q':
            break
            
        # --- LA MAGIE DE LA CORRECTION AUTOMATIQUE ---
        calcul = calcul.replace('x', '*')  # Change x en *
        calcul = calcul.replace('÷', '/')  # Change ÷ en /
        calcul = calcul.replace(':', '/')  # Change : en /
        calcul = calcul.replace(',', '.')  # Change la virgule en point (pour les décimaux)

        try:
            # eval() fait le calcul mathématique
            resultat = eval(calcul)
            print(Fore.GREEN + f"\nRésultat = {resultat}")
            input(Fore.WHITE + "\n[Entrée]")
            
        except Exception:
            # Si l'utilisateur écrit n'importe quoi, ça ne crash plus !
            print(Fore.RED + "\nErreur : Calcul impossible.")
            time.sleep(1.5)

    
def app_colorama():
    clear_screen()
    print(Fore.RED + "C")
    print(Fore.YELLOW + "O")
    print(Fore.GREEN + "L")
    print(Fore.CYAN + "O")
    print(Fore.BLUE + "R")
    print(Fore.MAGENTA + "A")
    print(Fore.WHITE + "M")
    print(Fore.RED + "A")
    print(Fore.YELLOW + "...")
    time.sleep(1)
    print(Fore.CYAN + "\n🎶 Colorama, la la la la ! 🎶")
    input("\n[Entrée pour revenir au calme]")



def app_anniversaire():
    clear_screen()
    print(Fore.YELLOW + "       (  )   (  )   (  )")
    print(Fore.RED + "        ||     ||     ||")
    print(Fore.WHITE + "      {|^^^^^^^^^^^^^^^^|}")
    print(Fore.MAGENTA + "      {|      29 MAI    |}")
    print(Fore.WHITE + "      {__________________}")
    print(Fore.CYAN + "\n🎂 JOYEUX ANNIVERSAIRE ADMIN ! 🎂")
    input("\n[Entrée pour continuer]")
    
# On crée une liste vide pour stocker les notes au début du programme
# Chaque note sera un petit dictionnaire avec un titre et du texte
mes_notes = [] 

def app_blocnotes():
    while True:
        clear_screen()
        print(Fore.YELLOW + "--- NAY-NOTES v1.0 ---")
        print(Fore.WHITE + "1. Voir mes notes")
        print("2. Créer une nouvelle note")
        print("q. Quitter")
        
        choix = input(Fore.CYAN + "\nOption > ").lower().strip()
        
        if choix == 'q':
            break
            
        elif choix == '2':
            # RÉDIGER UNE NOTE
            titre = input("\nTitre de la note : ")
            contenu = input("Contenu : ")
            mes_notes.append({"titre": titre, "texte": contenu})
            print(Fore.GREEN + "\nNote sauvegardée !")
            time.sleep(1)
            
        elif choix == '1':
            # CHOISIR ET LIRE UNE NOTE
            if not mes_notes:
                print(Fore.RED + "\nAucune note enregistrée.")
                time.sleep(1)
            else:
                print("\n--- Tes Notes ---")
                for i, note in enumerate(mes_notes):
                    print(f"{i+1}. {note['titre']}")
                
                try:
                    num = int(input("\nQuelle note veux-tu lire ? (numéro) : ")) - 1
                    print(Fore.GREEN + f"\n[{mes_notes[num]['titre']}]")
                    print(Fore.WHITE + mes_notes[num]['texte'])
                    input("\n[Entrée pour revenir]")
                except:
                    print(Fore.RED + "Numéro invalide.")
                    time.sleep(1)


                
import os
import sys
import json
import time

# --- FONCTION PARAMÈTRES (RÉINITIALISATION) ---
def app_settings():
    clear_screen()
    print(Fore.RED + "=== ⚙️ PARAMÈTRES SYSTÈME ===")
    print(Fore.WHITE + "1. Réinitialisation d'entreprise (Factory Reset)")
    print(Fore.WHITE + "2. Retour")
    
    choix = input(Fore.CYAN + "\nAction > ")
    
    if choix == "1":
        confirm = input(Fore.RED + "⚠️ Tout supprimer et réinitialiser ? (oui/non) : ").lower()
        if confirm == "oui":
            print(Fore.YELLOW + "\n[!] Nettoyage des données...")
            # On supprime les fichiers pour tout remettre à neuf
            for f in ["system_vault.json", "memoire.json"]:
                if os.path.exists(f):
                    os.remove(f)
            
            print(Fore.GREEN + "RÉINITIALISATION RÉUSSIE. REDÉMARRAGE...")
            time.sleep(2)
            # Relance le script depuis le début
            os.execl(sys.executable, sys.executable, *sys.argv)

def main_apps(username):
    while True:
        config = load_config() # On recharge bien les données
        apps_installees = config.get("apps_installees", ["Vault", "Store"])
        
        clear_screen()
        
        # --- ICI : ON CALCULE ET ON AFFICHE L'HEURE ---
        maintenant = datetime.now().strftime("%H:%M")
        print(Fore.YELLOW + f"[{maintenant}] " + Fore.GREEN + f"=== NAY-OS (Admin: {username}) ===")
        print(Fore.WHITE + "------------------------------")
        
        # ... tes options de menu (1, 2, 3...)

        apps_installees = config.get("apps_installees", ["Vault", "Store"])
        config = load_config()

        clear_screen()
        print(Fore.GREEN + f"=== NAY-OS (Admin: {username}) ===")
        print(Fore.WHITE + "------------------------------")
        print("1. 🔒 Ecole Vault")
        print("2. 📦 AsponeStore")
        print("3. ⚙️ Parametres")
        print("4. 📟 Calculatrice")
        print("5. 📒 Bloc-notes")
        
        # On initialise la map avec les apps de base
        menu_map = {
            "1": app_vault,
            "2": app_asponestore,
            "3": app_settings,
            "4": app_calculatrice,
            "5": app_blocnotes,
            "secret": app_secret,
            "29M": app_anniversaire,
            "pete": app_pete,
            "matrix": app_matrix,
            "colorama": app_colorama
        }
        
        idx = 6
        # On ajoute NayIA si elle est installée
        if "NayIA" in apps_installees:
            print(f"{idx}. 🤖 NayIA 1.1")
            menu_map[str(idx)] = app_nayia
            idx += 1
            
        # On ajoute le Jeu s'il est installé
        if "TrouveNombre" in apps_installees:
            print(f"{idx}. 🎯 Trouve le Nombre")
            menu_map[str(idx)] = mini_jeu_nombre # BIEN VERIFIER LE NOM DE TA FONCTION JEU
            idx += 1
            
        print(f"{idx}. 🚪 Eteindre")
        print(Fore.WHITE + "------------------------------")
        
        choix = input(Fore.CYAN + f"C:\\Users\\{username}> ").strip()

        # --- LOGIQUE DE SELECTION UNIQUE ---
        if not choix:
            continue
            
        if choix in menu_map:
            menu_map[choix]() # Lance l'appli correspondante
        elif choix == str(idx):
            print(Fore.RED + "Arret en cours...")
            break
        else:
            print(Fore.RED + "Erreur : Commande inconnue.")
            time.sleep(1)

# --- 4. DÉMARRAGE ---

def start_os():
    config = load_config()
    if config is None:
        print(Fore.CYAN + "=== CONFIGURATION INITIALE ===")
        u = input("Nom d'Admin : ")
        p = input("Mot de passe : ")
        # On initialise avec Vault et Store par défaut
        save_config(u, p, ["Vault", "Store"])
        print("Système configuré ! Relancez l'OS.")
    else:
        u_input = input("Utilisateur : ")
        p_input = input("Mot de passe : ")
        if u_input == config["admin_user"] and p_input == config["admin_pass"]:
            main_apps(config["admin_user"])
        else:
            print(Fore.RED + "Accès refusé.")

if __name__ == "__main__":
    start_os()
