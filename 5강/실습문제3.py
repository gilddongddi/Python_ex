# Q3. 사용자로부터 패스워드를 입력받아 프로그램에 저장된 패스워드와 일치하는지 여부를 비교해서 일치하면 '로그인 성공', 그렇지 않으면 '로그인 실패' 메시지를 출력하기

pw = input('패스워드 입력: ')
if pw == 'sejong':
    print('로그인 성공!')
else:
    print('로그인 실패 :(')
