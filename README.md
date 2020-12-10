# Snake EPSI

Le mini jeu snake développé par Samuel Platon, Fabien Drapeau, Simon Merceron et Loan Le Mauff.

## Installation

cloner le projet git sur la branche master dans votre IDE.

```git
git clone https://github.com/SamuelPlaton/epsi-python-snake
```

Et installer pygame
```pip install pygame OU pip install -r requirements.txt```

## Utilisation

après avoir ouvert le projet entrer la commande ci dessous pour lancer l'application
```bash
py game.py
```

Une fois le jeu lancé vous arrivez sur un menu demandant de saisir un pseudo.
Une fois celui-ci entré cliquez sur play et la partie se lmance

## Fonctionnement
Le point vert est votre serpent, les points rouges les pommes, les points oranges les malus et les points bleus les bonus.
 
Vous pouvez vous déplacer à l'aide des touches directionnelles afin d'avoir un maximum de score.

Si vous rencontrez un mur vous perdez une vie sachant que vous avez un total de 3 vies.

une fois la partie terminée vous voyez les 10 meilleurs scores enregistrés et avez la possibilité de recommencer ou de quitter le jeu.

## Bonus / Malus

les bonus sont représentés par des points bleus et les malus par des points oranges.

Bonus :
- +500 points
- réduction pendant quelques secondes de la vitesse

Malus :
- -500 points
- augmentation pendant quelques secondes de la vitesse

## Obstacles

Des obstacles apparaîtront de manière aléatoire toutes les 3 pommes mangées
