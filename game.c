#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> // Pour la fonction sleep

// Fonction pour effacer l'écran (marche sur CxxDroid)
void clear_screen() {
    printf("\e[1;1H\e[2J");
}

int main() {
    int secret_code;
    int user_guess;
    int difficulty = 1000; // Code à 4 chiffres

    // Initialisation du générateur de nombres aléatoires
    srand(time(NULL));
    secret_code = rand() % 9000 + difficulty; 

    printf("--- NAY-OS SECURITY CHALLENGE ---\n");
    printf("Connexion au Vault en cours...\n\n");
    sleep(1);

    printf("ATTENTION: Le code d'accès va s'afficher pendant 2 secondes.\n");
    printf("MEMORISEZ-LE !\n\n");
    sleep(2);

    // Affichage du code
    printf("###########################\n");
    printf("##  CODE ACCESS: %d    ##\n", secret_code);
    printf("###########################\n");
    
    fflush(stdout); // Force l'affichage avant le sleep
    sleep(2); // Le code reste 2 secondes

    clear_screen(); // On efface tout !

    printf("--- VERIFICATION D'IDENTITE ---\n");
    printf("Entrez le code d'accès : ");
    
    // On utilise scanf pour lire le nombre
    if (scanf("%d", &user_guess) != 1) {
        printf("\n[ERROR] Entrée invalide. Système verrouillé.\n");
        return 1;
    }

    if (user_guess == secret_code) {
        printf("\n[SUCCESS] Accès accordé au secteur 0x7F.\n");
        printf("Bienvenue, Administrateur.\n");
    } else {
        printf("\n[DENIED] Mauvais code. Alerte envoyée à NayIA.\n");
        printf("Le code correct était: %d\n", secret_code);
    }

    return 0;
}
