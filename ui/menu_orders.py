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
                print(f"{o.order_id}. Фильм: {movie_title} | Клиент ID: {o.client_id} | Дата продажи: {o.sale_date or '-'} | Кол-во: {o.quantity} | Сумма: {o.total_price} руб.")

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

            quantity = int(input("Количество: "))
            movie = get_movie_by_id(movie_id)
            total_price = movie.price * quantity if movie else 0

            sale_date = input("Дата продажи (YYYY-MM-DD): ")

            order = Order(
                movie_id=movie_id,
                client_id=client_id,
                sale_date=sale_date,
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
            
            print("Оставьте поле пустым, чтобы не изменять.")
            quantity = input(f"Количествo: ") or current.quantity
            sale_date = input(f"Дата продажи: ") or current.sale_date
            movie = get_movie_by_id(current.movie_id)
            if movie:
                total_price = movie.price * int(quantity) 
            else:
                total_price = 0

            updated = Order(
                order_id=id_to_edit,
                movie_id=current.movie_id,
                client_id=current.client_id,
                sale_date=sale_date,
                quantity=quantity,
                total_price=total_price
            )
            updated.save()
            print("✅ Заказ обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")
