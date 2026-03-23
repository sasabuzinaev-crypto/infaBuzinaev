import pandas as pd
import sqlite3 
from datetime import datetime


dillers = pd.read_csv('BDSanya/dillers.csv', sep=';')
marks = pd.read_csv('BDSanya/marks.csv', sep=';')
availability = pd.read_csv('BDSanya/availability.csv', sep=';')
dillers.columns = dillers.columns.str.strip()
marks.columns = marks.columns.str.strip()
availability.columns = availability.columns.str.strip()

conn = sqlite3.connect(':memory:')

dillers.to_sql('dillers', conn, index=False)
marks.to_sql('marks', conn, index=False)
availability.to_sql('availability', conn, index=False)

print(dillers.head())
print(marks.head())
print(availability.head())
query = """
WITH moscow_domestic AS (
    SELECT
        a."Дата"          AS op_date,
        a."Количество"    AS qty,
        a."Тип операции"  AS op_type
    FROM availability a
    JOIN dillers d ON a."ID дилера" = d."ID дилера"
    JOIN marks m   ON a."ID машины" = m."ID машины"
    WHERE d."Адрес" LIKE 'Москва%'
      AND m."Категория" = 'Отечественные автомобили'
),
balances AS (
    SELECT
        COALESCE(SUM(
            CASE WHEN DATE(op_date) <= '2021-01-01'
                 THEN CASE WHEN op_type = 'Поступило дилеру' THEN qty ELSE -qty END
            END
        ), 0) AS bal_2021,
        COALESCE(SUM(
            CASE WHEN DATE(op_date) <= '2022-01-01'
                 THEN CASE WHEN op_type = 'Поступило дилеру' THEN qty ELSE -qty END
            END
        ), 0) AS bal_2022
    FROM moscow_domestic
)
SELECT (bal_2022 - bal_2021) AS result
FROM balances;
"""

result = pd.read_sql_query(query,conn)
print(result)
