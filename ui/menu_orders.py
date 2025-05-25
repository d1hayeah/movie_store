from models.order_model import Order, get_all_orders, get_order_by_id
from models.employee_model import get_all_employees, get_employee_by_id
from models.client_model import get_all_clients, get_client_by_id
from models.film_model import get_all_movies, get_movie_by_id

def menu_orders():
    while True:
        print("\n=== Заказы ===")
        print("1. Показать все заказы")
        print("2. Добавить заказ")
        print("3. Удалить заказ")
        print("4. Изменить заказ")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            orders = get_all_orders()
            print("\nСписок заказов:")
            for o in orders:
                employee = get_employee_by_id(o.employee_id)
                employee_str = f"{employee.first_name} {employee.last_name}" if employee else "Неизвестно"
                client = get_client_by_id(o.client_id)
                client_str = client.name if client else f"ID {o.client_id}"
                movie = get_movie_by_id(o.movie_id)
                movie_str = movie.title if movie else f"ID {o.movie_id}"
                print(f"{o.order_id}. Клиент: {client_str} | Фильм: {movie_str} | Дата продажи: {o.sale_date} | Тип: {o.type} | Кол-во: {o.quantity} | Сумма: {o.total_price} | Сотрудник: {employee_str}")

        elif choice == "2":
            print("\n=== Добавление заказа ===")
            print("Доступные клиенты:")
            clients = get_all_clients()
            for c in clients:
                print(f"{c.client_id}. {c.name}")
            client_id = int(input("ID клиента: "))

            print("Доступные фильмы:")
            movies = get_all_movies()
            for m in movies:
                print(f"{m.movie_id}. {m.title}")
            movie_id = int(input("ID фильма: "))

            sale_date = input("Дата продажи (YYYY-MM-DD): ")
            type = input("Тип диска (Blu-ray/DVD): ")
            quantity = int(input("Количество: "))
            total_price = int(input("Сумма заказа: "))

            print("Доступные сотрудники:")
            employees = get_all_employees()
            for e in employees:
                print(f"{e.employee_id}. {e.first_name} {e.last_name}")
            employee_id = int(input("ID сотрудника: "))

            order = Order(movie_id=movie_id, client_id=client_id, sale_date=sale_date, type=type, quantity=quantity, total_price=total_price, employee_id=employee_id)
            order.save()
            print("✅ Заказ добавлен.")

        elif choice == "3":
            id_to_delete = input("Введите ID заказа: ")
            order = Order(order_id=int(id_to_delete))
            order.delete()
            print("❌ Заказ удалён.")

        elif choice == "4":
            id_to_edit = int(input("ID заказа: "))
            current = get_order_by_id(id_to_edit)
            if not current:
                print("❌ Заказ не найден!")
                continue

            print("Оставьте поле пустым, чтобы не изменять.")
            print("Доступные клиенты:")
            clients = get_all_clients()
            for c in clients:
                print(f"{c.client_id}. {c.name}")
            client_id = input("ID клиента: ") or current.client_id

            print("Доступные фильмы:")
            movies = get_all_movies()
            for m in movies:
                print(f"{m.movie_id}. {m.title}")
            movie_id = input("ID фильма: ") or current.movie_id

            sale_date = input("Дата продажи: ") or current.sale_date
            type = input("Тип заказа: ") or current.type
            quantity = input("Количество: ") or current.quantity
            total_price = input("Сумма заказа: ") or current.total_price

            print("Доступные сотрудники:")
            employees = get_all_employees()
            for e in employees:
                print(f"{e.employee_id}. {e.first_name} {e.last_name}")
            employee_id = input("ID сотрудника: ") or current.employee_id

            updated = Order(
                order_id=id_to_edit,
                movie_id=int(movie_id),
                client_id=int(client_id),
                sale_date=sale_date,
                type=type,
                quantity=int(quantity),
                total_price=int(total_price),
                employee_id=int(employee_id)
            )
            updated.save()
            print("✅ Заказ обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
