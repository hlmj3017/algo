-- 코드를 입력하세요
-- DISTINCT : 중복을 없애주지만 정렬을 해주지 않는다.
-- GROUP BY : 중복을 없애주고 정렬도 해준다.
SELECT COUNT(DISTINCT(NAME)) AS COUNT
FROM ANIMAL_INS
WHERE NAME != "NULL";

-- 다른 풀이
SELECT COUNT(*) AS COUNT
FROM (
    SELECT NAME
    FROM ANIMAL_INS
    WHERE NAME IS NOT NULL
    GROUP BY NAME
) AS A;

-- 다른 풀이
SELECT COUNT(DISTINCT(NAME)) AS COUNT
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;