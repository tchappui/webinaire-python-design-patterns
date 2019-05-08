# Le Singleton

Le design pattern **singleton** restreint l'instanciation d'une classe à un 
seul objet, ce qui est utile lorsque vous avez besoin d'un objet pour 
coordonner les actions du système.

L'idée de base est qu'une seule instance d'une classe particulière, faisant un 
travail, est créée pour les besoins du programme. Pour que cela fonctionne, 
nous avons besoin de mécanismes qui empêchent l'instanciation de la classe plus 
d'une fois et qui empêchent également le clonage.

## Exemples

- objet de configuration
- objet de logging
- objet controlant l'accès à une ressource:
    - objet de connexion à une base de données
    - mutex


