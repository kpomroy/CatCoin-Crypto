import csv
from this import d

# takes name of wallets csv file and returns 2d array of wallets 
def readWallets(inFile):
    file = open(inFile, 'r')
    wallets = []
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for line in csv_reader:
        wallets.append(line)

    return wallets

def validateInput(options):
    choice = input()
    for option in options:
        if choice == option:
            return True
        print("Invalid input")
        return False


            
def main():
    wallets = readWallets('wallets.csv')

    # print menu
    print('Welcome to CatCoin!')
    print('\n')
    print('Please select from the following options: ')
    print('    1. Check Wallet Balance')
    print('    2. Transfer CatCoins')
    print('    3. Quit CatCoin')

    # get and validate input
    menuValid = False
    while not menuValid:
        choice = input()

        # check balance
        if choice == '1':
            menuValid = True
            # print('Select a wallet:')
            # print('1. Wallet 1')
            # print('2. Wallet 2')
            # print('3. Wallet 3')
            # walletValid = False
            # while not walletValid:
            #     wallet = input()
            #     if wallet == '1':
            #         walletValid = True   
            #         print('Wallet 1 balance: ' + wallets[0][1] + ' CAT')   
            #     elif wallet == '2':
            #         walletValid = True
            #         print('Wallet 2 balance: ' + wallets[1][1] + ' CAT')  
            #     elif wallet == '3':
            #         walletValid = True
            #         print('Wallet 3 balance: ' + wallets[2][1] + ' CAT')  
            #     else: 
            #         print('Invalid choice. Enter 1, 2, or 3.')

        # transfer
        elif choice == '2':
            menuValid = True
            print('Select a source wallet:')
            print('1. Wallet 1')
            print('2. Wallet 2')
            print('3. Wallet 3')
            
            sourceValid = False
            while not sourceValid:
                source = input()
                if source == '1':
                    sourceValid = True   
                elif source == '2':
                    walletValid = True
                elif source == '3':
                    walletValid = True
                else: 
                    print('Invalid choice. Enter 1, 2, or 3.')

            print('Select a destination wallet:')
            print('1. Wallet 1')
            print('2. Wallet 2')
            print('3. Wallet 3')
            destinationValid = False
            while not destinationValid:
                destination = input()
                if destination == '1':
                    destinationValid = True   
                elif destination == '2':
                    destinationValid = True
                elif destination == '3':
                    destinationValid = True
                else: 
                    print('Invalid choice. Enter 1, 2, or 3.')

            floatValid = False
            while not floatValid:
                try:
                    amount = input('Enter CAT transfer amount: ')
                    floatAmount = float(amount)
                    floatValid = True
                except (TypeError):
                    print('Invalid input')
                    
                except(ValueError):
                    print('Invalid input')

            sourceIdx = int(source) - 1
            if floatAmount <= float(wallets[sourceIdx][1]): 
                confirm = input('Are you sure you want to transfer ' + amount + ' CatCoins to Wallet ' + destination + '? y/n ')
                while confirm.lower() != 'y' and confirm.lower() != 'n':
                    print('Invalid option')
                    confirm = input('Are you sure you want to transfer ' + amount + ' CatCoins to Wallet ' + destination + '? y/n ')
                if confirm.lower() == 'y':
                    # transfer money
                    print('Transaction complete')
                else:
                    print('Transaction cancelled')
            else: 
                print('Insufficient funds.')

        
        # exit
        elif choice == '3':
            menuValid = True
            confirm = input('Are you sure you want to exit CatCoin? y/n ')
            
        else: 
            print('Invalid choice. Enter 1, 2, or 3.')
    

main()