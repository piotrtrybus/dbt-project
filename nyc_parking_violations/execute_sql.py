import duckdb
import pandas as pd

sql_query_1 = '''
create or replace table parking_violation_codes as

select *
from read_csv_auto(
    'data/dof_parking_violation_codes.csv',
    normalize_names=True
    )
'''

sql_query_2 = '''
create or replace table parking_violations_2023 as

select *
from read_csv_auto(
    'data/parking_violations_issued_fiscal_year_2023_sample.csv',
    normalize_names=True
    ) 
'''


sql_query_3 = '''
show tables
'''

sql_query_4 = '''

select * from parking_violation_codes

'''

sql_query_5 = '''

select * from "nyc_parking_violations"."main_dbt_test__audit"."violation_codes_revenue"

'''

sql_query_import_1 = '''

create or replace table parking_violation_codes as

select * 

from read_csv_auto(
    'C:/Users/p_trybus/Downloads/dbt_project/data/dof_parking_violation_codes.csv',
    normalize_names=True
    )

'''

sql_query_import_2 = '''

create or replace table parking_violations_2023 as

select * 

from read_csv_auto(
    'C:/Users/p_trybus/Downloads/dbt_project/data/parking_violations_issued_fiscal_year_2023_sample.csv',
    normalize_names=True
    ) 

'''

with duckdb.connect('C:/Users/p_trybus/Downloads/dbt_project/data/prod_nyc_parking_violations.db') as con:
    con.sql(sql_query_import_1)
    con.sql(sql_query_import_2)
    #df = con.sql(sql_query_4)
    #print(df)