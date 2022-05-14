s = 'abracadabraab'
s1 = s.find('ab')
s2 = s.rfind('ab')
s3 = s.rfind('ab')
print(s1)
print(s2)
print(s3)

s1 = 'Hello'
print(s1.startswith('bye'))

s = 'Good morning'
s += s1
print(s)
s *= 3
print(s)

s7 = 'HEllo heNIntsoa, BYE'
s9 = list(s7)
for s in s9:
    if s.islower():
        index = s9.index(s)
        s9[index] = s.upper()
print(s9)
s10 = ''.join(s9)
print(s10)

name = "Аркадий"
age = 14
print(f"Меня зовут {name} Мне {age} лет.")


