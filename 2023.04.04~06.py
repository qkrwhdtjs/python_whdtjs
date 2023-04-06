        #문자열
# sentence ='나는 소년입니다.'
# print(sentence)
# sentence2 ='파이썬은 쉬워요'
# print(sentence2)
# sen3="""
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sen3)


        #슬라이싱
# jumin ="990120-1234567"
# print("성별:"+jumin[7]) # 주민번호 7번쨰 자리 출력
# print("연 :"+jumin[0:2])    #0번째 자리부터 2번쨰 자리 직전까지 출력
# print("월 :"+jumin[2:4])
# print("일 :"+jumin[4:6])

# print("생년월일 :"+jumin[:6]) #처음부터 6직전까지 출력
# print("뒤 7자리 :"+jumin[7:14]) #[7:14]==[7:]
# print("뒤 7자리 (뒤부터): "+jumin[-7:])

       #문자열 처리함수
#python = "Python is Amazing"
# print(python.lower())   #소문자로 출력
# print(python.upper())   #대문자로 출력
# print(python[0].isupper())  # 첫번쨰자리가 대문자면 true출력/아니면 falue출력
# print(len(python))  #python변쉥 저장되어있는값이 몇자리인지.
# print(python.replace("Python","Java"))    #python변수 안에 들어있는 Python값 자리에 Java로 변경되어 출력

# index = python.index("n")    #python변수안에 저장되어있는 n이 몇번째 자리인지 출력.
# print(index)
# index = python.index("n",index +1)  #python변수에 저장되어있는 두번째 n이 몇번째 자리인지 출력.
# print(index)

# print(python.find("JAVA")) #변수값과 다르다면 -1출력, 맞다면 자리 수 출력
# #print(python.index("JAVA")) #변수 값과 다르다면 -1출력이 아니라 오류 출력 

#print(python.count("n"))    #Python변수 값에 n이 몇개가 있는지 출력해주는 함수.


            #문자열 포멧
# print("나는 %d살입니다." %20)   #정수형
# print("나는 %s를 좋아해요."%"파이썬")   #문자열
# print("Apple 은 %c로 시작해요."%"A")    #문자형

# print("나는 {}살입니다.".format(20))
# print("나느 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))   #{}안에 값지정해주는 것이 format(,)안에 번지 수와 맞는것이 출력
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))   #0과 1이 윗문장과 반대여서 0번쨰인 파란이 뒤에 출력. 1번쨰인 빨간이 앞에 출력

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20,color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간",age=20))    #format안 변수선언 순서와 상관없이 {}안에 변수선언해주는 변수값출력.

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")       #f를 넣어주면 미리선언된 변수를 {}안에 변수값을 넣을 수 있다.


#                 #탈출문자
# # \n ==줄바꿈
# print("백문이 불여일견\n백견이불여일타")

# # \",\' : 문장 내에서 따옴표 출력.
# print("저는 '나도코딩'입니다.")
# print("저는\"나도코딩\"입니다")

# # \\ : 문장 내에서 \하나 출력
# print("C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python311\\python.ex")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\r Pine")

# # \b : 백스페이서 (왼쪽에 있는 한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭 
# print("Red\tApple")



            #문제 3
# url="http://naver.com"
# url1=url[7:]
# url2=url1[:-4]
# url3=url2[:3]

# password=url3+str(len(url2))+str(url2.count("e"))+"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url,password))



            #리스트
subway =[10,20,30]
print(subway[1])

subway = ["유재석","조세호","박명수"]
# subway 리스트 안에 0번째 -유재석, 1번째-조세호 ,2번째-박명수 저장

# 조세호가 몇번째 리스트에 저장되어있는지 출력하시오
print(subway.index("조세호"))

#  하하를 다음 칸에 저장
subway.append("하하")
print(subway)

# 정형돈을 유재석과 조세호 사이에 저장.
# 1번째 자리에 저장되어있던 조세호부터 한칸씩 뒤로 밀고
# 1번째 자리에 정형돈을 저장.
subway.insert(1,"정형돈")
print(subway)

# 리스트중 가장 마지막에 저장되어있는 "하하"를 리스트밖으로 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬
list=[5,4,3,2,1]
list.sort()
print(list)

# 순서 뒤집기 

list.reverse()
print(list)

# # 모두 지우기 (저장되어 있는 값 모두)
# list.clear()
# print(list)


# 다른 자료형과 함께 사용도 가능하며, 다른 리스트와 조합하여 하나의 리스트로 사용ㄱ능.
mix_list=["조세호",20,True]
list.extend(mix_list)
print(list)



