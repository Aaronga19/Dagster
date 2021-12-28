from dagster import resource, Field, String, graph, op, repository
import sqlalchemy
from database.database import Base, engine
from testing import keys

class Record(Base):
    __tablename__ = "records"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    for key in keys:
        key = sqlalchemy.Column(sqlalchemy.String(length=3, nullable=True))

    def __str__(self):
        return f'record added with id: {self.id}'

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

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