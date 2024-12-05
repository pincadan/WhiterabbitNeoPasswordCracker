import hashlib
import itertools
import string

def crack_password(hashed_password, password_length):
    """
    Cracks a SHA-256 hashed password of a given length.
    
    Args:
        hashed_password (str): The SHA-256 hashed password to crack.
        password_length (int): The length of the password to crack.
        
    Returns:
        str: The cracked password, or None if the password could not be cracked.
    """
    # Define the character set to use for password generation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate all possible password combinations
    password_combinations = itertools.product(characters, repeat=password_length)
    
    # Iterate through each password combination
    for password_tuple in password_combinations:
        password = ''.join(password_tuple)
        
        # Hash the generated password
        hashed_guess = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # Check if the hashed guess matches the target hashed password
        if hashed_guess == hashed_password:
            return password
    
    # If no password is found, return None
    return None

# Example usage
hashed_password = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
password_length = 8

cracked_password = crack_password(hashed_password, password_length)

if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password could not be cracked.")