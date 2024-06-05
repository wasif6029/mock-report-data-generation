import random

cluster_data = {
    "NORMAL_CLUSTER": {
        "transactions": {
            "CB2CW": {"min_amount": 15, "max_amount": 30},
            "CC2CW": {"min_amount": 10, "max_amount": 20},
            "CW2CB": {"min_amount": 10, "max_amount": 20},
        },
        "initial_balance_range": {
            "normal": (50000, 500000),
            "anomalous": (1000000, 3000000)
        },
        "transaction_amount_range": {
            "normal": (5, 300),
            "anomalous": (601, 2000)
        }
    }
}



def get_all_bank_cluster_data():
    return cluster_data


def get_bank_data_by_cluster(cluster):
    return cluster_data[cluster]


def get_bank_data_by_cluster_and_transaction(cluster, transaction):
    return cluster_data[cluster]["transactions"][transaction]


def get_random_bank_cluster():
    clusters = list(cluster_data.keys())
    return random.choice(clusters)
