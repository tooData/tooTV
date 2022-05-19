# tooTV
# Test de recrutement datascientist 


# Contexte

Ce test a pour but de vous mettre dans un cas concret que vous pourrez rencontrer
et voir comment vous abordez le sujet. Il n'y a pas de réponse ou méthode parfaite.
Si vous regardez les tests sur les valeurs attendues, nous avons mis des tranches 
assez larges. Ce test n'est pas éliminatoire

L'idée est d'évaluer vos capacités sur les points suivants:
- analyse d'un problème et compréhension des objectifs 
- maitrise de python
- maitrise des bases de SQL
- manipulation de données en python
- force de proposition d'une solution à un problème data

# Description du cas
Imaginons qu'un site de ecommerce diffuse des spots tv lors d'une campagne publicitaire.
Ce site commande un certain nombre de spots à un annonceur (à un prix donné) qui gère les achats
auprès des chaînes de télé.
Une fois la campagne passée, l'annonceur communique au site les heures de diffusion des spots.
Ainsi, en comparant ces heures avec les pics de trafic sur sa page web, le site de
ecommerce peut mesurer l'impact de chaque spot sur le nombre de visites et calculer
la rentabilité du spots (nombre de visites/prix du spot).
Les horaires de diffusion communiqués ne sont pas très précis et il faut procéder à
un recalage de l'horaire du spot par rapport au pic des visites observées sur le site.

# objectifs

Votre tâche sera de mesurer l'impact de chaque spot sur le nombre de visiteurs supplémentaires
induits (l'incrément) à 5 ou 10 min après le spot.

Vous commencerez par coder une fonction détectant le pic : src.impact_analysis.compute_date_spike
Vous coderez ensuite la fonction permettant de calculer l'incrément de visiteurs
pour chaque spot, à 5 ou 10 min selon la méthode que vous jugerez la plus pertinente: src.impact_analysis.compute_increment

Ensuite il faudra définir la fonction src.impact_analysis.compute_campaign_stats dont le rôle est de resumer
les performances de la campagne (nombre de spots, cout total, incrément total à 5 /10 min et cout par visite supplémentaire)

Et pour terminez vous ferez le fichier qui execute ces deux fonctions dans ./analysis.py et sort
ces deux petits dataframe. Vous les collerez dans un excel que vous commenterez avec une ou deux phrases.

#Pour aller plus loin 
Imaginons que ce site de ecommerce dispose d'un historique de milliers de spots avec leur efficacité
mesurée. Selon vous, que pourrait-il faire de ces données et comment, pour améliorer les campagnes suivantes.
Ecrivez quelques lignes sur comment vous feriez.


## LE PROJET

# Description des données

Le projet vient avec des scripts créant une base de données sqlite à partir de deux fichiers csv:
- too_spots_infos: infos des spots avec la date de diffusion et son prix
- visites_minutes: contient les visites par minute sur le site dans un lapse de temps 
autour de chaque spot disponible dans too_spots_infos.

La base de données contient donc deux table. Une avec les horaires de diffusion annoncée des spots et leur prix.
L'autre table contient les visites. 

Voici un exemple visuel de l'effet d'un spot sur les visites du site.

# Test unitaires

Il y a un sous dossier test/test_unit qui permet de tester vos fonctions pour vous 
assurer qu'elles renvoient le bon format de résultat. Comme nous n'attenonds pas
un résultat exact sur les incréments, nous n'avons pas mis de tests vérifiant le résultat.
- src/test_unit/test_create_db.py ne vous sera normalement pas utile car il sert à 
tester le script qui crée la base de données sqlite
- src/test_unit/test_impact_analysis.py vous permettra de vérifier que les fonctions que vous créez
renvoient les résultats au format attendu (colonnes, nombre de lignes)

Vous pouvez éxecuter les test avec la commande:
``` bash
python -m pytest test/test_unit/test_impact_analysis.py
```

# Installation
- Clonez le repository dans un dossier de votre choix

Il y a un fichier Makefile pour faciliter le déploiement avec les commandes suivantes à faire dans l'ordre.
Vous pouvez aussi faire les actions lister dans le Makefile à la main si vous n'arrivez pas à
executer le makefile

- Créez l'environnement de développement python dédié à ce projet avec :
(il vous faudra installer virtualenv)
``` bash
make venv
```

- Installez toutes les dépendances avec :
``` bash
make dependencies
```

- déployez sqlite dans le dossier de travail avec:
``` bash
make prepare_sqlite
```









