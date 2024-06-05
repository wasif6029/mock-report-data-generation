import random
import uuid

from faker import Faker

from agent_cluster import get_agent_data_by_cluster, get_random_agent_cluster
from bank_cluster import get_random_bank_cluster, get_bank_data_by_cluster
from src.cluster import get_random_customer_cluster, get_customer_data_by_cluster
from merchant_cluster import get_random_merchant_cluster, get_merchant_data_by_cluster



number_of_customers = 50000
number_of_agents = 1500
number_of_merchants = 100
number_of_banks = 20

def custom_round(value):
    # Get the integer part and decimal part of the value
    integer_part = int(value)
    decimal_part = value - integer_part

    # Determine the nearest .00, .25, .50, or .75
    if decimal_part < 0.125:
        decimal_part = 0.00
    elif decimal_part < 0.375:
        decimal_part = 0.25
    elif decimal_part < 0.625:
        decimal_part = 0.50
    elif decimal_part < 0.875:
        decimal_part = 0.75
    else:
        decimal_part = 0.00
        integer_part += 1

    return integer_part + decimal_part


# generate 10000 data
def generate_customer_data():
    fake = Faker()
    customer_data = []
    for i in range(1000001, 1000001 + number_of_customers):
        name = fake.name()
        cluster = get_random_customer_cluster()
        balance = custom_round(
            random.uniform(*get_customer_data_by_cluster(cluster)["initial_balance_range"]["normal"]))
        id = None
        idpId = uuid.uuid4()
        account_name = fake.name()
        customer_data.append({"name": name, "account_number": i, "cluster": cluster, "balance": balance, "merchant_id": id, "idp_id":idpId, "account_name": account_name})
    return customer_data


# generate 1000 agent data
def generate_agent_data():
    fake = Faker()
    agent_data = []
    for i in range(2000001, 2000001+number_of_customers):
        name = fake.name()
        cluster = get_random_agent_cluster()
        balance = custom_round(random.uniform(*get_agent_data_by_cluster(cluster)["initial_balance_range"]["normal"]))
        id = None
        idpId = uuid.uuid4()
        account_name = fake.name()
        agent_data.append({"name": name, "account_number": i, "cluster": cluster, "balance": balance,  "merchant_id": id, "idp_id": idpId, "account_name": account_name})
    return agent_data


def generate_merchant_data():
    fake = Faker()
    merchant_data = []
    for i in range(3000001, 3000001+number_of_merchants):
        name = fake.name()
        cluster = get_random_merchant_cluster()
        balance = custom_round(
            random.uniform(*get_merchant_data_by_cluster(cluster)["initial_balance_range"]["normal"]))
        id = uuid.uuid4()
        idpId = None
        account_name = fake.name()
        merchant_data.append({"name": name, "account_number": i, "cluster": cluster, "balance": balance, "merchant_id": id, "idp_id": idpId, "account_name": account_name})
    return merchant_data


def generate_bank_data():
    merchant_data = []
    for i in range(4000001, 4000001+number_of_banks):
        name = 'Bank of Trinidad and Tobago'
        cluster = get_random_bank_cluster()
        balance = custom_round(random.uniform(*get_bank_data_by_cluster(cluster)["initial_balance_range"]["normal"]))
        id = None
        idpId = None
        account_name = None
        merchant_data.append({"name": name, "account_number": i, "cluster": cluster, "balance": balance,  "merchant_id": id, "idp_id": idpId, "account_name": account_name})
    return merchant_data


# convert to customer.csv
def generate_customer_csv():
    customer_data = generate_customer_data()
    with open("C://Users//BS1123//PycharmProjects//TransactionReport//src//data//customer.csv", "w") as f:
        f.write("name,account_number,cluster,balance,merchant_id,idp_id,account_name\n")
        for customer in customer_data:
            f.write(f"{customer['name']},{customer['account_number']},{customer['cluster']},{customer['balance']},{customer['merchant_id']},{customer['idp_id']},{customer['account_name']}\n")


# write methods fot converting agent , merchant and bank data to csv
def generate_agent_csv():
    agent_data = generate_agent_data()
    with open("C://Users//BS1123//PycharmProjects//TransactionReport//src//data//agent.csv", "w") as f:
        f.write("name,account_number,cluster,balance,merchant_id,idp_id,account_name\n")
        for agent in agent_data:
            f.write(f"{agent['name']},{agent['account_number']},{agent['cluster']},{agent['balance']},{agent['merchant_id']},{agent['idp_id']},{agent['account_name']}\n")


def generate_merchant_csv():
    merchant_data = generate_merchant_data()
    with open("C://Users//BS1123//PycharmProjects//TransactionReport//src//data//merchant.csv", "w") as f:
        f.write("name,account_number,cluster,balance,merchant_id,idp_id,account_name\n")
        for merchant in merchant_data:
            f.write(f"{merchant['name']},{merchant['account_number']},{merchant['cluster']},{merchant['balance']},{merchant['merchant_id']},{merchant['idp_id']},{merchant['account_name']}\n")


# do same for bank
def generate_bank_csv():
    bank_data = generate_bank_data()
    with open("C://Users//BS1123//PycharmProjects//TransactionReport//src//data//bank.csv", "w") as f:
        f.write("name,account_number,cluster,balance,merchant_id,idp_id,account_name\n")
        for bank in bank_data:
            f.write(f"{bank['name']},{bank['account_number']},{bank['cluster']},{bank['balance']},{bank['merchant_id']},{bank['idp_id']},{bank['account_name']}\n")


generate_customer_csv()
generate_bank_csv()
generate_agent_csv()
generate_merchant_csv()
