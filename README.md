# **Melomaniac**
**Melomaniac** est un jeu très simple d'utilisation permettant de tester votre culture musicale ! Le principe est très simple, trouvez une chanson dont les paroles comprenne t un certain mot pour engranger le maximum de points !

## Installation
Pour jouer à Melomaniac, téléchargez le dossier complet du jeu

Un unique module externe est nécessaire : **pygame**
>pip install pygame

---

Vous n'avez plus qu'à ouvrir le jeu et profiter de la partie !
>Melomaniac.py

## Comment Jouer ?
Dans le menu principal, vous pouvez régler le niveau de jeu et choisir si vous voulez ou non que des exemples de réponse possible soient affichés
>Icône Options en haut à droite

---

Ensuite, cliquez sur le bouton *JOUER* pour lancer la partie!

Vous n'avez plus qu'à trouver le **titre** d'une chanson comprennant le mot donné dans les paroles, ainsi que son **interprète**!

Validez votre réponse avec le bouton ou la touche *Entrée*

---

Vous remportez **100** points si vous trouvez le titre d'une chanson, **200** si vous avez également l'interprète.

Enchaînez les bonnes réponses pour accumuler un **bonus** de points !
## Comment fonctionne Melomaniac ?
Le jeu fonctionne grâce à une base de données extrèmement riche de plus de... 3600 chansons !
>Mais d'où vient cette base de données ?

La réponse tient en un mot : **SCRAPING** !

---

**Scraping 1** : Récupération des couples (titre / interprète) sur un site dédié au karaoké (https://www.karaoke19.com/listedestitres/francais)

**Scraping 2** : Chanson par chanson, grâce à une simple requête Google ("*titre* *interprète* paroles") récupération des paroles si disponibles sur un des deux sites configurés pour le scraping (https://www.paroles-musique.com/ / https://www.paroles.net/)

*Nécessitant environ une quinzaine de secondes par requête, ce processus s'est étalé sur plusieurs jours ! (15 sec * 3600 titres = **15 heures** !)*

---

Grâce aux données collectées, le programme d'initialisation crée le fichier *Songs* contenant l'ensemble des objets de classe *Song*, chacun contenant les informations relatives à une chanson
## Soutenir le projet

Malgré le temps incalculable passé à soigner les moindres détails de Melomaniac, de la base de données au gameplay en passant par le design, le jeu est encore bien loin d'être parfait.


Malheureusement, il vous arrivera peut-être durant votre expérience de rencontrer un bug ou un oubli dans la base de chansons.

J'en suis désolé, il reste encore de nombreuses amélioration à apporter au programme.

Pour soutenir le projet, n'hésitez surtout pas à me faire part des problèmes que vous avez rencontré, dans la rubrique *Issues* sur Github ou bien par mail

> WilDev142@gmail.com

Je remercie d'avance tous ceux qui prendront le temps de le faire, chacun de vos retours permet d'améliorer Melomaniac !

---

## En vous souhaitant une excellente découverte du projet !
