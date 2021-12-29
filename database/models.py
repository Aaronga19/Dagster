from dagster import resource, Field, String, graph, op, repository
import sqlalchemy
from .database import Base, engine

# Solución SQLAlchemy
class Actor(Base):
    __tablename__ = 'actors'
    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(100), unique=True)
    # word = sqlalchemy.relationship('Relation', backref='Actor_Relation', lazy=True)

class Relation(Base):
    """ Modelo de tabla de excel para relacion de usuarios """
    __tablename__ = "relations"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    # No funcionó, por lo que se configurará manaulmente
    """for column in keys:
        print(f'ant-{column}')
        column = sqlalchemy.Column(sqlalchemy.String(3))
        print(f'des-{column}')"""
    A = sqlalchemy.Column(sqlalchemy.Integer)
    B = sqlalchemy.Column(sqlalchemy.Integer)
    C = sqlalchemy.Column(sqlalchemy.Integer)
    D = sqlalchemy.Column(sqlalchemy.Integer)
    E = sqlalchemy.Column(sqlalchemy.Integer)
    F = sqlalchemy.Column(sqlalchemy.Integer)
    G = sqlalchemy.Column(sqlalchemy.Integer)
    H = sqlalchemy.Column(sqlalchemy.Integer)
    I = sqlalchemy.Column(sqlalchemy.Integer)
    J = sqlalchemy.Column(sqlalchemy.Integer)
    K = sqlalchemy.Column(sqlalchemy.Integer)
    L = sqlalchemy.Column(sqlalchemy.Integer)
    M = sqlalchemy.Column(sqlalchemy.Integer)
    N = sqlalchemy.Column(sqlalchemy.Integer)
    Ñ = sqlalchemy.Column(sqlalchemy.Integer)
    O = sqlalchemy.Column(sqlalchemy.Integer)
    P = sqlalchemy.Column(sqlalchemy.Integer)
    Q = sqlalchemy.Column(sqlalchemy.Integer)
    R = sqlalchemy.Column(sqlalchemy.Integer)
    S = sqlalchemy.Column(sqlalchemy.Integer)
    T = sqlalchemy.Column(sqlalchemy.Integer)
    U = sqlalchemy.Column(sqlalchemy.Integer)
    V = sqlalchemy.Column(sqlalchemy.Integer)
    W = sqlalchemy.Column(sqlalchemy.Integer)
    X = sqlalchemy.Column(sqlalchemy.Integer)
    Y = sqlalchemy.Column(sqlalchemy.Integer)
    Z = sqlalchemy.Column(sqlalchemy.Integer)
    AA = sqlalchemy.Column(sqlalchemy.Integer)
    AB = sqlalchemy.Column(sqlalchemy.Integer)
    AC = sqlalchemy.Column(sqlalchemy.Integer)
    AD = sqlalchemy.Column(sqlalchemy.Integer)
    AE = sqlalchemy.Column(sqlalchemy.Integer)
    AF = sqlalchemy.Column(sqlalchemy.Integer)
    AG = sqlalchemy.Column(sqlalchemy.Integer)
    AH = sqlalchemy.Column(sqlalchemy.Integer)
    AI = sqlalchemy.Column(sqlalchemy.Integer)
    AJ = sqlalchemy.Column(sqlalchemy.Integer)
    AK = sqlalchemy.Column(sqlalchemy.Integer)
    AL = sqlalchemy.Column(sqlalchemy.Integer)
    AM = sqlalchemy.Column(sqlalchemy.Integer)
    AN = sqlalchemy.Column(sqlalchemy.Integer)
    AÑ = sqlalchemy.Column(sqlalchemy.Integer)
    AO = sqlalchemy.Column(sqlalchemy.Integer)
    AP = sqlalchemy.Column(sqlalchemy.Integer)
    AQ = sqlalchemy.Column(sqlalchemy.Integer)
    AR = sqlalchemy.Column(sqlalchemy.Integer)
    AS = sqlalchemy.Column(sqlalchemy.Integer)
    AT = sqlalchemy.Column(sqlalchemy.Integer)
    AW = sqlalchemy.Column(sqlalchemy.Integer)
    AX = sqlalchemy.Column(sqlalchemy.Integer) 
    

    def __str__(self):
        return f'Relación añadida con id: {self.id}'

if __name__ == '__main__':
    " Ejecutar este script para crear base de datos en postgres"
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print('Base de datos configurada')

# Con la documentación de Dagster
# class SqlAlchemyPostgresWarehouse:
#     def __init__(self, conn_str):
#         self._conn_str = conn_str
#         self._engine = sqlalchemy.create_engine(self._conn_str)

#     def update_normalized_cereals(self, records):
#         Base.metadata.bind = self._engine
#         Base.metadata.drop_all(self._engine)
#         Base.metadata.create_all(self._engine)
#         Record.__table__.insert().execute(records)


# @resource(config_schema={"conn_str": Field(String)})
# def sqlalchemy_postgres_warehouse_resource(context):
#     return SqlAlchemyPostgresWarehouse(context.resource_config["conn_str"])