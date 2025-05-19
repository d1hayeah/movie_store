from models.employee_model import Employee, get_all_employees, get_employee_by_id

def menu_employees():
    while True:
        print("\n=== Сотрудники ===")
        print("1. Показать всех сотрудников")
        print("2. Добавить сотрудника")
        print("3. Удалить сотрудника")
        print("4. Изменить сотрудника")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            employees = get_all_employees()
            print("\nСписок сотрудников:")
            for e in employees:
                print(f"{e.employee_id}. {e.first_name} {e.last_name} | Должность: {e.position}")

        elif choice == "2":
            print("\n=== Добавление сотрудника ===")
            first_name = input("Имя: ")
            last_name = input("Фамилия: ")
            position = input("Должность: ")
            employee = Employee(first_name=first_name, last_name=last_name, position=position)
            employee.save()
            print("✅ Сотрудник добавлен.")

        elif choice == "3":
            id_to_delete = input("Введите ID сотрудника: ")
            employee = Employee(employee_id=int(id_to_delete))
            employee.delete()
            print("❌ Сотрудник удален.")

        elif choice == "4":
            id_to_edit = int(input("ID сотрудника: "))
            current = get_employee_by_id(id_to_edit)
            if not current:
                print("❌ Сотрудник не найден!")
                continue

            print("Оставьте поле пустым, чтобы не изменять.")
            first_name = input(f"Новое имя: ") or current.first_name
            last_name = input(f"Новая фамилия: ") or current.last_name
            position = input(f"Новая должность: ") or current.position

            updated = Employee(employee_id=id_to_edit, first_name=first_name, last_name=last_name, position=position)
            updated.save()
            print("✅ Сотрудник обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
