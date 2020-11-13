-- Slave Rio tworzenie snapshota insurers odświerzanie 10s
CREATE SNAPSHOT insurers
BUILD IMMEDIATE
REFRESH FAST
NEXT SYSDATE+(1/(24*60*6))
AS 
SELECT id, name FROM insurers@tokyo_link; -- dopisać linki

CREATE VIEW insurers_global
AS SELECT * FROM insurers
UNION SELECT * FROM insurers_remote;