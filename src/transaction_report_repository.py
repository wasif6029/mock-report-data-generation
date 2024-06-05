import pyodbc

def batch_insert_transactions(transactions, batch_size=100000):
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=wasifs_wallet;"
        "Trusted_Connection=yes;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        insert_statement = """
        INSERT INTO report.transaction_report_mock (
            id, created_by, updated_by, create_date_time, update_date_time, is_deleted,
            request_id, transaction_id, workflow_request_id, transaction_type,
            transaction_code, from_account_name, to_account_name, from_internal_account,
            to_internal_account, sender_account_type, receiver_account_type, 
            bank_transaction_reference, amount, fee_amount, fee_payer, vat_amount, 
            vat_payer, sender_debit_amount, receiver_credit_amount, withdrawer_running_balance, 
            depositor_running_balance, user_note, remarks, status, dispute_status, dispute_remarks, 
            original_transaction_reference_for_reversal, transaction_date_time, sender_idp_id, 
            receiver_idp_id, from_account, to_account, transaction_category_id, sender_country_code, 
            sender_phone_number, receiver_country_code, receiver_phone_number, transaction_reference, 
            branch_id, merchant_id, reversed_transaction_ref, fee_description, fee_payer_internal_account, 
            vat_payer_internal_account, subsidy_id, subsidy_amount, subsidy_type, incentive_payment_type, 
            incentive_amount, anonymous_donor, is_shared_fee
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        for start in range(0, len(transactions), batch_size):
            batch = transactions[start:start+batch_size]
            values = [tuple(transaction.values()) for transaction in batch]
            cursor.executemany(insert_statement, values)
            conn.commit()

    except pyodbc.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

