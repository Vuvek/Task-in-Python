print("----------------------- 16 Coin Puzzle -----------------------")
print("---------------------  Coins -> 1 2 3 4 -----------------------")
import  random
import sys
l1 = [1,2,3,4]
sum_coin = 16
n = len(l1)+1
l2 = []
count = 0
flag = 0
flag1 = 0
while count!=16:
    flag = 0
    l2 = []
    try:
        player1 = int(input("player1 Enter Coin : "))
        if player1 not in l1:
            flag1 = 1
            print(flag1)
            raise Exception("\U0001F606 \U0001F606 \U0001F606 \U0001F923 \U0001F923 \U0001F923 Abe Sale Coins 1 2 3 4 Mai Chunna Hai To 4 Se Jyada Kiya Tera Bap Lakr Dega \U0001F606 \U0001F606 \U0001F606 \U0001F923 \U0001F923 \U0001F923")
    except Exception as e:
        if flag1 == 0:
            print("\U0001F606 \U0001F606 \U0001F606 \U0001F923 \U0001F923 \U0001F923 Abe Sale Coins 1 2 3 4 Mai Chun na Hai To or kuch dal ke gand kyu mra ra hai \U0001F923 \U0001F923 \U0001F923 \U0001F606 \U0001F606 \U0001F606")
            input("\n\n\n\n\n\n\U0001F923\U0001F606Press Enter to Close to the game\U0001F923\U0001F606")

            sys.exit()
        if flag1 == 1:
            print(e)
            input("\n\n\n\n\n\n\U0001F923\U0001F606Press Enter to Close to the game\U0001F923\U0001F606")

            sys.exit()
    count+=player1
    if count == 16:
        print("Player1 won the game ")
        break
    for i in l1:
        check = sum_coin - (count + i)
        if  check % 5 == 0:
            flag = 1
            l2.append(i)
            break
    else:
        l2.append(random.choice(l1))
    computer = min(l2)
    print(f"computer Entered : = {computer}")
    count+=computer

if flag == 1:
    print("Computer won the game ")










input("Enter to Close to the game")
