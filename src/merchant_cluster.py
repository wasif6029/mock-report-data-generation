import random

cluster_data = {
    "NANO_CLUSTER": {
        "transactions": {
            "CW2MW": {
                "normal": (5, 300),
                "anomalous": (601, 2000)
            }
        },
        "initial_balance_range": {
            "normal": (5, 300),
            "anomalous": (601, 2000)
        }
    },
    "MINI_CLUSTER": {
        "transactions": {
            "CW2MW": {
                "normal": (5, 300),
                "anomalous": (601, 2000)
            }
        },
        "initial_balance_range": {
            "normal": (15, 700),
            "anomalous": (901, 2500)
        }
    },
    "LARGE_CLUSTER": {
        "transactions": {
            "CW2MW": {
                "normal": (5, 300),
                "anomalous": (601, 2000)
            }
        },
        "initial_balance_range": {
            "normal": (10, 1200),
            "anomalous": (1301, 3000)
        }
    }
}


def get_all_merchant_cluster_data():
    return cluster_data


def get_merchant_data_by_cluster(cluster):
    return cluster_data[cluster]


def get_merchant_data_by_cluster_and_transaction(cluster, transaction):
    return cluster_data[cluster]["transactions"][transaction]


def get_random_merchant_cluster():
    clusters = list(cluster_data.keys())
    return random.choice(clusters)
