# Mini Projet Admninistration système
Projet entierement disponible [ici](https://github.com/fLaVz/monitoringSystem)

## 1. Collecte d'informations

### Bonus

- [x] CPU
- [x] RAM
- [x] Disque Dur
- [x] Utilisateur courant
- [ ] Processus (liste trop longue pour etre mise dans le fichier) 


### Library utilisées
* psutil


## 2. Stockage & Collecte web

### Bonus

- [x] Format standart ".ini"
- [x] Sauvegarde
- [x] L'ajout d'une machine sans changer le code

### Library utilisées

* ConfigParser : pour les fichiers ".ini"
* Re : pour les expressions régulières
* urllib : pour parser le web

## 3. Affichage et Alerte

### Bonus

- [x] Affichage en couleur de certaines infos
- [x] Critères de situation de crise configurable
- [x] Taille maximum de l'historique configurable
- [ ] Contenu de l'email parametrable  
- [x] Envoie des email via le serveur smtp de l'université

### Library utilisées

* smtpLib
* termcolor
* gnuplot

## 4. Communication

### Bonus
- [ ] Module web quireprend les informations du client CLI

### Library utilisées

* flask

# Fonctionnement

Pour lancer le server : 
> python flasker.py

Pour lancer la collecte des infos sur chaque machine :
> python Controleur.py


Le serveur va attendre les requetes des différentes machines.  
Quand il reçoit une requete (les infos d'une machine) il va l'afficher et le stocker dans le dossier correspondant  
> serverLogs/

Les données des rapports sont stockées aussi localement dans :  
> logs/

Tout comme les graphes dans :  
> graph/


Aussi, les sondes font un rapport toutes les 5 secondes (pour les besoins d'un test rapide).  
La boucle de temps peut etre changé dans le Controleur.py -> time.sleep.  