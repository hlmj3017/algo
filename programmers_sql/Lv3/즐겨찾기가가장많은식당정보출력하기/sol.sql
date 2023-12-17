-- SQL 쿼리의 진행순서떄문이라고 한다 
-- 즉 GROUP BY 후 그냥 MAX를 해버리면 이는 최대값이 아니라 테이블 최상단 값을 가져와서 
-- 서브쿼리로 최대 값을 따로 찾아준다

-- 코드를 입력하세요
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE FAVORITES IN (SELECT MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE)
GROUP BY FOOD_TYPE
ORDER BY FOOD_TYPE DESC;

-- 다른 풀이
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES) FROM REST_INFO GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC;