import csv
from os import preadv
import sys
import hashlib
from miner import mining
from miner import mining_reward

# takes name of wallets csv file and returns 2d array of wallets 
def readWallets(inFile):
    try:
        file = open(inFile, 'r')
        wallets = []
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            wallets.append(line)
        file.close()

        return wallets
    except IOError:
        print('Error reading file. Aborting...')
        sys.exit()

# takes name of transaction ledger file and returns 2d array of transactions
def readBlocks(inFile):
    try:
        file = open(inFile, 'r')
        blocks = []
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            blocks.append(line)
        file.close()
        return blocks
    except IOError:
        print('Error reading file. Aborting...')
        sys.exit()

def getCurrentHash(blockData, prevHash) -> str:
  
    # generate a len 80 hexadecimal value of bytes
    hashable = ''
    for data in blockData:
        hashable += data
    hashable = hashable + prevHash
    hashable = hashable.encode('utf-8')  # convert to bytes
    this_hash = hashlib.sha256(hashable).hexdigest()  # hash w/ SHA-256 and hexdigest
    return this_hash # prepend hash and return

def printMenu():
    # print menu
    print('Welcome to CatCoin!')
    print('\n')
    print('Please select from the following options: ')
    print('    1. Check Wallet Balance')
    print('    2. Transfer CatCoins')
    print('    3. Quit CatCoin')

def validateInput(options):
    choice = input()
    for option in options:
        if choice == option:
            return True
        print("Invalid input")
        return False

def checkWalletBalance(wallets):
    print('Select a wallet:')
    print('1. Wallet 1')
    print('2. Wallet 2')
    print('3. Wallet 3')
    walletValid = False
    while not walletValid:
        wallet = input()
        if wallet == '1':
            walletValid = True   
            print('Wallet 1 balance: ' + wallets[0][1] + ' CAT')   
        elif wallet == '2':
            walletValid = True
            print('Wallet 2 balance: ' + wallets[1][1] + ' CAT')  
        elif wallet == '3':
            walletValid = True
            print('Wallet 3 balance: ' + wallets[2][1] + ' CAT')  
        else: 
            print('Invalid choice. Enter 1, 2, or 3.')

def transferFunds(wallets):
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
            sourceValid = True
        elif source == '3':
            sourceValid = True
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
            
            blocks = readBlocks('blocks.csv')
            prevHash = blocks[len(blocks)-1][5]
            n, t = mining(prevHash)
            blockData = blocks[len(blocks)-1]
            
            currHash = getCurrentHash(blockData, prevHash)
            try:
                with open('blocks.csv', 'a') as blocksFile:
                    transaction = csv.writer(blocksFile)
                    transaction.writerow([len(blocks), source, destination, amount, prevHash, currHash, t, n])
                blocksFile.close()
                
            except IOError:
                print('Error reading file. Aborting...')
                sys.exit()
            
            # update wallet balances
            # deduct from source wallet
            sourceBalance = int(wallets[int(source)-1][1])
            sourceBalance -= int(amount)
            wallets[int(source)-1][1] = str(sourceBalance)
            # credit destination wallet
            destinationBalance = int(wallets[int(destination)-1][1])
            destinationBalance += int(amount)
            wallets[int(destination)-1][1] = str(destinationBalance)
            try:
                with open('wallets.csv', 'w') as walletsFile:
                    walletsFile.write('wallet,balance\n')
                    for i in range(len(wallets)):
                        for j in range(len(wallets[i])):
                            walletsFile.write(wallets[i][j])
                            if j < len(wallets[i]) - 1:
                                walletsFile.write(',')
                        walletsFile.write('\n')
                walletsFile.close()
                
            except IOError:
                print('Error reading file. Aborting...')
                sys.exit()

            print('Transaction complete')
        else:
            print('Transaction cancelled')
    else: 
        print('Insufficient funds.')
            
def main():
    wallets = readWallets('wallets.csv')
    printMenu()

    # get and validate input
    menuValid = False
    while not menuValid:
        choice = input()

        # check balance
        if choice == '1':
            menuValid = True
            checkWalletBalance(wallets)

        # transfer
        elif choice == '2':
            menuValid = True
            transferFunds(wallets)
        
        # exit
        elif choice == '3':
            menuValid = True
            confirm = input('Are you sure you want to exit CatCoin? y/n ')
            
        else: 
            print('Invalid choice. Enter 1, 2, or 3.')
    

main()