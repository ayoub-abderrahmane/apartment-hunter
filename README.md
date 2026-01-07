Documentation – Modèles de Régression pour la Prédiction du Prix des Maisons

1. Contexte du projet

Ce projet a pour objectif de prédire le prix d’un bien immobilier à partir de plusieurs caractéristiques (features) comme :

- la superficie,

- la ville,

- le nombre de pièces,

- l’état du bien, etc.

Pour cela, plusieurs modèles de régression ont été testés afin de comparer leurs performances et leur capacité à généraliser correctement sur de nouvelles données.

Les trois modèles principaux utilisés sont :

la Régression Linéaire,

le Random Forest Regressor,

le Gradient Boosting Regressor.

Chaque modèle a ses avantages, ses limites, et répond à un besoin différent (simplicité, robustesse, performance).

2. La Régression Linéaire
Description générale

La régression linéaire est le modèle le plus simple et le plus utilisé en régression. Elle cherche à établir une relation mathématique entre les variables d’entrée (features) et la variable cible (le prix).

Elle repose sur une formule du type :

Prix = a₁×Feature1 + a₂×Feature2 + a₃×Feature3 + b

Chaque coefficient représente l’influence d’une variable sur le prix.

⚙️ Fonctionnement

Le modèle ajuste automatiquement les coefficients pour minimiser l’erreur entre les prix prédits et les prix réels.
L’apprentissage se fait en trouvant la meilleure droite (ou hyperplan en plusieurs dimensions) qui passe au plus près des données.

✅ Avantages

Simple et rapide à entraîner

Facile à interpréter

Très bon modèle de référence (baseline)

Faible coût de calcul

❌ Inconvénients

Gère mal les relations complexes

Sensible aux valeurs aberrantes (outliers)

Peu performante si la relation entre les variables n’est pas linéaire

🎯 Rôle dans le projet

Elle sert de point de comparaison de base pour juger l’apport des modèles plus avancés.

3. Random Forest Regressor
Description générale

Le Random Forest est un modèle basé sur un ensemble d’arbres de décision. Au lieu de faire une seule prédiction, il en fait des centaines, puis calcule la moyenne.

C’est un modèle très utilisé dans l’immobilier car il gère bien :

les données bruitées,

les relations non linéaires,

les interactions entre variables.

⚙️ Fonctionnement

Plusieurs arbres de décision sont construits à partir de sous-échantillons du jeu de données.

Chaque arbre fait une prédiction de prix.

Le modèle final prend la moyenne de toutes les prédictions.

Ce principe permet de réduire le risque de surapprentissage (overfitting).

✅ Avantages

Très bonne précision

Robuste aux erreurs et au bruit

Capable de gérer des relations complexes

Peu sensible aux valeurs aberrantes

❌ Inconvénients

Plus lent à entraîner

Moins interprétable qu’une régression linéaire

Modèle plus lourd

🎯 Rôle dans le projet

C’est le modèle intermédiaire, souvent très performant sans réglages complexes.

4. Gradient Boosting Regressor
Description générale

Le Gradient Boosting est un modèle basé sur un apprentissage progressif par correction des erreurs.
Contrairement au Random Forest où les arbres sont indépendants, ici chaque arbre apprend à corriger les erreurs du précédent.

On retrouve ce principe dans des bibliothèques très connues comme :

XGBoost,

LightGBM,

CatBoost.

⚙️ Fonctionnement

Un premier modèle fait une prédiction grossière.

Un second modèle apprend uniquement à prédire les erreurs du premier.

Le processus se répète sur plusieurs itérations.

Les prédictions sont additionnées pour produire le résultat final.

Cela permet d’obtenir un modèle très précis et très puissant.

✅ Avantages

Excellente précision

Très bon pour les données complexes

Très utilisé en compétition et en industrie

Gère bien les non-linéarités

❌ Inconvénients

Plus long à entraîner

Plus compliqué à régler

Risque d’overfitting si mal paramétré

Peu interprétable

Rôle dans le projet

C’est le modèle final de performance, utilisé pour obtenir les meilleurs résultats possibles.

5. Comparaison des modèles

Modèle	            Simplicité	Précision	  Interprétabilité	Temps d'entraînement
Régression Linéaire	✅✅✅    ⭐⭐	      ✅✅✅	         Très rapide
Random Forest	    ✅✅	     ⭐⭐⭐⭐	✅                 Moyen
Gradient Boosting	✅	      ⭐⭐⭐⭐⭐	❌                 Plus long

6. Évaluation des performances

Les modèles sont évalués à l’aide des métriques suivantes :

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² (Coefficient de détermination)

Cela permet de comparer objectivement les performances et de choisir le modèle le plus adapté.

7. Conclusion

Dans ce projet :

La régression linéaire sert de référence simple.

Le Random Forest apporte robustesse et précision.

Le Gradient Boosting permet d’atteindre les meilleures performances.

Ce trio offre un bon équilibre entre compréhension du modèle et puissance prédictive.