import random

transaction_frequency_range = 1000

cluster_data = {
    "NANO_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (10, 250), "anomalous": (650, 1700), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (15, 200), "anomalous": (700, 1800), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (20, 280), "anomalous": (750, 1900), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (25, 320), "anomalous": (800, 2000), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (30, 350), "anomalous": (850, 2100), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (35, 380), "anomalous": (900, 2200), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (40, 400), "anomalous": (950, 2300), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (45, 300),
            "anomalous": (1050, 2300)
        },
        "transaction_amount_range": {
            "normal": (35, 290),
            "anomalous": (950, 2100)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    },
    "MICRO_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (20, 250), "anomalous": (650, 1700), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (25, 200), "anomalous": (700, 1800), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (30, 280), "anomalous": (750, 1900), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (35, 320), "anomalous": (800, 2000), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (40, 350), "anomalous": (850, 2100), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (45, 380), "anomalous": (900, 2200), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (50, 400), "anomalous": (950, 2300), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (50, 400),
            "anomalous": (1050, 2500)
        },
        "transaction_amount_range": {
            "normal": (40, 350),
            "anomalous": (950, 2200)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),

    },
    "MINI_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (15, 230), "anomalous": (660, 1800), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (20, 180), "anomalous": (710, 1900), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (25, 260), "anomalous": (760, 2000), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (30, 300), "anomalous": (810, 2100), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (35, 330), "anomalous": (860, 2200), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (40, 360), "anomalous": (910, 2300), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (45, 380), "anomalous": (960, 2400), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (55, 500),
            "anomalous": (1100, 2700)
        },
        "transaction_amount_range": {
            "normal": (45, 400),
            "anomalous": (1000, 2300)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    },
    "SMALL_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (20, 270), "anomalous": (680, 1900), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (25, 220), "anomalous": (730, 2000), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (30, 300), "anomalous": (780, 2100), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (35, 340), "anomalous": (830, 2200), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (40, 370), "anomalous": (880, 2300), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (45, 400), "anomalous": (930, 2400), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (50, 420), "anomalous": (980, 2500), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (60, 550),
            "anomalous": (1150, 2800)
        },
        "transaction_amount_range": {
            "normal": (50, 450),
            "anomalous": (1050, 2400)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    },
    "MEDIUM_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (25, 290), "anomalous": (700, 2000), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (30, 240), "anomalous": (750, 2100), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (35, 320), "anomalous": (800, 2200), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (40, 360), "anomalous": (850, 2300), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (45, 390), "anomalous": (900, 2400), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (50, 420), "anomalous": (950, 2500), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (55, 440), "anomalous": (1000, 2600), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (65, 600),
            "anomalous": (1200, 2900)
        },
        "transaction_amount_range": {
            "normal": (55, 500),
            "anomalous": (1100, 2500)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    },
    "LARGE_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (30, 340), "anomalous": (750, 2100), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (35, 280), "anomalous": (800, 2200), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (40, 360), "anomalous": (850, 2300), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (45, 400), "anomalous": (900, 2400), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (50, 430), "anomalous": (950, 2500), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (55, 460), "anomalous": (1000, 2600), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (60, 480), "anomalous": (1050, 2700), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (70, 650),
            "anomalous": (1250, 3000)
        },
        "transaction_amount_range": {
            "normal": (60, 550),
            "anomalous": (1150, 2600)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    },
    "MEGA_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (35, 390), "anomalous": (800, 2200), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (40, 320), "anomalous": (850, 2300), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (45, 400), "anomalous": (900, 2400), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (50, 440), "anomalous": (950, 2500), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (55, 470), "anomalous": (1000, 2600), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (60, 500), "anomalous": (1050, 2700), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (65, 520), "anomalous": (1100, 2800), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (75, 700),
            "anomalous": (1300, 3100)
        },
        "transaction_amount_range": {
            "normal": (65, 600),
            "anomalous": (1200, 2700)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    },
    "GIGA_CLUSTER": {
        "transactions": {
            "CW2CW": {"normal": (40, 440), "anomalous": (850, 2300), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2AW": {"normal": (45, 370), "anomalous": (900, 2400), "normalFrequency": (1, 5),
                      "anomalousFrequency": (6, 11)},
            "AW2CW": {"normal": (50, 450), "anomalous": (950, 2500), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CW2MW": {"normal": (55, 480), "anomalous": (1000, 2600), "normalFrequency": (2, 6),
                      "anomalousFrequency": (7, 12)},
            "CB2CW": {"normal": (60, 510), "anomalous": (1050, 2700), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CC2CW": {"normal": (65, 540), "anomalous": (1100, 2800), "normalFrequency": (3, 7),
                      "anomalousFrequency": (8, 13)},
            "CW2CB": {"normal": (70, 570), "anomalous": (1150, 2900), "normalFrequency": (4, 8),
                      "anomalousFrequency": (9, 14)},
        },
        "initial_balance_range": {
            "normal": (80, 750),
            "anomalous": (1350, 3200)
        },
        "transaction_amount_range": {
            "normal": (70, 650),
            "anomalous": (1250, 2800)
        },
        "transaction_frequency_range": (transaction_frequency_range, transaction_frequency_range+5),
    }
}


def get_all_customer_cluster_data():
    return cluster_data


def get_customer_data_by_cluster(cluster):
    return cluster_data[cluster]


def get_customer_data_by_cluster_and_transaction(cluster, transaction):
    return cluster_data[cluster]["transactions"][transaction]


def get_random_customer_cluster():
    clusters = list(cluster_data.keys())
    return random.choice(clusters)


def get_customer_total_transaction_count(cluster):
    return random.randint(*cluster_data[cluster]["transaction_frequency_range"])
