from models.rental_model import Rental, get_all_rentals, get_rental_by_id
from models.employee_model import get_all_employees, get_employee_by_id

def menu_rentals():
    while True:
        print("\n=== Прокат ===")
        print("1. Показать все записи проката")
        print("2. Добавить запись проката")
        print("3. Удалить запись проката")
        print("4. Изменить запись проката")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            rentals = get_all_rentals()
            print("\nСписок записей проката:")
            for r in rentals:
                employee = get_employee_by_id(r.employee_id) 
                employee_str = f"{employee.first_name} {employee.last_name}"
                print(f"{r.rental_id}. Клиент ID: {r.client_id} | Фильм ID: {r.movie_id} | Дата начала: {r.rental_date} | Дата возврата: {r.return_date or 'Не возвращено'} | Сотрудник: {employee_str}")

        elif choice == "2":
            print("\n=== Добавление записи проката ===")
            client_id = int(input("ID клиента: "))
            movie_id = int(input("ID фильма: "))
            rental_date = input("Дата начала проката (YYYY-MM-DD): ")
            return_date = input("Дата возврата (YYYY-MM-DD, оставьте пустым если не возвращено): ") or None
            rental_price = int(input("Стоимость проката: ")) 

            print("Доступные сотрудники:")
            employees = get_all_employees()
            for e in employees:
                print(f"{e.employee_id}. {e.first_name} {e.last_name}")
            employee_id = int(input("Введите ID сотрудника: "))

            rental = Rental(client_id=client_id, movie_id=movie_id, rental_date=rental_date, return_date=return_date, rental_price=rental_price, employee_id=employee_id)
            rental.save()
            print("✅ Запись проката добавлена.")

        elif choice == "3":
            id_to_delete = input("Введите ID записи проката: ")
            rental = Rental(rental_id=int(id_to_delete))
            rental.delete()
            print("❌ Запись проката удалена.")

        elif choice == "4":
            id_to_edit = int(input("ID записи проката: "))
            current = get_rental_by_id(id_to_edit)
            if not current:
                print("❌ Запись проката не найдена!")
                continue

            print("Оставьте поле пустым, чтобы не изменять.")
            client_id = input(f"ID клиента: ") or current.client_id
            movie_id = input(f"ID фильма: ") or current.movie_id
            rental_date = input(f"Дата начала проката: ") or current.rental_date
            return_date = input(f"Дата возврата: ") or current.return_date
            rental_price = input(f"Стоимость проката: ") or current.rental_price

            print("Доступные сотрудники:")
            employees = get_all_employees()
            for e in employees:
                print(f"{e.employee_id}. {e.first_name} {e.last_name}")
            employee_id = input(f"ID сотрудника: ") or current.employee_id

            updated = Rental(
                rental_id=id_to_edit, client_id=client_id, movie_id=movie_id,
                rental_date=rental_date, return_date=return_date, rental_price=rental_price,
                employee_id=int(employee_id)
            )
            updated.save()
            print("✅ Запись проката обновлена.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
