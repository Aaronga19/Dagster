#
from setup import environment_vars_schedule
# librerias para leer el archivo de excel
import pandas as pd
from dagster import job, op, get_dagster_logger, schedule, ScheduleEvaluationContext, RunRequest
# para base de datos
from database.models import Base, engine
from database.database import session
from database.models import Relation

# Código para la extracción de datos del archivo excel
@op
def extract():
    """ Función de lectura del archivo excel"""
    data = pd.read_excel('./data/Matriz_de_adyacencia_data_team.xlsx', header=1, index_col=[0,1])
    get_dagster_logger().info("Datos extraidos de formato excel")
    # get_dagster_logger().info(data)
    return data

@op
def transform():
    data = extract()
    get_dagster_logger().info("Entrando a la transformación de datos")
    data = data.dropna()
    get_dagster_logger().info(f'registros encontrados: {len(data)}')
    return data

@op
def load():
    Base.metadata.drop_all(engine)
    get_dagster_logger().info("Base de datos borrada")
    Base.metadata.create_all(engine)
    get_dagster_logger().info("Base de datos creada")
    data = transform()
    get_dagster_logger().info("Iniciando guardado de datos en Data Warehouse")
    # Extraer usuarios
    for user in range(len(data)):
        userRecords = data.iloc[user]
        print(f'usuario:{user}')
        relation = Relation(
            A = userRecords['A'],
            B = userRecords['B'],
            C = userRecords['C'],
            D = userRecords['D'],
            E = userRecords['E'],
            F = userRecords['F'],
            G = userRecords['G'],
            H = userRecords['H'],
            I = userRecords['I'],
            J = userRecords['J'],
            K = userRecords['K'],
            L = userRecords['L'],
            M = userRecords['M'],
            N = userRecords['N'],
            Ñ = userRecords['Ñ'],
            O = userRecords['O'],
            P = userRecords['P'],
            Q = userRecords['Q'],
            R = userRecords['R'],
            S = userRecords['S'],
            T = userRecords['T'],
            U = userRecords['U'],
            V = userRecords['V'],
            W = userRecords['W'],
            X = userRecords['X'],
            Y = userRecords['Y'],
            Z = userRecords['Z'],
            AA = userRecords['AA'],
            AB = userRecords['AB'],
            AC = userRecords['AC'],
            AD = userRecords['AD'],
            AE = userRecords['AE'],
            AF = userRecords['AF'],
            AG = userRecords['AG'],
            AH = userRecords['AH'],
            AI = userRecords['AI'],
            AJ = userRecords['AJ'],
            AK = userRecords['AK'],
            AL = userRecords['G'],
            AM = userRecords['AM'],
            AN = userRecords['AN'],
            AÑ = userRecords['AÑ'],
            AO = userRecords['AO'],
            AP = userRecords['AP'],
            AQ = userRecords['AQ'],
            AR = userRecords['AR'],
            AS = userRecords['AS'],
            AT = userRecords['AT'],
            AW = userRecords['AW'],
            AX = userRecords['AX'],
        )
        session.add(relation)
        session.commit()
        print(f'usuario:{user} listo')

    get_dagster_logger().info("Se han guardado los datos correctamente")


@op
def etl():
    load()

@job
def update_warehouse():
    etl()

# @schedule(job=update_warehouse, cron_schedule="0 2 * * *", environment_vars=environment_vars_schedule)
# def update_warehouse_schedule(context: ScheduleEvaluationContext):
#     scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
#     return RunRequest(
#         run_key=None,
#         run_config={"ops": {"configurable_op": {"config": {"scheduled_date": scheduled_date}}}},
#         tags={"date": scheduled_date},
#     )




if __name__ == "__main__":
    result = update_warehouse.execute_in_process()