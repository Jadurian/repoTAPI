CREATE VIEW [View_Test3_VG] AS
SELECT *
FROM Hist_Bk
WHERE FECHA < DATEADD(month, -1, DATEADD(month, DATEDIFF(month, 0, GETDATE()), 0))
UNION ALL
SELECT *
FROM Valores_Gen_Diario_Automatico
WHERE FECHA >= DATEADD(month, -1, DATEADD(month, DATEDIFF(month, 0, GETDATE()), 0));
