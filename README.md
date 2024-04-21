# TP1 - Wrapper météo avec Docker

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

J'ai opté pour Alpine Linux comme base pour cette image Docker car elle me permet de bénéficier d'une taille réduite d'une sécurité accrue pour minimiser les vulnérabilités détectées Trivy.

L'utilisation de la commande `pip install --no-cache-dir requests==2.3` permet d'éviter les erreurs de linting. En spécifiant `--no-cache-dir`, je désactive la mise en cache des fichiers téléchargés, ce qui garantit que je n'utilise que la version spécifique de la bibliothèque Requests (2.3) et évite les erreurs potentielles causées par des versions plus récentes ou incompatibles

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

# TP2 - Weather API

Ce TP vise à créer une API météo qui récupère les données météorologiques d'un lieu donné à partir de la latitude et de la longitude fournies.

## Objectifs

- Créer une API météo
- Configurer un workflow GitHub Actions pour automatiser la construction de l'image Docker et son déploiement sur Docker Hub.
- Publier l'image Docker sur Docker Hub.
- Exposer l'API météo à l'aide de Docker.

## Utilisation

Pour utiliser cette API météo, suivez les étapes suivantes :

2. Accédez au répertoire du projet :

    ```bash
    cd weather-api
    ```

3. Définissez votre clé API OpenWeatherMap en tant que variable d'environnement :

    ```bash
    export OPENWEATHER_API_KEY=votre_clé_api
    ```

4. Lancez l'API en utilisant Docker :

    ```bash
    docker run -p 8081:8081 -e OPENWEATHER_API_KEY=$OPENWEATHER_API_KEY mansat269/weatherapp:latest
    ```

5. Accédez à l'API à l'aide de votre navigateur Web ou d'un outil comme cURL :

    ```bash
    curl "http://localhost:8081/?lat=3.140853&lon=101.693207"
    ```

## Étapes réalisées

1. **Configuration du Workflow GitHub Actions :** Un workflow GitHub Actions a été configuré pour automatiser la construction de l'image Docker à chaque nouveau commit sur la branche principale. L'image est ensuite poussée vers Docker Hub.
    
2. **Transformation du Wrapper en API :** Le wrapper météo a été transformé en une API utilisant Flask. Cette API accepte les paramètres de latitude et de longitude et renvoie les données météorologiques correspondantes à partir de l'API OpenWeatherMap.

J'ai choisi d'utiliser Flask pour développer l'API météo principalement parce que mon wrapper initial était déjà écrit en Python. Flask est un micro-framework web en Python qui offre une syntaxe simple et intuitive, ce qui rend la transition du wrapper vers une API plus fluide et efficace.
    
3. **Publication automatique sur Docker Hub :** L'image Docker de l'API est automatiquement publiée sur Docker Hub à chaque nouveau commit sur la branche principale, grâce au workflow GitHub Actions.
    
4. **Exposition de l'API :** L'API météo est exposée en utilisant Docker. Les utilisateurs peuvent accéder à l'API en exécutant un conteneur Docker local et en envoyant des requêtes HTTP aux endpoints appropriés.

## Explication du Workflow GitHub Actions

### Définition des conditions de déclenchement du workflow

Le workflow est déclenché à chaque fois qu'un push est effectué sur la branche principale (main). Cela signifie que chaque fois qu'un commit est effectué sur la branche main, le workflow sera déclenché pour construire et pousser l'image Docker.

```yaml
on:
  push:
    branches:
      - main
```

### Tâches à exécuter

Le workflow consiste en une seule tâche (build-and-push), qui est exécutée sur un runner Ubuntu.

```yaml
jobs:
  build-and-push:
    runs-on: ubuntu-latest
```

1. **Clonage du dépôt** :  
   La première étape consiste à cloner le dépôt GitHub dans le runner.

```yaml
steps:
  - name: Checkout repository 
    uses: actions/checkout@v2
```

