import requests

def currency_converter(base_currency, target_currency, amount):
    api_key = '6d5025f34712b80efd1d73d4'
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}'
    try:
        response = requests.get(url)
        response_json = response.json()
        if response.status_code == 200 and response_json['result'] == 'success':
            return f'{amount} {base_currency} = {response_json['conversion_result']:.2f} {target_currency}'
        else:
            return 'Error!'
    except requests.exceptions.RequestException as e:
        return f'Network error: {e}'
    except KeyError:
        return 'Unexpected API response. Please check your inputs'
    except ValueError:
        return 'Please enter a valid number for the amount'

try:
    base_currency = input('Enter a base currency: ').upper()
    target_currency = input('Enter a target_currency: ').upper()
    amount = int(input('Enter a amount: '))
    print(currency_converter(base_currency=base_currency, target_currency=target_currency, amount=amount))
except ValueError:
    print('Invalid input. Please enter a numeric value for the amount')