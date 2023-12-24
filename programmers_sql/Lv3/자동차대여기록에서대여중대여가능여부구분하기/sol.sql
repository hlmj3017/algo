-- 코드를 입력하세요
-- CAR_ID별로 여러 기록이 있고, 그 중에서도 가장 나중에 렌탈 기록이 끝난걸 확인해야 한다 -> MAX
SELECT CAR_ID,
MAX(CASE WHEN DATE_FORMAT(START_DATE, '%Y-%m-%d') <= '2022-10-16' AND '2022-10-16' <= DATE_FORMAT(END_DATE, '%Y-%m-%d') THEN '대여중'
ELSE '대여 가능'
END) AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;

-- 다른 풀이
SELECT CAR_ID,
MAX(CASE WHEN '2022-10-16' BETWEEN DATE_FORMAT(START_DATE, '%Y-%m-%d') AND DATE_FORMAT(END_DATE, '%Y-%m-%d')
THEN '대여중'
ELSE '대여 가능'
END) AS 'AVAILABILITY'
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC