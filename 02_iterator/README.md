# Le pattern itérateur

Le pattern itérateur fournit un moyen d'accéder aux éléments d'une collection 
d'objets de façon séquentielle sans exposer sa représentation sous-jacente. En
python par exemple, les listes et les dictionnaires implémentent le pattern
itérateur, ce qui leur permet de fonctionner avec une boucle **for**.

Il est possible de résumer le pattern itérateur de la manière suivante:

```
TANT QUE pas itérateur.terminé() FAIRE
    élément = itérateur.prochain()

    # faire quelque chose avec élément

FIN TANT QUE
```