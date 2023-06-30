# OSINT---LinkedIn-Scrapping
C'est un outil qui permet de récupérer les informations sur des personnes ayant un poste similaire à un poste recherché. Il est également possible de récupérer les informations des employés d'une entreprise. 

Introduction 

LinkediIn Scrapping est un outil de scrapping destiné à LinkedIn. Il permet de récupérer les informations sur les personnes ayant un poste similaire au poste recherche et également les informations sur les employés d'une entreprise. Avec les données récupérées, nous pouvons rechercher un poste, récupérer les personnes qui ont ce poste ou un poste similaire, récupérer les informations de l'entreprise dans laquelle ces personnes travaillent et enfin récupérer les employés de cette entreprise qui ont un poste similaire. 

Contexte et problématique 
Le but est de créer un outil permettant de récupérer les profils pour un poste donné, d'analyser ces profils en récupérant les informations des entreprises ou ces profils ont travaillé. Ainsi pour un poste donné, nous pourrons déterminer quelles entreprises recrutent le plus pour ce poste. 

État actuelle de l'outil  
L'outil possède les fonctionnalités suivantes : 
    - Une fonction pour se connecter à LinkedIn avec un mail et un mot de passe 
    - une fonction pour nettoyer une chaine de caractère pour ne récupérer que des lettres
    - une fonction pour récupérer les noms et postes des personnes ayant un poste similaire au poste recherché 
    - une fonction pour récupérer les noms et postes des personnes ayant un poste similaire au poste recherché dans une entreprise donné

Difficultés rencontrées 
    - La connexion à LinkedIn a été compliqué parce que LinkedIn a mis une sécurité. Raison pour laquelle dans mon code je passe par un chrome driver pour me connecter.
    - Difficulté à récupérer les noms des profils. LinkedIn a également mis une sécurité et je n'arrive qu'à récupérer ce texte : "utilisateur LinkedIn" mais le nom. 

Tests et résultats 
L'outil a été développer en python avec le l'outil Spider. L'outil possède :
    - des inputs pour saisir le nom du poste recherché et le nom d'une entreprise 
    - des outputs qui affiche le résultat des fonctions 

Scénario : 
   - L'outil demande un mail et un mot de passe pour se connecter à LinkedIn
   - L'utilisateur doit rentrer ses identifiants
   - Une fois connecté, l'outil demande à l'utilisateur de rentrer un nom de poste et un nom d'entreprise
   - l'outil renvoie les résultats

Exécution du scénario : 

Résultats des recherches : 

Conclusion 
Plusieurs améliorations peuvent être faits sur cet outil : 
    - Récupérer les urls des profils pour y accéder directement 
    - Enregistrer les résultats dans une base de données qui possèdera des tables lies pour une clé primaire (nom de l'entreprise)
    - Rechercher idéal pour un poste donné
