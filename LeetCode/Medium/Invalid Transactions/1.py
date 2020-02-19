class Solution:
    def invalidTransactions(self, transactions):
        transactions_sorted = []
        
        invalid_transactions = set()
        
        for transaction_str in transactions:
            name, time, amount, place = transaction_str.split(',')
            transactions_sorted.append((name, int(time), place, int(amount)))
        

        transactions_sorted.sort()
        
        print(transactions_sorted)
        
        for i in range(len(transactions_sorted)-1):
            

            first_name, first_time, first_place, first_amount = transactions_sorted[i]
            second_name, second_time, second_place, second_amount = transactions_sorted[i+1]
            
            
            if first_amount > 1000:
                invalid_transactions.add("{},{},{},{}".format(first_name, first_time, first_amount, first_place))
                
                
            if second_amount > 1000:
                invalid_transactions.add("{},{},{},{}".format(second_name, second_time, second_amount, second_place))
                
            
            if first_name == second_name:
                if not first_place == second_place:
                    if first_time+60 >= second_time:
                        invalid_transactions.add("{},{},{},{}".format(first_name, first_time, first_amount, first_place))
                        invalid_transactions.add("{},{},{},{}".format(second_name, second_time, second_amount, second_place))
            
            else:
                continue
                
            
        return list(invalid_transactions)
                