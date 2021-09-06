catalogue = {
        'iphone': {
            'X': 800,
            'XR': 900,
            '11': 1000,
            '12': 1200,
        },
        'ipad': {
            'mini': 400,
            'air': 500,
            'pro': 800,
        },
        'mac': {
            'macbook air': 999,
            'macbook': 1299,
            'macbook pro': 1799,
        }
    }

for key, value in catalogue.items():
    print('-' * 10)
    print(key)
    for k, v in value.items():
        print(k, '', v)
print(' ')
print('='*64)
for key, value in catalogue.items():
    print(f"which {key} would you like to purchase together with quantity")
    for k, v in value.items():
        print(k)
