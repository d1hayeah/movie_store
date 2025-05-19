from models.supplier_model import Supplier, get_all_suppliers

def menu_suppliers():
    while True:
        print("\n=== Поставщики ===")
        print("1. Показать всех поставщиков")
        print("2. Добавить поставщика")
        print("3. Удалить поставщика")
        print("4. Изменить поставщика")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            suppliers = get_all_suppliers()
            print("\nСписок поставщиков:")
            for s in suppliers:
                print(f"{s.supplier_id}. {s.name} | Телефон: {s.phone} | Email: {s.email}")

        elif choice == "2":
            print("\n=== Добавление поставщика ===")
            name = input("Название: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            supplier = Supplier(name=name, phone=phone, email=email)
            supplier.save()
            print("✅ Поставщик добавлен.")

        elif choice == "3":
            id_to_delete = input("Введите ID поставщика: ")
            supplier = Supplier(supplier_id=int(id_to_delete))
            supplier.delete()
            print("❌ Поставщик удален.")

        elif choice == "4":
            id_to_edit = int(input("ID поставщика: "))
            current = None
            for s in get_all_suppliers():
                if s.supplier_id == id_to_edit:
                    current = s
                    break
            if not current:
                print("❌ Поставщик не найден!")
                continue

            name = input(f"Новое имя: ") or current.name
            phone = input(f"Новый телефон: ") or current.phone
            email = input(f"Новый email: ") or current.email

            updated = Supplier(supplier_id=id_to_edit, name=name, phone=phone, email=email)
            updated.save()
            print("✅ Поставщик обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")