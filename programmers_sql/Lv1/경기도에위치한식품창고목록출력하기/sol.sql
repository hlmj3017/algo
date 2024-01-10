-- 코드를 입력하세요
-- null 인 부분의 문제만 해결하기 때문에 해당 문제와는 가장 근접하지만 null 이 아닌 부분은 무시하게 된다.
-- ifnull
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "%경기도%"
ORDER BY WAREHOUSE_ID;

-- if
select warehouse_id, warehouse_name, address, (if(freezer_yn is null, 'N', 'Y')) freezer_yn
from food_warehouse
where address like "경기도%"
order by warehouse_id asc;


-- case when
-- freezer_yz이 NULL인 경우에 'N'을 입력,
-- Else 그외 경우는 그대로 들어가도록 입력. 무언가 조건이 여러개 달려야 하는 경우 사용하면 시인성이 좋을 것 같다.
select * from food_warehouse;

select  warehouse_id, 
        warehouse_name, 
        address, 
        (CASE
            WHEN freezer_yn is null THEN 'N'
            ELSE freezer_yn
        END	) as freezer_yn 
    from food_warehouse
    where address like "경기도%"
    order by warehouse_id asc;