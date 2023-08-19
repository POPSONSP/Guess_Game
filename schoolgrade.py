"""
PROJECT:
Prepare a school entrance grading program whereby for a particular student will be asked to enter 
the score of the various subjects offered the sum of the score will determine the 
action and the review go be given
"""

import time
user= input("what is your name?: ").lower()
school= input("what school are you from?: ").lower()
print(f"welcome {user} from {school} you have been granted full access to our grading platform")
que= input("Will you like to know your grade in your last exam?: ")
if que=="yes":
    print("Kindly provide your score in the space provided below")
    chemistry_score=input("chem 101 score: ")
    physics_score=input("phy 101 score: ")
    eng_score=input("eng 101 score: ")
    mth_score=input("mth 101 score: ")
    res= float(chemistry_score)+ float(physics_score)+ float(eng_score)+ float(mth_score)
    print(res)
    if res <=30:
        time.sleep(1)
        print(" Your grade is F ")
        time.sleep(1)
        print(" Your score is below standard,, you are hereby Rusticated from school ")
    elif res >= 31  and res <= 40:
        time.sleep(1)
        print(" Your grade is E ")
        time.sleep(1)
        print("Your score is poor, Your grade is E, You are hereby placed on probation from school for a period of 6 month")
    elif res >=40 and res <=50:
        time.sleep(1)
        print(" Your grade is D ")
        time.sleep(1)
        print("You have performed below averegely, you are hereby requested to repeat exams ")
    elif res >=51 and res<= 60:
        time.sleep(1)
        print(" Your grade is C ")
        time.sleep(1)
        print("you have performed averagely, you have been placed on strict monitoring for re-evaluation for a period of 6 month ")
    elif res >=61 and res<=70:
        time.sleep(1)
        print(" Your grade is B ")
        time.sleep(1)
        print("you performed slightly above average, you are hereby encouraged to explore more")
    elif res >=71 and res<=85:
        time.sleep(1)
        print(" Your grade is A ")
        time.sleep(1)
        print("you have perfromed satisfactorily, do not give up")
    elif res>=86 and res<=100:
        time.sleep(1)
        print(" Your grade is A+ ")
        time.sleep(1)
        print("We are proud of you, You are hereby placed on SCHORLASHIP")
    elif res>100:
        print("You have entered a wrong scale of grade,kindly check and confirm thereafter check your grade again.")    
else:
    print("You are free to access your grade in your leisure time")
