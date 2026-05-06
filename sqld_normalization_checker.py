def check_normalization(issue):
    print(f"\n[분석 대상]: {issue}:")
    if"중복" in issue or "여러 값" in issue:
        print("결과: 제1정규화(1NF)가 필요합니다.")
        print("조치: 속성의 원자성을 확보하세요.(한 칸에 하나씩)")
    elif "부분" in issue or "복합키" in issue:
        print("결과: 제2정규화(2NF)가 필요합니다.")
        print("조치: 부분 함수 종속성을 제거하세요. (기본키 전체에 매달리게)")
    elif "이행" in issue or "일반속성" in issue:
        print("결과: 제3정규화(3NF)가 필요합니다.")
        print("조치 이행 함수 종속성을 제거하세요. (남의 다리 긁지 말기)")
    else:
        print("현재 정규형을 만족하거나 분석이 더 필요합니다.")
study_list = [
    "유형기능분류코드1~9까지 칼럼이 옆으로 나열되어 중복됨",
    "복합키(사번, 부서) 중 부서에만 사무실 번호가 부분 종속됨"
]

for subject in study_list:
    check_normalization(subject)