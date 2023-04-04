import math #math.log함수를 사용하기 위해 math호출.

a=17.27 #a에 주어진 값 17.27
b=237.7 #b에 주어진 값 237.7

RH=float(input("상대 습도를 0~1로 입력해주세요:"))  #상대습도 입력받아서 RH에 저장
T=int(input("온도°C를 입력해주세요:"))  #온도 입력받아서 T에 저장
FTRH=(a*T)/(b+T)+math.log(math.exp(RH)) #FT,FRT 구하는 공식에 MATH.LOG 함수 사용하여 FTRH에 저장.

print((b*FTRH)/(a-FTRH)) #이슬점 온도Td구하는 공식 사용하여 출력.

    