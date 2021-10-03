# 변수선언
a = 1
b = 1.2
c = b

print(id(a), id(1), id(b), id(c))  # 주소값
print(a is b, a == b)  # False False
print(b is c, b == c)  # True True


# type
print(type("str"))  # <class 'str'>
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>

print()


# Integer arithmetic
print(10 + 10)   # 20
print(100 - 10)  # 90
print(10 * 10)   # 100
print(77 / 10)   # 7.7
print(77 // 10)  # 7

print(7 % 2)  # 1
print(8 % 2)  # 0
print(11 % 6.0)  # 5.0
print(10 ** 2)  #

'''
첫 번째 경우, 11 % -5 = -4나머지는 음수여야 하므로 10과 11이 아니라 15와 11을 비교해야 합니다 11 = (-5) * (-3) + (-4). 
두 번째 경우 , -11 % 5 = 4나머지는 양수여야 합니다. -11 = 5 * (-3) + 4.
'''
print(-11 % 5)    # 4
print(11 % -5)    # -4


# 파이썬 변수 명명법 : GNU Naming Convention
mountain_name = "Everest"
EVEREST_HEIGHT = 8848  # 상수 변수


# Boolean
bool1 = False  # False
bool2 = 0 or True  # True
bool3 = 0 or False  # False
bool4 = 0 and True  # 0
bool5 = 0.0 and True  # 0.0
bool6 = "" and True  # ""
bool7 = "" or True  # True
print(bool1, bool2, bool3, bool4, bool5, bool6, bool7)

a = True
b = False
c = a and not b
print(a and (not c or b))  # False


# Comparisons & Dictionary & for & if
Anne = {"name": "Anne", "average_grade": 49, "recommended_by_tutor": True, "finished_intro_course": False, "intro_course_grade": 0}
John = {"name": "John", "average_grade": 41, "recommended_by_tutor": False, "finished_intro_course": True, "intro_course_grade": 76}
Frank = {"name": "Frank", "average_grade": 37, "recommended_by_tutor": True, "finished_intro_course": True, "intro_course_grade": 97}
Victoria = {"name": "Victoria", "average_grade": 40, "recommended_by_tutor": True, "finished_intro_course": True, "intro_course_grade": 86}
Mary = {"name": "Mary", "average_grade": 49, "recommended_by_tutor": False, "finished_intro_course": True, "intro_course_grade": 85}
Sam = {"name": "Sam", "average_grade": 33, "recommended_by_tutor": False, "finished_intro_course": True, "intro_course_grade": 51}

People = [Anne, John, Frank, Victoria, Mary, Sam]

for p in People:
    enroll_student = ((p['average_grade'] >= 40 and p['recommended_by_tutor']) or (p['finished_intro_course'] and p['intro_course_grade'] > 85))
    if enroll_student:
        print(p['name'])


