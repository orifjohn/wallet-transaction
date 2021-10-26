import random

PREFIX = '8600'


def generate_wallet_id():
    generated_wallet_id = PREFIX
    for _ in range(12):
        generated_wallet_id += str(random.randint(0, 9))
    return generated_wallet_id
