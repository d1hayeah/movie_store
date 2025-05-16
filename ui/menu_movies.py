from models.film_model import Films, get_all_movies, get_movie_by_id

def menu_movies():
    while True:
        print("\n=== Фильмы ===")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Удалить фильм")
        print("4. Изменить фильм")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")

        if choice == "1":
            movies = get_all_movies()
            print("\nСписок фильмов:")
            for m in movies:
                print(f"{m.movie_id}. {m.title} | Режиссер: {m.director} | Жанр: {m.genre}")

        elif choice == "2":
            print("\n=== Добавление фильма ===")
            title = input("Название: ")
            director = input("Режиссер: ")
            genre = input("Жанр: ")
            actors = input("Актеры: ")
            format = input("Формат (DVD/Blu-ray): ")
            release_year = int(input("Год выпуска: "))
            stock = int(input("Количество на складе: "))
            price = int(input("Цена: "))
            movie = Films(title=title, director=director, genre=genre, actors=actors,
                          format=format, release_year=release_year, stock_quantity=stock, price=price)
            movie.save()
            print("✅ Фильм добавлен.")

        elif choice == "3":
            id_to_delete = input("ID фильма для удаления: ")
            movie = Films(movie_id=int(id_to_delete))
            movie.delete()
            print("❌ Фильм удален.")

        elif choice == "4":
            id_to_edit = int(input("ID фильма для редактирования: "))
            current = get_movie_by_id(id_to_edit)
            if not current:
                print("❌ Фильм не найден!")
                continue

            print("Оставьте поле пустым, чтобы не изменять.")
            title = input(f"Новое названи: ") or current.title
            director = input(f"Новый режиссер: ") or current.director
            genre = input(f"Новый жанр: ") or current.genre
            actors = input(f"Новые актеры: ") or current.actors
            format = input(f"Новый формат: ") or current.format
            release_year = input(f"Новый год: ") or current.release_year
            stock = input(f"Новое количество: ") or current.stock_quantity
            price = input(f"Новая цена: ") or current.price 
            updated = Films(movie_id=id_to_edit, title=title, director=director, genre=genre,
                            actors=actors, format=format, release_year=int(release_year),
                            stock_quantity=int(stock), price=int(price))
            updated.save()
            print("✅ Фильм обновлён.")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод.")