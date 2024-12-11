def sort(width, height, length, mass):
    # Calculate volume
    volume = width * height * length
    
    # Determine if the package is bulky
    is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if the package is heavy
    is_heavy = mass >= 20
    
    # Determine the stack for the package
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def get_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "$":
            print("Exiting...")
            return None
        try:
            value = float(user_input)
            if value <= 0:
                print("Invalid input. Please enter a positive number or '$' to exit.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number or '$' to exit.")

# Example usage
if __name__ == "__main__":
    width = get_input("Enter width: ")
    if width is None: exit()
    height = get_input("Enter height: ")
    if height is None: exit()
    length = get_input("Enter length: ")
    if length is None: exit()
    mass = get_input("Enter mass: ")
    if mass is None: exit()
    print(sort(width, height, length, mass))