class FarmLogic:
    def add_animal(self, data, animal_type, name, age, weight):
        if animal_type not in ['корова', 'овца', 'курица', 'коза', 'утка']:
            print("Неизвестный тип животного")
            return
        
        a = {'type': animal_type, 'name': name, 'age': age, 'weight': weight}
        data.save_animal(a)
    
    def collect(self, data, animal_type):
        products = []
        animals = data.get_animals_by_type(animal_type)
        
        for a in animals:
            if a['type'] == 'корова':
                milk = 10 * float(a['weight']) / 100
                products.append({'type': 'молоко', 'amount': round(milk, 2)})
                if int(a['age']) > 2:
                    beef = 50 * float(a['weight']) / 100
                    products.append({'type': 'говядина', 'amount': round(beef, 2)})
            elif a['type'] == 'овца':
                wool = 5 * float(a['weight']) / 100
                products.append({'type': 'шерсть', 'amount': round(wool, 2)})
                if int(a['age']) > 3:
                    mutton = 30 * float(a['weight']) / 100
                    products.append({'type': 'баранина', 'amount': round(mutton, 2)})
            elif a['type'] == 'курица':
                eggs = 15 * (1 + float(a['age']) / 10)
                products.append({'type': 'яйца', 'amount': round(eggs)})
            elif a['type'] == 'коза':
                cheese = 8 * float(a['weight']) / 100
                products.append({'type': 'сыр', 'amount': round(cheese, 2)})
            elif a['type'] == 'утка':
                eggs = 10 * (1 + float(a['age']) / 10)
                products.append({'type': 'яйца', 'amount': round(eggs)})
                meat = 20 * float(a['weight']) / 100
                products.append({'type': 'утина', 'amount': round(meat, 2)})
        
        for p in products:
            data.save_product(p)
        
        return products
    
    def sell_product(self, data, product_type, amount, price):
        # Сложная логика продажи
        pass