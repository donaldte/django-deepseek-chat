# Django DeepSeek Chat

## 📌 Description
Django DeepSeek Chat est une application de chat en temps réel basée sur Django, Django Channels et WebSockets. Elle permet aux utilisateurs de créer et rejoindre des salons de discussion dynamiques et d'interagir avec une IA DeepSeek intégrée. L'application est optimisée pour offrir une expérience fluide et réactive, permettant aux utilisateurs de poser des questions à l'IA, d'apprendre et de collaborer sur des projets.

## 🚀 Fonctionnalités
- 📡 **WebSockets avec Django Channels** pour la communication en temps réel
- 👤 **Authentification utilisateur** (connexion et inscription)
- 💬 **Salons de discussion dynamiques** (création et gestion des chats)
- 🔄 **Système de messagerie instantanée** avec mise à jour en temps réel
- 🤖 **Intégration de l'IA DeepSeek** pour répondre aux questions et assister les utilisateurs
- 📝 **Stockage des messages dans la base de données**
- 🎨 **Interface utilisateur responsive** avec Bootstrap
- ☁️ **Déploiement avec Daphne et Redis**

## 🛠 Prérequis
Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- **Python 3.8+**
- **pip et virtualenv**
- **PostgreSQL ou SQLite** (selon votre choix de base de données)
- **Redis** (pour la gestion des WebSockets)
- **Ollama** installé
- **Un modèle DeepSeek configuré en local avec Ollama**
- **Git**

## 📦 Installation
### 🔹 1. Cloner le dépôt
```bash
git clone https://github.com/donaldte/django-deepseek-chat.git
cd django-deepseek-chat
```

### 🔹 2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### 🔹 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 🔹 4. Configurer la base de données
```bash
python manage.py migrate
```

### 🔹 5. Créer un superutilisateur (optionnel pour l'admin)
```bash
python manage.py createsuperuser
```

### 🔹 6. Lancer le serveur de développement
```bash
python manage.py runserver
```
Accéder à l'application sur [http://127.0.0.1:8000](http://127.0.0.1:8000)

## ⚙️ Configuration WebSockets avec Daphne et Redis
Pour exécuter le serveur en mode WebSocket avec **Daphne** et **Redis**, utilise :
```bash
daphne -b 0.0.0.0 -p 8000 deepseek_chat.asgi:application
```
Si tu utilises **Redis** pour le backend des channels, assure-toi que Redis est installé et lancé :
```bash
redis-server
```

## 📜 Fichier `.env` (Exemple de configuration environnementale)
Crée un fichier `.env` à la racine du projet et ajoute tes variables de configuration si nécessaire :
```ini
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/deepseek_chat
REDIS_URL=redis://127.0.0.1:6379/0
```

## 🏗 Technologies utilisées
- **Django** (backend principal)
- **Django Channels** (gestion des WebSockets)
- **Redis** (gestion des messages en temps réel)
- **Daphne** (serveur ASGI)
- **PostgreSQL / SQLite** (base de données)
- **Bootstrap** (interface utilisateur responsive)
- **Ollama** (exécution des modèles DeepSeek en local)

## 🎯 Roadmap
- 🔜 Ajout des notifications en temps réel
- 🔜 Support multi-room avancé
- 🔜 Historique des conversations stocké et consultable
- 🔜 Amélioration de l'IA pour une meilleure interaction utilisateur

## 🤝 Contribuer
Les contributions sont les bienvenues ! Pour contribuer :
1. Fork le projet 🍴
2. Crée une branche de fonctionnalité (`git checkout -b feature-xyz`)
3. Commit tes modifications (`git commit -m "Ajout d'une nouvelle fonctionnalité"`)
4. Pousse la branche (`git push origin feature-xyz`)
5. Crée une Pull Request 🛠

## 📄 Licence
Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 💬 Contact
Développé par **Donald Programmeur**. 
- 🌐 [Site Web](https://hooyia.net)
- 📧 Email: donaldtedom0@gmail.com
- 🐙 [GitHub](https://github.com/donaldte)

⭐️ **N'oublie pas de laisser une étoile sur le repo si ce projet t'a aidé !** ⭐️

