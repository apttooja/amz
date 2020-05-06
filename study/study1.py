print(100+10)
print(7/5)
print(7//5)
print(7 % 5)
print(divmod(7, 5))    # 몫과 나머지를 동시에 튜플형태로 반환

# 진수표현
print('\n***진수표현***')
print(0b10)    # 2진수 10을 10진수로 출력
print(0o10)    # 8진수 10을 10진수로 출력
print(0x10)    # 8진수 10을 10진수로 출력

# 형변환
print('\n***형변환***')
print(int(True))
print(int(False))
print(type(int('-23')))    # int로 쒸우면 int형으로 형변환
# int('99 bottles')    # 정수와 문자가 섞이는 경우 오류 발생
print(4+7.0)            # 숫자 타입이 섞이는 경우 자동 형변환
# 형변환
print('\n***형변환-부동소수점***')
print(float(98))
print(float('98'))
print(float('1.0e3'))

print('\n***형변환-str()***')
print(str(98.6))

print('\n***문자열 처리***')
print('cho ' + 'wonyong')
print('cho ' 'wonyong')
a = 'Duck.'
b = a
c = 'Grey Duck!'
print(a+b+c)
print(a, b, c)    #변수 사이에 자동으로 공백을 넣어줌

print('\n***문자열 처리-복제하기***')
start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)


print('\n***문자열 처리-문자추출***')
letters = 'abcde'
print(letters[0])
print(letters[1])
print(letters[2])
print(letters[3])
print(letters[4])
print(letters[-1])
print(letters[-2])
print(letters[-3])
print(letters[-4])
print(letters[-5])

print('\n***문자열 처리-슬라이스***')
letters = 'abcdefghijk'
print(letters[0:2])
print(letters[:2])
print(letters[::2])

print('\n***문자열 처리-len()***')
print(len(letters))

print('\n***문자열 처리-split()***')
todos = 'get gloves, get mask, call mom'
print(todos.split(','))
print(todos.split())    # 아무런 인자없이 호출하는경우 공백기준으로 split

print('\n***문자열 처리-join()***')
crypto_list = ['Yeti', 'Bigfoot', 'Monster']
crypto_string = ': '.join(crypto_list)
print(crypto_string)

print('\n***문자열 다루기***')
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('End'))
word = 'doth'
print(poem.find(word))    # 첫번째로 word에 있는 글자가 나오는 위치
wordr = 'the'
print(poem.rfind(wordr))    # 마지막으로 wordr에 있는 글자가 나오는 위치
print(poem.count(word))     # word에 있는 글자가 나오는 횟수
print(poem.isalnum())        # 이 시는 글자와 숫자로만 이루어졌나?

print('\n***문자열 다루기-replace()***')
setup = 'a duck goes into a bar...'
print(setup.replace('duck', 'marmoset'))

print(setup.replace('a ', 'a famous ', 100))    # 100번까지 변경한다

# 여기까지 처음시작하는 파이썬 2장 완료 20.05.06