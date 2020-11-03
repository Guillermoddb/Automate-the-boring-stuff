import random
from pathlib import Path
capitals = {'Spain': 'Madrid', 'Portugal':'Lisbon', 'Italy':'Rome', 'France':'Paris', 'UK':'London'}
path_cwd = Path.cwd()
#we generate a text file for each element in the list
'''for i , j in enumerate(capitals):
    print(i)
    a = 'test%s.txt'%(i)
    f = path_cwd / a
    f = open(f, 'w')'''
#we create 35 quiz
for quizNum in range(10):
    quizFile = open(f'capitalquiz{quizNum +1}.txt','w')
    answer_key_file = open(f'capitalquiz_ans{quizNum+1}.txt', 'w')
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + f'European Countries Quiz (Form{quizNum+1})')
    quizFile.write('\n\n')

    capitales = list(capitals.keys())
    random.shuffle(capitales)
    #we select the correct and wrong answers
    for questionNum in range(5):
        correct_ans = capitals[capitales[questionNum]]
        wrong_ans = list(capitals.values())
        del wrong_ans[wrong_ans.index(correct_ans)]
        wrong_ans = random.sample(wrong_ans, 3)
        answer_opt = wrong_ans + [correct_ans]
        random.shuffle(answer_opt)

        #write the question and answer
        quizFile.write(f'{questionNum + 1}. What is teh capital of {capitales[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. {answer_opt[i]}\n")
        quizFile.write('\n')
        answer_key_file.write(f"{questionNum + 1}. {'ABCD'[answer_opt.index(correct_ans)]}")
    quizFile.close()
    answer_key_file.close()
    

