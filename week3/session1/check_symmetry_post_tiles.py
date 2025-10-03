def is_symmetrical_title(title):
    # s = "".join(char for char in title if char.isalpha()).lower()
    s = ""
    for char in title:
        if char.isalpha():
            s += char.lower()
    
    left,right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

# Planning
    # Initialize two pointers