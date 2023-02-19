
# quiz game


# clear terminal
import os
os.system('cls')


# questions in list form #
Q1 = [" Q1: What is the capital city of Australia?\n", "a. Sydney\n", "b. Canberra\n", "c. Melbourne\n", "d. Brisbane\n", 2 ]
Q2 = [" Q2: Which river is the longest in the world?\n", "a. Amazon River\n", "b. Nile River\n", "c. Yangtze River\n", "d. Mississippi River\n", 2 ]
Q3 = [" Q3: Which of the following is NOT a continent?\n", "a. Europe\n", "b. Antarctica\n", "c. Asia\n", "d. Greenland\n", 4 ]
Q4 = [" Q4: What is the largest country in South America by land area?\n", "a. Brazil\n", "b. Argentina\n", "c. Peru\n", "d. Colombia\n", 1 ]
Q5 = [" Q5: Which country is both in Europe and Asia?\n", "a. Turkey\n", "b. Egypt\n", "c. Russia\n", "d. Saudi Arabia\n", 1 ]
Q6 = [" Q6: What is the highest mountain in North America?\n", "a. Mount Denali\n", "b. Mount Whitney\n", "c. Mount Rainier\n", "d. Mount St. Helens\n", 1 ]
Q7 = [" Q7: What is the name of the largest ocean on Earth?\n", "a. Indian Ocean\n", "b. Atlantic Ocean\n", "c. Pacific Ocean\n", "d. Southern Ocean\n", 3 ]
Q8 = [" Q8: What is the capital city of Canada?\n", "a. Vancouver\n", "b. Ottawa\n", "c. Toronto\n", "d. Montreal\n", 2 ]
Q9 = [" Q9: What is the largest desert in the world?\n", "a. Sahara Desert\n", "b. Gobi Desert\n", "c. Arabian Desert\n", "d. Antarctic Desert\n", 4 ]
Q10 = [" Q10: What is the name of the river that flows through the Grand Canyon?\n", "a. Colorado River\n", "b. Mississippi River\n", "c. Amazon River\n", "d. Nile River\n", 1 ]


# game vars #
answer_map = [0, 'a', 'b', 'c', 'd']
quiz = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]
score = 0


# intro #
print('Welcome to my world geography quiz!\n')
playing = input('Do you want to play? ')
# exit if player does not want to play
if not playing.startswith('y'):
    quit()
print('\nOkay, lets play :\n')


# ask questions #
for Q in quiz:
    print(*Q[0:5])
    if input('Answer: ') == answer_map[Q[5]]:
        print('\nCorrect! ')
        score += 1
    else:
        print('\nIncorrect! :( ')
    print('The answer was: '+Q[Q[5]])


# end and report score #
print('\n\nYou have completed the quiz!\n\nYour score was: '+str(score)+'/'+str(len(quiz)))
