def suspicious_transactions(transactions, threshold):
    suspicious_transactions_list = []
    for transaction in transactions:
        if transaction > threshold:
            suspicious_transactions_list.append(transaction)
    return suspicious_transactions_list