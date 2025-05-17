from models.order_model import Order, get_all_orders, get_order_by_id
from models.film_model import Films, get_all_movies, get_movie_by_id
from models.client_model import get_all_clients

def menu_orders():
    while True:
        print("\n=== Заказы ===")
        print("1. Показать все заказы")
        print("2. Добавить заказ")
        print("3. Удалить заказ")
        print("4. Редактирование заказа")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            orders = get_all_orders()
            print("\nСписок заказов:")
            for o in orders:
                movie = get_movie_by_id(o.movie_id) if o.movie_id else None
                movie_title = movie.title if movie else "-"
                print(f"{o.order_id}. Фильм: {movie_title} | Клиент ID: {o.client_id} | Тип: {o.type} | Продажа: {o.sale_date or '-'} | Прокат: {o.rental_date or '-'} - {o.return_date or '-'} | Кол-во: {o.quantity} | Сумма: {o.total_price} руб.")

        elif choice == "2":
            print("Доступные клиенты:")
            clients = get_all_clients()
            for c in clients:
                print(f"{c.client_id}. {c.name}")
            client_id = int(input("Введите ID клиента: "))

            print("Доступные фильмы:")
            movies = get_all_movies()
            for m in movies:
                print(f"{m.movie_id}. {m.title} (На складе: {m.stock_quantity})")
            movie_id = int(input("Введите ID фильма: "))

            order_type = input("Тип заказа (sale - продажа, rental - прокат): ").strip().lower()
            quantity = int(input("Количество: "))
            movie = get_movie_by_id(movie_id)
            total_price = None
            if movie:
                total_price = movie.price * quantity
            else:
                total_price = 0

            sale_date = None
            rental_date = None
            return_date = None

            if order_type == "sale":
                sale_date = input("Дата покупки (YYYY-MM-DD): ") 
                print('Стоимость: {total_price}')
            elif order_type == "rental":
                rental_date = input("Дата начала проката (YYYY-MM-DD): ") 
                return_date = input("Дата возврата (YYYY-MM-DD): ")
                total_price = movie.price * quantity / 6
                print(f'Стоимость проката: {total_price}')
            else:
                print("❌ Неверный тип заказа.")
                continue

            order = Order(
                movie_id=movie_id,
                client_id=client_id,
                sale_date=sale_date,
                type=order_type,
                rental_date=rental_date,
                return_date=return_date,
                quantity=quantity,
                total_price=total_price
            )
            order.save()
            print("✅ Заказ добавлен.")

        elif choice == "3":
            id_to_delete = input("Введите ID заказа для удаления: ")
            order = Order(order_id=int(id_to_delete))
            order.delete()
            print("❌ Заказ удален.")
            
        elif choice == "4":
            print("Доступные заказы:")
            orders = get_all_orders()
            for o in orders:
                print(f"{o.order_id}")
            id_to_edit = int(input("ID заказа для редактирования: "))
            current = get_order_by_id(id_to_edit)
            if not current:
                print("❌ Заказ не найден!")
                continue
            
            total_price = None
            sale_date = None
            rental_date = None
            return_date = None
            movie = get_movie_by_id(current.movie_id)
            print("Оставьте поле пустым, чтобы не изменять.")
            quantity = input(f"Количество: ") or current.quantity
            order_type = input(f"Тип заказа(sale - продажа, rental - прокат): ") or current.type
            if order_type == "sale":
                sale_date = input("Дата покупки (YYYY-MM-DD): ") 
                if movie:
                    total_price = int(movie.price * quantity)
                else:
                    total_price = 0
            elif order_type == "rental":
                rental_date = input("Дата начала проката (YYYY-MM-DD): ") 
                return_date = input("Дата возврата (YYYY-MM-DD): ")
                total_price = movie.price * int(quantity) / 6
            else:
                print("❌ Неверный тип заказа.")
                continue
            
            
            updated = Order(
                order_id=id_to_edit,
                movie_id=current.movie_id,
                client_id=current.client_id,
                type=order_type,
                rental_date=rental_date,
                return_date=return_date,
                quantity=quantity,
                total_price=total_price
            )
            updated.save()
            print("✅ Фильм обновлён.")
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
