def make_tshirt(size, message):
    print(f"The size of the shirt is {size}.")
    print(f'The message on the shirt is "{message}".')

#positional arguments 
make_tshirt('Small', 'Hello world!')

#keyword arguments
make_tshirt(message='Hello world!', size='Medium')
