import requests

# This is a module where we can get all other data
# from other external services needed

def get_customer_data(customer_id):
    try:
        response = requests.get(f'https://jsonplaceholder.typicode.com/users/{customer_id}')
        response.raise_for_status()  # Raise an exception if response status code is not 200
        data = response.json()
        customer_data = {'id': data['id'], 'name': data['name'], 'email': data['email']}
        return customer_data
    except (requests.exceptions.RequestException, KeyError):
        return None

customer_data = get_customer_data(4)
if customer_data:
    print(customer_data)
else:
    print("Failed to retrieve customer data.")
