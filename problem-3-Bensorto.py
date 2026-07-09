age = 17

print("I am " + 17 + " years old")
TypeError: can only concatenate str (not "int") to str
String and number are being combined
Python cannot use `+` directly between text and a number on line 3 (`print("I am " + 17 + " years old")`).
Convert the string to a number with `int()` or `float()` before arithmetic.
Convert the number to text with `str()` before joining strings.
Example fix

age = 17

print("I am " + str(17) + " years old")
print(f"I am {17} years old")
I am 17 years old
I am 17 years old
