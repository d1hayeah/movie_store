from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_movies import menu_movies
from ui.menu_clients import menu_clients
from ui.menu_suppliers import menu_suppliers
from ui.menu_orders import menu_orders
from ui.menu_employees import menu_employees  
from ui.menu_rentals import menu_rentals      

def main():
    initialize_db()
    while True:
        user_choice = show_main_menu()
        if user_choice == "1":
            menu_movies()
        elif user_choice == "2":
            menu_clients()
        elif user_choice == "3":
            menu_suppliers()
        elif user_choice == "4":
            menu_orders()
        elif user_choice == "5":
            menu_employees()  
        elif user_choice == "6":
            menu_rentals()   
        elif user_choice == "0":
            print("Выход из программы.")
            break
        else:
            print("❌ Неверный ввод.")

if __name__ == "__main__":
    main()