2. **Configuration de Docker Buildx** :  
   Ensuite, Docker Buildx est configuré pour permettre la construction d'images Docker multiplateformes.

```yaml
  - name: Set up Docker Buildx
    uses: docker/setup-buildx-action@v1
```

3. **Connexion à Docker Hub** :  
Le workflow se connecte à Docker Hub en utilisant les identifiants Docker Hub stockés dans les secrets GitHub.

```yaml
    - name: Login to Docker Hub
    uses: docker/login-action@v1
    with:
      username: ${{ secrets.DOCKERHUB_USERNAME }} 
      password: ${{ secrets.DOCKERHUB_PASSWORD }}
```

4. **Construction et publication de l'image Docker** :  
L'image Docker est construite à partir du Dockerfile dans le répertoire actuel et est ensuite poussée vers Docker Hub.

```yaml
     - name: Build and push Docker image
    id: docker_build
    uses: docker/build-push-action@v2
    with:
      context: .
      file: ./Dockerfile
      push: true
      tags: mansat269/weatherapp:latest
    env:
      OPENWEATHER_API_KEY: ${{ secrets.OPENWEATHER_API_KEY }}
```

4. **Exécution de Hadolint** :  
Enfin, Hadolint est exécuté pour vérifier le Dockerfile avant la construction de l'image Docker.

```yaml
      - name: Run Hadolint
    uses: hadolint/hadolint-action@v1.6.0
    with:
      dockerfile: Dockerfile
```



# TP3 - Cloud - ACI

Ce TP vise à créer une API météo qui récupère les données météorologiques d'un lieu donné à partir de la latitude et de la longitude fournies, avec déploiement sur Azure Container Instance (ACI) utilisant GitHub Actions pour l'automatisation du processus.

## Objectifs

- Mettre à disposition son code dans un repository Github
- Mettre à disposition son image (format API) sur Azure Container Registry (ACR) using Github Actions
- Deployer sur Azure Container Instance (ACI) using Github Actions

## Utilisation

Pour utiliser cette API météo, suivez les étapes suivantes :

Accédez à l'URL suivante dans votre navigateur web ou via une requête HTTP :

