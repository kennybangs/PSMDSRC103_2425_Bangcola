CREATE VIEW V_PROFESSORS AS 

SELECT EMPLOYEE_ID
,FIRST_NAME
,LAST_NAME
,DEPARTMENTS.NAME AS DEPARTMENT
,TITLES.NAME AS POSITION
,HIRE_DATE
FROM PROFESSORS
LEFT JOIN DEPARTMENTS ON PROFESSORS.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
LEFT JOIN TITLES ON PROFESSORS.TITLE_ID = TITLES.TITLE_ID