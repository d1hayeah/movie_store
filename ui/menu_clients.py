from models.client_model import Client, get_all_clients

def menu_clients():
    while True:
        print("\n=== Клиенты ===")
        print("1. Показать всех клиентов")
        print("2. Добавить клиента")
        print("3. Удалить клиента")
        print("4. Изменить клиента")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            clients = get_all_clients()
            print("\nСписок клиентов:")
            for c in clients:
                print(f"{c.client_id}. {c.name} | Телефон: {c.phone} | Email: {c.email}")

        elif choice == "2":
            print("\n=== Добавление нового клиента ===")
            name = input("Имя клиента: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            client = Client(name=name, phone=phone, email=email)
            client.save()
            print("✅ Клиент добавлен.")

        elif choice == "3":
            id_to_delete = input("Введите ID клиента для удаления: ")
            client = Client(client_id=int(id_to_delete))
            client.delete()
            print("❌ Клиент удален.")

        elif choice == "4":
            id_to_edit = int(input("Введите ID клиента для редактирования: "))
            current_client = None
            for c in get_all_clients():
                if c.client_id == id_to_edit:
                    current_client = c
                    break
            if not current_client:
                print("❌ Клиент не найден!")
                continue
            
            print("Оставьте поле пустым, чтобы не изменять значение")
            name = input(f"Новое имя: ") or current_client.name
            phone = input(f"Новый телефон: ") or current_client.phone
            email = input(f"Новый email: ") or current_client.email

            updated = Client(client_id=id_to_edit, name=name, phone=phone, email=email)
            updated.save()
            print("✅ Клиент обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")