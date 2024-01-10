-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME ASC;


-- 다른풀이
-- 코드를 입력하세요
-- in은 시퀀스 타입(리스트, 튜플, 문자열 등)에서 특정 요소가 포함되어 있는지 확인하는데 사용됩니다.
-- in은 딕셔너리에서도 사용될 수 있으며, 이 경우는 딕셔너리의 키에 대한 존재 여부를 확인합니다
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS','GS')
ORDER BY HIRE_YMD DESC, DR_NAME ASC;