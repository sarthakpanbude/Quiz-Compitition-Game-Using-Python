print("\n-----------------------------------")
print("Welcome To The Quiz Compitition !")
print("\n-----------------------------------")
a=input("Enter Your Full Name :")
score=0
print("Let's Start The Compitition")

#Question 1
print("1.What is the capital city of Australia?")
option1=print("\nA.Sydney\nB.Melbourne\nC.Canberra\nD.Brisbane")
answer1=input("Enter Your Answer (A/B/C/D): ")
if answer1 == "C":
    print("Congratulations ! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry! Your Answer Is Wrong.........Correct Answer Is C")
    score-=2

#Question 2
print("\n 2.Who painted the Mona Lisa?")
option2=print("\nA.Leonardo da Vinci\nB.Pablo Picasso\nC.Vincent van Gogh\nD.Michelangelo")
answer2=input("Enter Your Answer (A/B/C/D): ")
if answer2 == "A":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry! Your Answer Is Wrong.........Correct Answer Is A")
    score-=2

#Question 3
print("\n 3.Which planet is known as the Red Planet?")
option3=print("\nA.Jupiter\nB.Mars\nC.Venus\nD.Saturn")
answer3=input("Enter Your Answer (A/B/C/D): ")
if answer3 == "B":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong .........Correct Answer Is B")
    score-=2

#Question 4
print("\n 4.In what year did World War II end?")
option4=print("\nA.1939\nB.1940\nC.1945\nD.1950")
answer4=input("Enter Your Answer (A/B/C/D): ")
if answer4 == "C":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is C")
    score-=2

#Question 5
print("\n 5.Who wrote the play Romeo and Juliet?")
option5=print("\nA.William Shakespeare\nB.Charles Dickens\nC.George Orwell\nD.Jane Austen")
answer5=input("Enter Your Answer (A/B/C/D): ")
if answer5 == "A":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is A")
    score-=2

#Question 6
print("\n 6.What is the largest mammal in the world?")
option6=print("\nA.African Elephant\nB.Blue Whale\nC.Giraffe\nD.Polar Bear")
answer6=input("Enter Your Answer (A/B/C/D): ")
if answer6 == "B":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is B")
    score-=2

#Question 7
print("\n 7.Which element has the chemical symbol 'O' ?")
option7=print("\nA.Oxygen\nB.Ozmium\nC.Ozone\nD.Oxide")
answer7=input("Enter Your Answer (A/B/C/D): ")
if answer7 == "A":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is A")
    score-=2

#Question 8
print("\n 8.What currency is used in Japan?")
option8=print("\nA.Won\nB.Yen\nC.Yuan\nD.Ringgit")
answer8=input("Enter Your Answer (A/B/C/D): ")
if answer8 == "B":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is B")
    score-=2

#Question 9
print("\n 9.How many continents are there on Earth?")
option8=print("\nA.5\nB.6\nC.7\nD.8")
answer9=input("Enter Your Answer (A/B/C/D): ")
if answer9 == "C":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is C")
    score-=2

#Question 10
print("\n 10.What is the tallest mountain in the world?")
option10=print("\nA.Mount Everest\nB.K2\nC.Kangchenjunga\nD.Lhotse")
answer10=input("Enter Your Answer (A/B/C/D): ")
if answer10 == "A":
    print("Congratulations! Your  Answer Is Correct")
    score+=5
else:
    print("Sorry ! Your Answer Is Wrong.........Correct Answer Is A")
    score-=2

total_questions = 10
max_score = total_questions * 5  

#Final Score
print("\n-----------------------------------")
print("Your final score is", score, "out of", max_score)
print("\n-----------------------------------")

#Result
if score >= 50:
    print("Outstanding! Well Played!")
elif score >= 30:
    print("Nice Played!")
else:
    print("\n-----------------------------------")
    print("\nYou Are Fail Better Luck Next Time....Keep Practicing")
    print("\n-----------------------------------")