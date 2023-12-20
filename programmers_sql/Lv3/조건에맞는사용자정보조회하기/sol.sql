-- 코드를 입력하세요
SELECT USER_ID, NICKNAME, CONCAT(CITY, ' ',STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
CONCAT(LEFT(TLNO,3), '-', MID(TLNO,4,4), '-', RIGHT(TLNO,4)) AS 전화번호
FROM USED_GOODS_BOARD A
JOIN USED_GOODS_USER B
ON A.WRITER_ID = B.USER_ID
GROUP BY WRITER_ID
HAVING COUNT(WRITER_ID) >= 3
ORDER BY USER_ID DESC;