import pandas as pd
import random
import uuid
import decimal
from datetime import datetime, timedelta, timezone
import pyodbc

from src.transaction_report_repository import batch_insert_transactions
from src.type_wise_transaction_configuration import configure_transaction_configuration

# Define transaction types with their probabilities
status_distribution = {
    'PENDING': 0.14,
    'FAILED': 0.05,
    'SUCCESSFUL': 0.8,
    'REVERSED': 0.01,
}

categories = [{'id': str(uuid.uuid4())} for _ in range(100)]
subsidies = [{'id': str(uuid.uuid4())} for _ in range(1000)]

transaction_type_distribution = {
    'ADD_MONEY_FROM_BANK': 0.05,
    'ADD_MONEY_FROM_CARD': 0.05,
    'SEND_MONEY': 0.3,
    'MERCHANT_PAYMENT': 0.1,
    'MERCHANT_PAYMENT_REFUND': 0.05,
    'CASH_IN': 0.07,
    'CASH_OUT': 0.07,
    'WALLET_TO_BANK': 0.05,
    'BANK_PARKING_TO_BANK_TRANSFER': 0.001,
    'BRANCH_TO_MERCHANT': 0.001,
    'MERCHANT_TO_BRANCH': 0.001,
    'MERCHANT_TO_BANK_TRANSFER': 0.005,
    'MERCHANT_GATEWAY_TRANSACTION': 0.005,
    'AGENT_ADD_FUND': 0.01,
    'AGENT_FLOAT_COLLECTION': 0.001,
    'SUBSIDY_RESERVE_PAYMENT': 0.001,
    'SUBSIDY_RELEASE_PAYMENT': 0.001,
    'SUBSIDY_CASHBACK_PAYMENT': 0.08,
    'SUBSIDY_DIRECT_DISBURSEMENT': 0.05,
    'CHARITY_PAYMENT': 0.001,
    'HELPING_HAND_CREATION_FEE': 0.01,
    'COMMISSION_PAYMENT': 0.05,
    'INCENTIVE_PAYMENT': 0.042,
    'CHARITY_BALANCE_TRANSFER': 0.001
}

# Mapping from transaction_code to transaction_type
transaction_code_to_type = {
    "CB2CW": "ADD_MONEY_FROM_BANK",
    "CC2CW": "ADD_MONEY_FROM_CARD",
    "CW2CW": "SEND_MONEY",
    "CW2MW": "MERCHANT_PAYMENT",
    "MW2CW": "MERCHANT_PAYMENT_REFUND",
    "AW2CW": "CASH_IN",
    "CW2AW": "CASH_OUT",
    "CW2CB": "WALLET_TO_BANK",
    "BPA2BA": "BANK_PARKING_TO_BANK_TRANSFER",
    "BW2MW": "BRANCH_TO_MERCHANT",
    "MW2BW": "MERCHANT_TO_BRANCH",
    "MW2BA": "MERCHANT_TO_BANK_TRANSFER",
    "MWGTRN": "MERCHANT_GATEWAY_TRANSACTION",
    "AFBAF": "AGENT_ADD_FUND",
    "AFBFC": "AGENT_FLOAT_COLLECTION",
    "SPA2SA": "SUBSIDY_RESERVE_PAYMENT",
    "SA2SPA": "SUBSIDY_RELEASE_PAYMENT",
    "SA2SRWCB": "SUBSIDY_CASHBACK_PAYMENT",
    "SA2SRWDD": "SUBSIDY_DIRECT_DISBURSEMENT",
    "CP2ORGW": "CHARITY_PAYMENT",
    "SF_HHC": "HELPING_HAND_CREATION_FEE",
    "CP2AW": "COMMISSION_PAYMENT",
    "IP2CW": "INCENTIVE_PAYMENT",
    "CHW2ORGW": "CHARITY_BALANCE_TRANSFER"
}

# Load CSV data
agents = pd.read_csv('C://Users//BS1123//PycharmProjects//TransactionReport//src//data//agent.csv')
customers = pd.read_csv('C://Users//BS1123//PycharmProjects//TransactionReport//src//data//customer.csv')
banks = pd.read_csv('C://Users//BS1123//PycharmProjects//TransactionReport//src//data//bank.csv')
merchants = pd.read_csv('C://Users//BS1123//PycharmProjects//TransactionReport//src//data//merchant.csv')

idp_id_list = customers['idp_id'].tolist()
merchant_id_list = merchants['merchant_id'].tolist()

# Helper functions
def get_random_element(df, column):
    return df[column].sample().values[0]

def generate_uuid():
    return str(uuid.uuid4())

def generate_big_decimal(min_value=0, max_value=10000, precision=19, scale=2):
    value = decimal.Decimal(random.uniform(min_value, max_value))
    return value.quantize(decimal.Decimal('.' + '0' * (scale - 1) + '1'), rounding=decimal.ROUND_HALF_UP)

