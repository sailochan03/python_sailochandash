from find_sus_trans import suspicious_transactions
from sort_sus_trans import sort_suspicious_transactions
from search_sus_trans import search_transaction
from reconstruct_trans import reconstruct_transactions

def main():
    transactions = [120, 45, 300, 220, 90, 600, 130, 75, 800, 500, 350, 40]
    threshold = 250
    search_amount = 500

    suspicious_transactions_list = suspicious_transactions(transactions, threshold)
    print(f'\nSuspicious transactions: {suspicious_transactions_list}\n')

    sorted_suspicious_transactions = sort_suspicious_transactions(suspicious_transactions_list)
    print(f'Sorted Suspicious transactions: {sorted_suspicious_transactions}\n')

    transaction_exists = search_transaction(sorted_suspicious_transactions, search_amount)
    print(f'Transaction {search_amount} found: {transaction_exists}\n')

    reconstructed_transactions = reconstruct_transactions(transactions)
    print(f'Fully sorted transactions: {reconstructed_transactions}\n')

if __name__ == '__main__':
    main()