import requests

#This is a module where we can get all other data
# from other external services needed


def get_customer_data(customer_id):
    response = requests.get(f'https://transafe.api.com/customers/{transafe_customer_id}')
    if response.status_code == 200:
        return response.json()
    else:
        return None
