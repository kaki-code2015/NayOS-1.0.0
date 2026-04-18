#include <stdio.h>
#include <time.h>

// Ce programme simule la génération d'une clé de session unique pour le Vault
int main() {
    unsigned long seed;
    printf("--- NAY-OS SECURITY KERNEL (Low-Level) ---\n");
    printf("Instance: SESSION_MANAGER_V1\n\n");

    // On demande un ID à l'utilisateur
    printf("Entrez votre ID Administrateur (chiffres) : ");
    if (scanf("%lu", &seed) != 1) {
        printf("[ERROR] Format ID invalide.\n");
        return 1;
    }

    printf("\n[PROCESS] Génération de la clé de hachage...\n");
    
    // Un peu de "mathématiques de hacker" pour le style
    // On mélange l'ID avec le temps actuel
    unsigned long final_key = (seed * 1234567) ^ (unsigned long)time(NULL);

    printf("------------------------------------------\n");
    printf(" CLÉ DE SESSION GÉNÉRÉE : 0x%lX\n", final_key);
    printf(" STATUT : SÉCURISÉ\n");
    printf("------------------------------------------\n");

    return 0;
}
