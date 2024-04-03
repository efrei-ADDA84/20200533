# Wrapper météo avec Docker

Ce dépôt contient un wrapper météo qui utilise l'API OpenWeatherMap pour récupérer les données météorologiques d'un lieu donné à partir de sa latitude et de sa longitude. Le code est packagé dans une image Docker pour faciliter le déploiement et l'exécution.

## Objectifs

1. Créer un repository Github
2. Créer un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude (passées en variable d'environnement) en utilisant l'API OpenWeatherMap dans le langage de programmation de votre choix.
3. Packager son code dans une image Docker
4. Mettre à disposition son image sur DockerHub

## Utilisation

1. **Téléchargez l'image Docker** :  
Utilisez la commande suivante pour télécharger l'image Docker depuis Docker Hub :
```
docker pull mansat269/weatherapp
```

2. **Exécutez le conteneur Docker** :  
Une fois l'image téléchargée, vous pouvez exécuter le conteneur Docker en fournissant les variables d'environnement nécessaires :
```
docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY= YOUR_API_KEY mansat269/weatherapp
```

Assurez-vous de remplacer `YOUR_API_KEY` par votre clé API OpenWeather


## Étapes réalisées

1. **Choix du langage de programmation** :  
   J'ai choisi d'utiliser Python pour sa simplicité d'utilisation notemment pour l'utilisation d'API

2. **Création du wrapper météo** :  
   J'ai créé un script Python (`weather.py`) qui utilise l'API OpenWeather pour obtenir les données météorologiques d'un lieu donné à partir de sa latitude et de sa longitude.


3. **Packager le code dans une image Docker** :  
J'ai créé un Dockerfile qui décrit l'environnement nécessaire pour exécuter mon application. J'ai utilisé l'image Python officielle comme base, copié mon code source dans le conteneur, installé les dépendances nécessaires avec pip, puis défini la commande par défaut pour exécuter mon application.

J'ai ensuite utilisé la commande 
```
docker build -t myapp .
```
pour construire l'image Docker à partir du Dockerfile.

4. **Mise à Disposition sur DockerHub** :  
Pour rendre l'image disponible sur DockerHub je me suis d'abord connecté à compte DockerHub en utilisant : 

```
docker login
```

Il a ensuite fallu taguer mon image avec mon nom d'utilisateur DockerHub et le nom à donner a l'image:
```
docker tag myapp mansat269/weatherapp
```

Enfin, j'ai utilisé la commande suivante pour posser l'image sur DockerHub et la rendre publique

```
docker push mansat269/weatherapp
```
