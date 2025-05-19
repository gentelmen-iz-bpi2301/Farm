class AnimalData:
    def __init__(self):
        self.animals = []
        self.products = []
        self.sales = []
    
    def save_animal(self, animal):
        self.animals.append(animal)
    
    def save_product(self, product):
        self.products.append(product)
    
    def save_sale(self, sale):
        self.sales.append(sale)
    
    def get_animals_by_type(self, animal_type):
        return [a for a in self.animals if a['type'] == animal_type]
    
    def get_all_animals(self):
        return self.animals
    
    def get_all_products(self):
        return self.products
    
    def get_all_sales(self):
        return self.sales
    
    def remove_product(self, product_type, amount):
        # Сложная логика удаления продуктов
        pass