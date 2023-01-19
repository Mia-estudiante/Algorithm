alpha = ['c=', 'c-','dz=','d-','lj','nj','s=','z=']

word = input()

for a in alpha:
    word = word.replace(a, "*")
print(len(word))

'''
아예 다른 문자로 대체하자
ex. nljj의 경우, lj를 삭제하면 nj가 되는데..
이는 또 크로아티아 알파벳에 속해 있어 3이 아닌 2가 출력된다. 
'''