import random

# خوشامدگویی و توضیح بازی
print("Welcome to game")
#گل در یکی از سه دست پنهان می‌شود. هر بازیکن به نوبت باید حدس بزند که گل در کدام دست است
#دست‌ها شماره‌گذاری شده‌اند: 1، 2 و 3"

# امتیاز اولیه برای هر بازیکن
score_player1 = 0
score_player2 = 0

# تعداد دفعات بازی
rounds = int(input("How many rounds do you want to play?"))

# حلقه بازی برای هر دور
for i in range(rounds):
    print(f"Rounds {i+1} {rounds}")
    
    # تعیین تصادفی مکان گل
    goal_position = random.randint(1, 3)
    
    # حدس بازیکن 1
    try:
        player1 = int(input("In which hand is the goal? "))
        
        if player1 == goal_position:
            print("You guessed right , Good work player1")
            score_player1 += 1
        else:
            print("It was wrong Player1 : " , goal_position )

    except ValueError:
        print("Error! ,Please Enter correct number")

    
    # حدس بازیکن 2
    try:
        player2 = int(input("Wich one ? 1 , 2 , 3 ? "))
        
        if player2 == goal_position:
            print("You guessed right , Good work player2")
            score_player2 += 1
        else:
            print("It was wrong Player2 : " , goal_position)
    
    except ValueError:
        print("Error! ,Please Enter correct number")
      

# نمایش امتیازات نهایی
print("Result")
print("Score Player1 :", score_player1)
print("Score Pleyer2 :", score_player2)

if score_player1 > score_player2:
    print("Excelent Player1 , You Win...")
elif score_player2 > score_player1:
    print("Excelent Player1 , You Win...")
else:
    print("The game was tied")
