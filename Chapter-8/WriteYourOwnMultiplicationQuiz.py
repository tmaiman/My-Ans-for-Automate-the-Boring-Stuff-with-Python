import time
import random

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    ans = num1 * num2
    
    print(f'Q{questionNumber + 1}: {num1} x {num2} = ?')
    
    start_time = time.time()
    for retries in range(3):
        user = input('\nYour answer: ')
        try:
            user = int(user)
        except:
            print('Please enter numerical value...')
            
        if time.time() - start_time < 8.0:
            if user == ans:
                print('Correct!')
                correctAnswers += 1
                break
            else:
                    print(f'Wrong!\nRetries left = {2 - retries}')
        else:
            print('Timeout!')
            break
    time.sleep(1)
                
print(f'Number of correct answers = {correctAnswers}')