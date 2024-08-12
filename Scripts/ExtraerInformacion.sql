use Seminario2
BULK INSERT Temporal
FROM 'C:\Users\Roberto\Desktop\Semestre\Semi2\Lab\-SS2-Practica1_202000544\Vuelos.csv'
WITH (
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
);

select count(*) from Temporal