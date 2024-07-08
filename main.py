from pet import Pet
from actions import check_status, feed_pet, play_with_pet, put_to_sleep, check_status

def main():
    print("Welcome to the Virtual Pet Simulator!")
    name = input("Enter the name of your pet: ")
    pet = Pet(name)
    print(f"{name} is ready to play!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed Pet")
        print("2. Play with Pet")
        print("3. Put Pet to Sleep")
        print("4. Check Pet Status")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            feed_pet(pet)
        elif choice == '2':
            play_with_pet(pet)
        elif choice == '3':
            put_to_sleep(pet)
        elif choice == '4':
            check_status(pet)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
