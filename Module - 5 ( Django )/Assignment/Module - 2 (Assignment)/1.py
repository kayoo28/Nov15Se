def generate_even_numbers():
    for num in range(2, 21, 2):
        yield num

gen = generate_even_numbers()
for i in gen:
    print(i)