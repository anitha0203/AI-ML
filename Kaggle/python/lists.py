def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) == 2:
        return L[1]
    return None

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='')  

squares = [n**2 for n in range(10)]
print(squares)

