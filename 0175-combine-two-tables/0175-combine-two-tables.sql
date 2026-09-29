# Write your MySQL query statement below
SELECT P.firstname, P.lastname, A.City, A.STATE
FROM Person P LEFT JOIN ADDRESS A
ON P.personId = A.personID;