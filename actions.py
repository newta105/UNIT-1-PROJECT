from pet import Pet

def feed_pet(pet):
    pet.feed()
    print(f"{pet.name} has been fed.")

def play_with_pet(pet):
    pet.play()
    print(f"{pet.name} is happy after playing with you.")

def put_to_sleep(pet):
    pet.sleep()
    print(f"{pet.name} is sleeping peacefully.")

def check_status(pet):
    status = pet.get_status()
    print(f"Status of {pet.name}:")
    print(f"Hunger: {status['hunger']}")
    print(f"Happiness: {status['happiness']}")
    print(f"Energy: {status['energy']}")
