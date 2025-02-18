import string, random
import image_generator as ig

def main():

    # a method which generates the random data to be processed
    def generate_data():
        def generate_random_strings(length):
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

        random_string = generate_random_strings(10)
        ig.generate_image(random_string)

    generate_data()

main()