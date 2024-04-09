def calGrade (score) :
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else :
        return "F"

def calgradeMain():
    kor_score = int (input ('국어 점수를 입력 하시오: '))
    math_score = int (input ('수학 점수를 입력 하시오: '))
    eng_score = int (input ('영어 점수를 입력 하시오: '))
    kor_grade = calGrade (kor_score)
    math_grade = calGrade (math_score)
    eng_grade = calGrade (eng_score)
    print ('국어 학점은 ', kor_grade, '입니다')
    print ('수학 학점은 ', math_grade, '입니다')
    print ('영어 학점은 ', eng_grade, '입니다')
    
