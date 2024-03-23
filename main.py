import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'

def get_data():
    response = requests.get(url)
    data = response.json()
    return data

def parse_currency_data(data):
    currencies = []
    for currency_code in data['Valute']:
        currency = data['Valute'][currency_code]
        currencies.append({
            "CharCode": currency_code,
            "Name": currency["Name"],
            "Value": currency["Value"],
            "Previous": currency["Previous"],
        })
    return currencies

def create_hash_table(data):
    currency_table = {}
    for currency in data:
        currency_table[currency['CharCode']] = {
            "Name": currency["Name"],
            "Value": currency["Value"],
            "Previous": currency["Previous"],
        }
    return currency_table

def get_currency_info(currency_hash_table, currency_query):   
    for currency_code, data in currency_hash_table.items():
        if currency_query in (currency_code, data['Name']):
            return data 
    return None

def validate_currency(currency_hash_table, currency_query):
    if currency_query in currency_hash_table:
        return True
    else:
        suggestions = []
        for currency_code, data in currency_hash_table.items():
            if 'Name' in data and currency_query.lower() in data['Name'].lower():
                suggestions.append(f"{currency_code} ({data['Name']})") 
        if suggestions:
            print(f"Валюта '{currency_query}' не найдена. Возможно, Вы имели в виду:")
            for suggestion in suggestions:
                print(f" * {suggestion}")
        else:
            print(f"Валюта '{currency_query}' не найдена.")
        return False
    
data = get_data()
cur = parse_currency_data(data)
table = create_hash_table(cur)
while True:
    resp = input("Введите код валюты: ").upper()
    if validate_currency(table, resp):
        break
currency_info = get_currency_info(table, resp)

if currency_info is not None:
    print(f"Код валюты: {resp}")
    print(f"Название валюты: {currency_info['Name']}")
    print(f"Текущий курс: {currency_info['Value']}")
    print(f"Предыдущий курс: {currency_info['Previous']}")
else:
    print(f"Валюта с кодом {resp} не найдена.")