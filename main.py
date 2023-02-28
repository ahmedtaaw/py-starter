name="Bob"
greetings="hello,{}, Today is {}"

with_name = greetings.format(name,"today")
with_name2 = greetings.format(name,"Monday")
print(with_name)
print(with_name2)


size_input = input("How big is your house");
square_feet = int(size_input);
square_metres = square_feet/10.8;

print(f"{square_feet} square feet is {square_metres:.2f} square metres.")