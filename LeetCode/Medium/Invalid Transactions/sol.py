class Solution:
    def invalidTransactions(self, transactions):
        sorted_transactions = []
        invalid_transactions = set()
        
        for t in transactions:
            name, minutes, amount, city = t.split(',')
            minutes, amount = int(minutes), int(amount)
            sorted_transactions.append((minutes, name, amount, city, t))
            
        sorted_transactions.sort(key=lambda item: item[0])
                        
        for index, t in enumerate(sorted_transactions):
            minutes, name, amount, city, t = t

            if amount > 1000:
                invalid_transactions.add(t)
            counter = index+1
            while counter < len(transactions):
                if (sorted_transactions[counter][0] <= minutes+60):
                    if((sorted_transactions[counter][1] == name)
                         and (sorted_transactions[counter][3] != city)):
                        invalid_transactions.add(sorted_transactions[counter][4])
                        invalid_transactions.add(t)
                    counter += 1
                else:
                    break
                    
        return list(invalid_transactions)