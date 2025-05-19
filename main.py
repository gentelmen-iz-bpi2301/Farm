from animal_data import AnimalData
from report import Report
from farm_logic import FarmLogic
from storage import save_to_file, load_from_file

def run():
    d = AnimalData()
    r = Report()
    l = FarmLogic()
    
    # Загрузка данных
    loaded = load_from_file()
    if loaded:
        d.animals = loaded.get('animals', [])
        d.products = loaded.get('products', [])
        d.sales = loaded.get('sales', [])

    while True:
        print("\n1. Добавить животное")
        print("2. Показать всех животных")
        print("3. Собрать продукцию")
        print("4. Показать всю продукцию")
        print("5. Продать продукцию")
        print("6. Показать продажи")
        print("7. Финансовый отчет")
        print("8. Сохранить данные")
        print("9. Выход")
        
        c = input("Выберите: ")
        
        if c == "1":
            t = input("Введите тип (корова/овца/курица/коза/утка): ")
            n = input("Введите имя: ")
            a = input("Введите возраст: ")
            w = input("Введите вес: ")
            l.add_animal(d, t, n, a, w)
        elif c == "2":
            r.show_all(d)
        elif c == "3":
            t = input("Введите тип животного: ")
            r.collect_products(d, l, t)
        elif c == "4":
            r.show_products(d)
        elif c == "5":
            p = input("Тип продукции: ")
            a = input("Количество: ")
            pr = input("Цена: ")
            l.sell_product(d, p, a, pr)
        elif c == "6":
            r.show_sales(d)
        elif c == "7":
            r.financial_report(d)
        elif c == "8":
            save_to_file({'animals': d.animals, 'products': d.products, 'sales': d.sales})
        elif c == "9":
            break