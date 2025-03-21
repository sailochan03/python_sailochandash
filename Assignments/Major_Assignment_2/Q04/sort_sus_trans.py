def sort_suspicious_transactions(transactions):
    n = len(transactions)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if transactions[j] < transactions[min_index]:
                min_index = j
        transactions[i], transactions[min_index] = transactions[min_index], transactions[i]
    return transactions