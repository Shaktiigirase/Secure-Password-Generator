import random
import string

def generate_password(length=16):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Define the characters to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuations = string.punctuation
    
    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(punctuations)
    ]
    
    # Fill the rest of the password length with random choices
    all_characters = lower + upper + digits + punctuations
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
print(generate_password(16))  # You can specify the desired password length
