import re

def password_strength(password):
    # Criteria flags
    length_flag = len(password) >= 8
    uppercase_flag = re.search(r'[A-Z]', password) is not None
    lowercase_flag = re.search(r'[a-z]', password) is not None
    number_flag = re.search(r'\d', password) is not None
    special_char_flag = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Calculate strength score
    strength_score = sum([length_flag, uppercase_flag, lowercase_flag, number_flag, special_char_flag])
    
    # Feedback based on strength score
    if strength_score == 5 and len(password) >= 12:
        feedback = "Very Strong"
    elif strength_score == 5:
        feedback = "Strong"
    elif strength_score == 4:
        feedback = "Moderate"
    elif strength_score == 3:
        feedback = "Weak"
    else:
        feedback = "Very Weak"
    
    return feedback

# Test the function
passwords = ["12345", "Password", "Passw0rd!", "StrongPassw0rd!", "Very$tr0ngPassw0rd123"]
for pwd in passwords:
    print(f"Password: {pwd}, Strength: {password_strength(pwd)}")
