name="Bob"
greetings="hello,{}, Today is {}"

with_name = greetings.format(name,"today")
with_name2 = greetings.format(name,"Monday")
print(with_name)
print(with_name2)
