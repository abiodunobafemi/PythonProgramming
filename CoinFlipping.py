# Coin-flipping
import random

numHeads = 0
numTails = 0

#Flip a coin 10 times
for i in range(100):
    coin = random.choice(['heads', 'tails'])
    if coin == 'heads':
        numHeads = numHeads + 1
    else:
        numTails = numTails + 1
    print(coin)

print("\nNumber of Heads: ", numHeads)
print("Number of Tails: ", numTails)
