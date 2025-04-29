# petroleum-agent

**Automatisation self-hosted pour Petroleum.land**  
Un agent Dockerisable qui, en local ou sur un VPS, se connecte à la blockchain Sonic pour :
- Récolter (claim) votre cOIL  
- Réparer vos pompes  
- Raffiner votre surplus  

Chaque utilisateur garde ses clés privées chez lui ; l’agent s’exécute via un simple `docker-compose up`.

---

## Table des matières

1. [Fonctionnalités](#fonctionnalités)  
2. [Prérequis](#prérequis)  
3. [Installation & démarrage rapide](#installation--démarrage-rapide)  
4. [Configuration](#configuration)  
5. [Structure du projet](#structure-du-projet)  
6. [Développement](#développement)  
7. [Contribuer](#contribuer)  
8. [Licence](#licence)  

---

## Fonctionnalités

- Scheduling de vos opérations (`harvest`, `repair`, `refine`) à vos créneaux (ex. 07:00 & 19:00)  
- Interactions directes Web3.py avec :
  - **PetroRewardManager** (claimAll)  
  - **Laboratory** (repairBatch)  
  - **Refinery** (refine)  
- Configuration simple via `config.yaml`  
- Conteneur Docker + `docker-compose` pour un déploiement en 1 commande  

---

## Prérequis

- Docker ≥ 20.10  
- Docker Compose ≥ 1.29  
- (Optionnel) Python 3.11 et `pip` si vous souhaitez exécuter l’agent sans Docker  

---

## Installation & démarrage rapide

1. **Cloner le dépôt**  
   ```bash
   git clone https://github.com/VotreUser/petroleum-agent.git
   cd petroleum-agent/self-hosted-agent
