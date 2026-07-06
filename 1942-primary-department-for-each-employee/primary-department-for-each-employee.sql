SELECT e1.employee_id, e1.department_id
FROM Employee e1
WHERE primary_flag = 'Y' OR (SELECT COUNT(e2.department_id) FROM Employee e2 WHERE e1.employee_id = e2.employee_id)=1;

