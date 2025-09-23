# Program 1
s = input("String: ")
print(s.swapcase())

# Program 2
s = "X-DSPAM-Confidence:0.8475"
print(s.find(":"))
value = s[19:25]
print(value)
print(type(value))

x = float(value)
print(type(x))

# convert
s = "luckynumber27"
print(s.find("r"))
value = s[11:]
print(value)
print(type(value))

convert = int(value)
print(type(convert))

# Program 3
vc, cc, sp, ss, d = 0, 0, 0, 0, 0
s = input("Enter a string: ")

for ch in s:
    # vowel count
    if ch in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        vc += 1
    # consonant count
    elif ch.isalpha() and ch not in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        cc += 1
    elif ch in ["%", "$", "!", ".", "'"]:
        ss += 1
    elif ch in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        d += 1
    elif ch == " ":
        sp += 1

print(f"vowels = {vc}")
print(f"consonants = {cc}")
print(f"spaces = {sp}")
print(f"special symbols = {ss}")
print(f"digits = {d}")

# Program 4
s = "A quick brown fox jumps over the lazy dog."
print(s.replace(" ", ",", 5))

# s.replace
s = "I am learning C, C is easy."
print(s.replace("C", "Python", 1))