# ATS-Project

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
Nos scripts fonctionnent avec le strict nécessaire. Tous nos tests ont pu se faire sur des machines Debian 10 vierges.
Ce projet pourrais fonctionner sur d'autres distro mais nous ne le garantissons pas.

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
root@Debian:~# git clone https://github.com/clyhtsuriva/ATS-Project
```

Installez, configurez et lancez la base de données :
```Shell
root@Debian:~# ./ATS-Project/automatisation/BDDAuto.sh
```

Installez, configurez et lancer le serveur web :
```Shell
root@Debian:~# ./ATS-Project/automatisation/apacheAuto.sh
```

Installez, configurez et lancer le sniffer :
```Shell
root@Debian:~# ./ATS-Project/automatisation/
```

## Utilisation
