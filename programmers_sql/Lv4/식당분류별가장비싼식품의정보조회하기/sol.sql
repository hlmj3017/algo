-- 코드를 입력하세요
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
AND CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC;


-- 이 결과는 같은건지? 코드 제출은 안 됐음
SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
GROUP BY CATEGORY
HAVING CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY MAX_PRICE DESC;


-- 두 번째 쿼리에서는 각 카테고리별로 최대 가격을 그룹화하고 있으며, 그룹화된 결과 중에서 필터링된 카테고리만 남겨둡니다. 
-- 그런 다음 최종 결과를 최대 가격을 기준으로 내림차순으로 정렬합니다.

-- 반면 첫 번째 쿼리는 서브쿼리를 사용하여 각 카테고리에 대한 최대 가격을 찾고, 이 최대 가격과 일치하는 행들만 선택합니다. 
-- 그리고 그 결과를 최대 가격을 기준으로 내림차순으로 정렬합니다.