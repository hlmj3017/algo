-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK A
JOIN BOOK_SALES B
ON A.BOOK_ID = B.BOOK_ID
WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
# WHERE SALES_DATE LIKE '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY;
