from random import randint

from captcha.image import ImageCaptcha


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)

num = random_with_N_digits(int(input("Enter number of digits:")))
name = f"{num}.png"
image = ImageCaptcha()
data = image.generate(f"'{num}'")
image.write(f"'{num}'", name)
print(f"A {num}.png is generated")