[http://devops-20200533.francesouth.azurecontainer.io/?lat=5.902785&lon=102.754175](http://devops-20200533.francesouth.azurecontainer.io/?lat=5.902785&lon=102.754175)

Assurez-vous de remplacer les valeurs `lat` et `lon` par les coordonnées de latitude et de longitude du lieu dont vous souhaitez obtenir les données météorologiques.

Exemple d'utilisation avec cURL :

```bash
curl "http://devops-20200533.francesouth.azurecontainer.io/?lat=5.902785&lon=102.754175"
```

## Étapes réalisées

### Surveillance des Métriques avec Prometheus

Pour améliorer la surveillance de notre application, nous avons intégré la collecte de métriques à l'aide de Prometheus. Voici ce que fait ce rajout :

- **Importation des modules nécessaires :** Nous importons les modules `PrometheusMetrics`, `Counter`, `generate_latest`, et `CONTENT_TYPE_LATEST` depuis les bibliothèques Prometheus et Flask.

```python
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
```

- **Initialisation de PrometheusMetrics :** Nous utilisons `PrometheusMetrics` pour créer une instance qui va automatiquement exposer nos métriques à l'URL `/metrics`.

```python
app = Flask(__name__)
metrics = PrometheusMetrics(app)
```

- **Définition de la route des métriques :** Nous définissons une route `/metrics` à laquelle Prometheus peut accéder pour collecter les métriques. Lorsque cette route est appelée, nous générons les dernières métriques au format Prometheus et les retournons avec le type de contenu approprié grâce au code suivant.

```python
@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'contentType': CONTENT_TYPE_LATEST}
```

Cette intégration nous permet de surveiller plus efficacement les performances de notre application et de collecter des métriques importantes pour l'analyse et le diagnostic.


### Mise a jour du Github Workflow

Enfin, afin de déployer ce code sur ACI après 'avoir build et push sur ACR le github workflow a été mis à jour pour se connecter à azure en utilisant les organisation secrets et configurer les paramètres de notre ressource:

```yaml
- name: 'Deploy to Azure Container Instance' 
        uses: azure/aci-deploy@v1
        with: 
          resource-group: ADDA84-CTP 
          dns-name-label: devops-20200533
          image: ${{ secrets.REGISTRY_LOGIN_SERVER }}/20200533 
          name: 20200533 
          location: 'france south' 
          registry-login-server: ${{ secrets.REGISTRY_LOGIN_SERVER }}
          registry-username: ${{ secrets.REGISTRY_USERNAME }} 
          registry-password: ${{ secrets.REGISTRY_PASSWORD }}
          secure-environment-variables: OPENWEATHER_API_KEY=${{ secrets.OPENWEATHER_API_KEY }} 
```
# TP4 - Cloud - Terraform
## Objectifs

Ce document décrit le processus pour déployer une machine virtuelle Azure (VM) avec une adresse IP publique dans un réseau existant (network-tp4) en utilisant Terraform. Les objectifs spécifiques sont les suivants :

1. **Créer une machine virtuelle Azure (VM) :** Déployer une VM dans Azure avec une adresse IP publique, en utilisant Terraform pour automatiser le processus.

2. **Utiliser Terraform :** Utiliser Terraform pour décrire et provisionner l'infrastructure Azure requise pour la VM.

3. **Se connecter à la VM avec SSH :** Configurer la VM pour permettre la connexion SSH et se connecter à celle-ci après son déploiement.

4. **Comprendre les différents services Azure (ACI vs. AVM) :** Explorer les différences entre les services Azure Container Instances (ACI) et Azure Virtual Machines (AVM) dans le contexte de ce déploiement.

5. **Mettre à disposition son code dans un repository GitHub :** Héberger le code Terraform dans un repository GitHub pour faciliter la collaboration et le suivi des modifications.

## Contraintes

L'ensemble du déploiement doit respecter les contraintes suivantes :

- **Location :** France Central
- **Azure Subscription ID :** 765266c6-9a23-4638-af32-dd1e32613047
- **Azure Resource Group :** ADDA84-CTP
- **Network :** network-tp4
- **Subnet :** internal
- **Azure VM Name :** devops-<identifiant-efrei>
- **VM Size :** Standard_D2s_v3
- **Authentification :** Utiliser Azure CLI pour l'authentification
- **Utilisateur Administrateur de la VM :** devops
- **Création d'une clé SSH avec Terraform**
- **Système d'exploitation :** Ubuntu 22.04

## Fichiers Terraform

Ce projet contient plusieurs fichiers Terraform, chacun ayant un rôle spécifique dans le déploiement de l'infrastructure Azure nécessaire à la machine virtuelle. Voici une brève description de chaque fichier :

- **`main.tf` :** Ce fichier contient la configuration principale pour créer une interface réseau Azure, une adresse IP publique, et une machine virtuelle Azure. Il définit également la configuration de l'interface réseau et l'allocation de l'adresse IP publique.

- **`data.tf` :** Ce fichier utilise les données existantes d'Azure pour récupérer des informations sur le réseau virtuel et le sous-réseau spécifiés dans les variables.

- **`network.tf` :** Ce fichier définit la ressource pour l'interface réseau Azure, y compris la configuration de l'adresse IP privée et l'association avec le sous-réseau.

- **`ssh.tf` :** Ce fichier crée une clé SSH utilisée pour se connecter à la machine virtuelle Azure. Il génère une paire de clés privée/publique utilisée pour l'authentification SSH.

- **`variables.tf` :** Ce fichier contient les déclarations de toutes les variables utilisées dans le projet Terraform, telles que l'ID d'abonnement Azure, le nom du groupe de ressources, le nom du réseau virtuel, le nom du sous-réseau, etc.

- **`virtual_machine.tf` :** Ce fichier contient la configuration pour créer la machine virtuelle Azure. Il définit le type de machine virtuelle, le système d'exploitation, la taille du disque, le script personnalisé à exécuter au démarrage, et les clés SSH pour l'authentification.

Chaque fichier contribue à la configuration globale de l'infrastructure Azure nécessaire à la création de la machine virtuelle dans Azure.

## Étapes Réalisées

Voici les différentes étapes que j'ai suivies pour mener à bien ce projet :

1. **Installation de Terraform et Azure CLI avec Brew :** J'ai installé Terraform et Azure CLI sur ma machine en utilisant Homebrew pour simplifier la gestion des dépendances.

   ```bash
   brew install terraform azure-cli
   ```

2. **Connexion à Azure avec az login :** Pour permettre à Terraform d'interagir avec Azure, j'ai utilisé la commande `az login` pour me connecter à mon compte Azure.

   ```bash
   az login
   ```

3. **Initialisation de Terraform :** J'ai initialisé mon projet Terraform dans le répertoire de travail en exécutant la commande `terraform init`, ce qui a permis de télécharger les plugins nécessaires et d'initialiser l'état du projet.

   ```bash
   terraform init
   ```
4. **Formatage du code Terraform :** J'ai utilisé la commande terraform fmt pour formater mon code Terraform selon les conventions de style recommandées.

   ```bash
   terraform fmt
   ```


5. **Planification des ressources Terraform :** Après avoir initialisé et formaté mon projet, j'ai planifié les ressources à déployer avec la commande `terraform plan`.

   ```bash
   terraform plan
   ```

6. **Déploiement des ressources Terraform :** Une fois satisfait du plan de déploiement, j'ai procédé au déploiement des ressources dans Azure en exécutant la commande `terraform apply`.

   ```bash
   terraform apply
   ```

## Connexion a la VM en SSH

La seconde partie de ce TP consistait a se connecter a distance a la VM fraichement déployée grâce au protocole SSH

1. **Récupération de l'adresse IP publique de la VM :** J'ai copié l'adresse IP publique de la machine virtuelle déployée depuis le portail Azure afin de pouvoir l'utiliser dans les commandes qui vont suivre.

2. **Génération de la clé privée SSH :** J'ai généré une paire de clés SSH localement à l'aide de la commande `ssh-keygen`.

   ```bash
   ssh-keygen -t rsa -b 4096 -C "thierno-sadou.diallo@efrei.net"
   ```

3. **Récupération de la clé privée Terraform :** J'ai récupéré la clé privée générée par Terraform en utilisant la commande `terraform output private_key_pem`, que j'ai ensuite enregistrée dans un fichier `id_rsa.pem`.

4. **Connexion SSH à la machine virtuelle :** En utilisant la clé privée générée, j'ai établi une connexion SSH à la machine virtuelle avec la commande `ssh`.

   ```bash
   ssh -i id_rsa.pem devops@52.143.179.175
   ```

5. **Vérification du système d'exploitation de la VM :** Pour confirmer que la machine virtuelle correspondait à mes spécifications, j'ai récupéré des informations sur le système d'exploitation avec la commande `cat /etc/os-release`.

nous obtenons la sortie siuvante qui nous confirme que les contraintes ont été respectées:

```
   PRETTY_NAME="Ubuntu 22.04.4 LTS"
   NAME="Ubuntu"
   VERSION_ID="22.04"
   VERSION="22.04.4 LTS (Jammy Jellyfish)"
   VERSION_CODENAME=jammy
   ID=ubuntu
   ID_LIKE=debian
   HOME_URL="https://www.ubuntu.com/"
   SUPPORT_URL="https://help.ubuntu.com/"
   BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
   PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
   UBUNTU_CODENAME=jammy
   ```

6. **Destruction des ressources Terraform :** Une fois que j'ai terminé d'utiliser la machine virtuelle, j'ai supprimé les ressources Terraform pour éviter les coûts inutiles en exécutant la commande `terraform destroy`.

    ```bash
    terraform destroy
    ```
