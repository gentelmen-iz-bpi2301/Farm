class Report:
    def show_all(self, data):
        animals = data.get_all_animals()
        for a in animals:
            print(f"{a['type']} {a['name']}, возраст {a['age']}, вес {a['weight']}")
    
    def collect_products(self, data, logic, animal_type):
        products = logic.collect(data, animal_type)
        for p in products:
            print(f"Собрано: {p['amount']} кг/шт. {p['type']}")
    
    def show_products(self, data):
        products = data.get_all_products()
        total = {}
        for p in products:
            if p['type'] in total:
                total[p['type']] += p['amount']
            else:
                total[p['type']] = p['amount']
        
        print("Вся продукция:")
        for t, a in total.items():
            print(f"{t}: {a} кг/шт.")
    
    def show_sales(self, data):
        sales = data.get_all_sales()
        for s in sales:
            print(f"Продано {s['amount']} {s['product']} за {s['price']} руб.")
    
    def financial_report(self, data):
        sales = data.get_all_sales()
        total = sum(float(s['price']) for s in sales)
        print(f"Общий доход: {total} руб.")