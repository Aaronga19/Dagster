import pandas as pd
from dagster import job, op, get_dagster_logger

# Código para la extracción de datos del archivo excel
@op 
def extract():
    data = pd.read_excel('./data/Matriz_de_adyacencia_data_team.xlsx')
    get_dagster_logger().info(data.to_json())
    pass

@op
def transform():
    pass

@op
def load():
    pass

@job
def update_info():
    extract()







if __name__ == "__main__":
    result = update_info.execute_in_process()