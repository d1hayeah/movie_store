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
            for i in range(len(suppliers)):
                s = suppliers[i]
                print(f"{s.supplier_id}. {s.name} | Контакты: {s.contact_info}")

        elif choice == "2":
            print("\n=== Добавление поставщика ===")
            name = input("Название: ")
            contact_info = input("Контактная информация: ")
            supplier = Supplier(name=name, contact_info=contact_info)
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
            for i in range(len(get_all_suppliers())):
                s = get_all_suppliers()[i]
                if s.supplier_id == id_to_edit:
                    current = s
                    break
            if not current:
                print("❌ Поставщик не найден!")
                continue

            name = input(f"Новое имя ({current.name}): ") or current.name
            contact_info = input(f"Новые контакты: ") or current.contact_info

            updated = Supplier(supplier_id=id_to_edit, name=name, contact_info=contact_info)
            updated.save()
            print("✅ Поставщик обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")