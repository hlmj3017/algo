-- 코드를 입력하세요
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME; 

-- GROUP BY
-- 1. 집계 함수와 함께 데이터 집계
-- SELECT user_id, SUM(order_quantity)
-- FROM orders
-- GROUP BY user_id;

-- 2. 중복된 값을 제거하고 유니크한 값 확인
-- SELECT department
-- FROM employees
-- GROUP BY department;

-- 3. 그룹 내 조건을 적용하여 데이터 필터링
-- SELECT department, AVG(salary) as avg_salary
-- FROM employees
-- GROUP BY department
-- HAVING AVG(salary) > 50000;