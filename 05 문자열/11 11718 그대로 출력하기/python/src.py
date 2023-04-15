from sys import exit

while True:
    try:
        # 문장 sentence 입력.
        sentence = input()
        if len(sentence) < 0 or len(sentence) > 100: exit(0)
        print(sentence)
    except:
        break