import random

cluster_data = {
    "NANO_CLUSTER": {
        "transactions": {
            "AW2CW": {"min_amount": 15, "max_amount": 30},
            "CW2AW": {"min_amount": 10, "max_amount": 20}
        },
        "initial_balance_range": {
            "normal": (5, 300),
            "anomalous": (601, 2000)
        },
        "transaction_amount_range": {
            "normal": (5, 300),
            "anomalous": (601, 2000)
        }
    },
    "MINI_CLUSTER": {
        "transactions": {
            "AW2CW": {"min_amount": 10, "max_amount": 40},
            "CW2AW": {"min_amount": 10, "max_amount": 25}
        },
        "initial_balance_range": {
            "normal": (15, 700),
            "anomalous": (901, 2500)
        },
        "transaction_amount_range": {
            "normal": (5, 300),
            "anomalous": (601, 2000)
        }
    },
    "LARGE_CLUSTER": {
        "transactions": {
            "AW2CW": {"min_amount": 30, "max_amount": 50},
            "CW2AW": {"min_amount": 20, "max_amount": 40}
        },
        "initial_balance_range": {
            "normal": (10, 1200),
            "anomalous": (1301, 3000)
        },
        "transaction_amount_range": {
            "normal": (5, 300),
            "anomalous": (601, 2000)
        }
    }
}



def get_all_agent_cluster_data():
    return cluster_data


def get_agent_data_by_cluster(cluster):
    return cluster_data[cluster]


def get_agent_data_by_cluster_and_transaction(cluster, transaction):
    return cluster_data[cluster]["transactions"][transaction]


def get_random_agent_cluster():
    clusters = list(cluster_data.keys())
    return random.choice(clusters)
