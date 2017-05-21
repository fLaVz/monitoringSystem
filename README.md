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