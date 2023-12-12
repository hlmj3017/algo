-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE a.SEX_UPON_INTAKE like 'Intact%' and b.SEX_UPON_OUTCOME not like 'Intact%'
-- WHERE A.SEX_UPON_INTAKE NOT IN ('Spayed', 'Neutered') AND B.SEX_UPON_OUTCOME IN ('Spayed', 'Neutered')
-- in은 둘 중 하나만 가능해도 성립하므로 이렇게 작성하면 안 됨
ORDER BY A.ANIMAL_ID;
