# utilisation

Cloner le repo :
```
git clone https://github.com/IUT-InTheEnd/analyse.git
```

Aller dans le dossier : analyse/dataset
Glisser tout les datasets disponibles sur le Teams dans le dossier dataset.
Retourner à la racine du projet et lancer le main.py avec python.
**Il y a un bouton dans l'interface pour installer les dépendances.**
**Attention** : si les dépendances ne s'installent pas, il faut les installer manuellement avec pip ou crée un environnement.

Ensuite il faut lancer cleanup pour obtenir les fichiers nettoyés.
Et enfin lancer analysis pour obtenir les analyses.

Si on veut lancer les scripts 1 à 1 :
Il faut aller dans le dossier script :
- Dossier clean : 
    - chaque fichier python nettoie un dataset
- Dossier analyse :
    - chaque fichier python fait une analyse spécifique

## analyse  

analyse de données en vue de la création d'un algorithme de recommendation de musique  


### clonage (non obligatoire)

ce repo utilise [git lfs](https://git-lfs.com/) pour stocker les csv,
pour cloner le repo utilisez :  
`git clone https://github.com/IUT-InTheEnd/analyse.git`  
et pour cloner les csv complets utilisez :  
`git lfs checkout`  
