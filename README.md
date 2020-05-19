# ATS

## Introduction

Analyse du trafic sortant d'un smartphone

Notre but est de pouvoir analyser le trafic sortant d'un smartphone à l'aide d'un sniffer et d'afficher notre analyse sur une interface web.


Ce projet nous fait utiliser (entre autres) les outils suivants :


Web : HTML / CSS / JS / PostgreSQL / Python / Apache2

Analyse des paquets : TCP Dump/PostgreSQL/Shell

Automatisation du déploiement : Shell

Editeurs : Neovim / Nano

OS : Debian 10

Outils de présentation : PowerPoint / Google Slides

Outils de gestion : Gantt Project / GitHub

## Installation
Tous nos tests ont pu se faire sur des machines Debian 10 vierges.
Ce projet pourrait fonctionner sur d'autres distro, mais nous ne le garantissons pas.

Nous vous conseillons d'effectuer toutes les prochaines actions en tant que **root** et dans le répertoire ```/root``` :
```Shell
user@Debian:~$ sudo su -
```

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

Clonez-le ce dépôt :
```Shell
root@Debian:~# git clone https://github.com/clyhtsuriva/ATS
```

Installez, configurez et lancez :
```Shell
root@Debian:~# ./ATS/automatisation/deploi.sh
```

## Utilisation

A ce point, tout est censé être configuré pour une utilisation optimale.
Vous pouvez maintenant vous connecter sur l'interface web pour voir ce que le sniffer a déjà capté.
Cela est faisable via n'importe quel navigateur web et en tapant **localhost**.

Le nom d'utilisateur et le mot de passe sont **admin** par défaut. Vous pouvez biensur changez cela en modifiant le fichier concerné :
```Shell
root@Debian:~# editor /var/www/.htpasswd
```

La syntaxe pour utiliser le filtre est donnée sur la page **syntaxe**.
