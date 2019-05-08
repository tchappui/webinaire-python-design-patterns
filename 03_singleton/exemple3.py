from collections import defaultdict

import requests

class Product:

    def __init__(self, code, product_name, **kwargs):
        self.code = code
        self.product_name = product_name

    def __str__(self):
        return f"({self.code}, {self.product})"

    def __hash__(self):
        return hash(self.code)

    def __eq__(self, other):
        return self.code == other.code


class SingletonType(type):

    _singletons = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._singletons:
            cls._singletons[cls] = super().__call__(*args, **kwargs)
        return cls._singletons[cls]


class ProductFetcher(metaclass=SingletonType):

    def __init__(self):
        self.products = defaultdict(set)
        
    def fetch(self, category, page=1, page_size=20, country="fr"):
        url = f"https://{country}.openfoodfacts.org/cgi/search.pl"
        payload = {
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": category,
            "json": 1,
            "page_size": page_size,
            "page": page,
            "sort_by": "unique_scans_n",
        }
        response = requests.get(url, params=payload)
        if response.status_code == 200:
            data = response.json()
            for product in data["products"]:
                try:
                    self.products[category].add(Product(**product))
                except TypeError:
                    continue
        return self.products[category]