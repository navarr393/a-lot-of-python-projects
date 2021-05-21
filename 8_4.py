def make_tshirt(size = 'Large', message = 'I love Python'):
    print(f"\nThe size of the shirt is {size}.")
    print(f'The message on the shirt is "{message}".')

#default size and message
make_tshirt()

#medium shirt with default message
make_tshirt('Medium')

#tshirt with different size and message
make_tshirt('Small', 'I love C++')
