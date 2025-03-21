def search_transaction(transactions, target):
    low, high = 0, len(transactions) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if transactions[mid] == target:
            return True
        elif transactions[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False