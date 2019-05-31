import random
#값 종류: 문제|답|점수
#문제 파일 불러오기
with open('questions.txt', 'r') as f: questions = f.readlines()

#
random.shuffle(questions)

#퀴즈 시작
count = 0; score = 0

print('---=====<<<[[[ 개꿀잼 퀴즈 타임 : 울트라 에디션 ]]]>>>=====---')
for s in questions:
    count += 1
    tmp = s.strip().split('|')
    print('\n[' + str(len(questions)) + '개 중 ' + str(count) + '번째 문제]')
    print('질문: ' + tmp[0] + ' [' + tmp[2] + '점]')
    if input('입력: ') == tmp[1]:
        print('정답!')
        score += int(tmp[2])
    else:
        print("틀렸습니다! 정답은 '" + tmp[1] + "' (이)었습니다...")
    
    
print('총점:', score)
