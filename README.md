# ATS

## Introduction

Analyse du trafic sortant d'un smartphone

Notre but est de pouvoir analyser le trafic sortant d'un smartphone à l'aide d'un sniffer et d'afficher notre analyse sur une interface web.


Ce projet nous fait utiliser (entre autres) les outils suivants :


Web : HTML / CSS / JS / PostgreSQL / Python / Apache2

Analyse des paquets : TCP Dump / PostgreSQL / Shell / Python

Automatisation du déploiement : Shell

Editeurs : Neovim / Nano

OS : Debian 10

Outils de présentation : Google Slides

Outils de gestion : Gantt Project / GitHub

## Installation
Tous nos tests ont pu se faire sur des machines Debian 10 vierges.
Ce projet pourrait fonctionner sur d'autres distro, mais nous ne le garantissons pas.

Nous vous conseillons d'effectuer toutes les prochaines actions en tant que **root** et dans le répertoire ```/root``` :
```Shell
user@Debian:~$ sudo su -
```

Pour aller plus vite, vous pouvez utiliser la commande suivante et ainsi passer directement à l'étape **Utilisation** :
```Shell
root@Debian:~# apt update && apt upgrade && apt install git && git clone https://github.com/clyhtsuriva/ATS && ./ATS/automatisation/deploi.sh
```
***Cette commande peut prendre un certain temps en fonction de votre connexion internet et de votre ordinateur.***


Mettez à jour la liste des paquets :
```Shell
root@Debian:~# apt update
```
Mettez à jour les paquets installés sur le système :
```Shell
root@Debian:~# apt upgrade
```

Installez git, si ce n'est pas déjà fait :
```Shell
root@Debian:~# apt install git
```

Clonez ce dépôt :
```Shell
root@Debian:~# git clone https://github.com/clyhtsuriva/ATS
```

Installez, configurez et lancez :
```Shell
root@Debian:~# ./ATS/automatisation/deploi.sh
```

## Utilisation

À ce point, tout est censé être configuré pour une utilisation optimale.
Vous pouvez maintenant vous connecter sur l'interface web pour voir ce que le sniffer a déjà capté.
Cela est faisable via n'importe quel navigateur web et en tapant **localhost** dans la barre de recherche.

Par défaut, SSL est activé avec un certificat autosigné pour localhost. Vous arriverez donc sur la page suivante :
![Warning: Potential Security Risk Ahead](https://i.imgur.com/EJlqDlV.png)

Il suffira alors d'accepter les risques liés à cette connexion pour accéder au site.

Ensuite, la phase d'authentification :
![Authentication Required](https://i.imgur.com/0lC1BmH.png)

Le login et le mot de passe sont **admin** par défaut. Vous pouvez bien sûr changer cela en modifiant le fichier concerné :
```Shell
root@Debian:~# editor /var/www/.htpasswd
```

La syntaxe pour utiliser le filtre est donnée sur la page **syntaxe**.

**Le reste est assez intuitif.**
La page d'**accueil** contient les 20 derniers paquets enregistrés dans la bdd avec la possibilité de tout affichés.

***Attention, cela peut être très lent s’il y a énormément de paquets réceptionnés.***

Vous avez aussi la possibilité de visualiser uniquement les paquets qui concerne un champ en cliquant dessus.

La page **filtrage** permet d'effectuer un peu plus manuellement une requête SQL, voir **syntaxe**.

***Page qui sera surement enlevée dans le futur à cause de l'injection SQL***

Enfin, on a la page **bilan**. On y trouve les informations "statistiques".