def generate_datetime():
    return datetime.now() - timedelta(days=random.randint(0, 365))

def generate_offset_datetime():
    return datetime.now(timezone.utc).astimezone()

def choose_transaction_type():
    return random.choices(list(transaction_type_distribution.keys()), weights=transaction_type_distribution.values(), k=1)[0]

def choose_status():
    return random.choices(list(status_distribution.keys()), weights=status_distribution.values(), k=1)[0]

def get_transaction_code(transaction_type):
    for code, type_ in transaction_code_to_type.items():
        if type_ == transaction_type:
            return code
    return 'TXN_CODE'

# Function to generate transaction based on type
def generate_transaction(transaction_type):
    transaction_code = get_transaction_code(transaction_type)
    sender_idp_id = random.choice(idp_id_list)
    receiver_idp_id = random.choice(idp_id_list)
    merchant_id = random.choice(merchant_id_list)
    branch_id = random.choice(merchant_id_list)


    base_transaction = {
        'id': generate_uuid(),
        'created_by': 'system',
        'updated_by': 'system',
        'create_date_time': generate_offset_datetime(),
        'update_date_time': generate_offset_datetime(),
        'is_deleted': 0,
        'request_id': generate_uuid(),
        'transaction_id': generate_uuid(),
        'workflow_request_id': generate_uuid(),
        'transaction_type': transaction_type,
        'transaction_code': transaction_code,
        'from_account_name': 'from_account_name',
        'to_account_name': 'to_account_name',
        'from_internal_account': 'from_internal_account',
        'to_internal_account': 'to_internal_account',
        'sender_account_type': random.choice(['CUSTOMER', 'MERCHANT', 'AGENT', 'WALLET_AUTHORITY', 'ORGANIZATION', 'BANK', 'CARD', 'PARKING']),
        'receiver_account_type': random.choice(['CUSTOMER', 'MERCHANT', 'AGENT', 'WALLET_AUTHORITY', 'ORGANIZATION', 'BANK', 'CARD', 'PARKING']),
        'bank_transaction_reference': 'bank_ref',
        'amount': generate_big_decimal(),
        'fee_amount': generate_big_decimal(0, 100),
        'fee_payer': 'fee',
        'vat_amount': generate_big_decimal(0, 100),
        'vat_payer': 'vat',
        'sender_debit_amount': generate_big_decimal(),
        'receiver_credit_amount': generate_big_decimal(),
        'withdrawer_running_balance': generate_big_decimal(),
        'depositor_running_balance': generate_big_decimal(),
        'user_note': 'user_note',
        'remarks': 'remarks',
        'status': choose_status(),
        'dispute_status': random.choice([None]),
        'dispute_remarks': 'dispute_remarks',
        'original_transaction_reference_for_reversal': None,
        'transaction_date_time': generate_datetime(),
        'sender_idp_id': sender_idp_id,
        'receiver_idp_id': receiver_idp_id,
        'from_account': sender_idp_id,
        'to_account': receiver_idp_id,
        'transaction_category_id': random.choice(categories)['id'],
        'sender_country_code': '+1868',
        'sender_phone_number': sender_idp_id,
        'receiver_country_code': '+1868',
        'receiver_phone_number': receiver_idp_id,
        'transaction_reference': generate_uuid(),
        'branch_id': branch_id,
        'merchant_id': merchant_id,
        'reversed_transaction_ref': 'reversed_transaction_ref',
        'fee_description': 'fee_description',
        'fee_payer_internal_account': sender_idp_id[:5],
        'vat_payer_internal_account': sender_idp_id[:5],
        'subsidy_id': random.choice(subsidies)['id'],
        'subsidy_amount': generate_big_decimal(),
        'subsidy_type': random.choice(['NO_SUBSIDY', 'DIRECT', 'DISCOUNT', 'CASHBACK']),
        'incentive_payment_type': random.choice(['DISCOUNT', 'CASHBACK']),
        'incentive_amount': generate_big_decimal(),
        'anonymous_donor': None,
        'is_shared_fee': None
    }

    configure_transaction_configuration(transaction_type, base_transaction)

    return base_transaction

# Generate a list of transactions


num_transactions = 10000000

count = 0
t_batch_size = int(num_transactions/10)
for t_batch in range(0, num_transactions, t_batch_size):
    transactions = []
    for _ in range(t_batch_size):
        transaction = generate_transaction(choose_transaction_type())
        transactions.append(transaction)

    print(f"Count transactions generated till now: {t_batch+t_batch_size}")
    batch_insert_transactions(transactions)
    print(f"Data inserted in table: {t_batch+t_batch_size}")


