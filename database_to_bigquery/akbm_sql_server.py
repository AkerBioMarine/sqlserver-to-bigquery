import decimal
from database_to_bigquery.sql_server import SqlServerToCsv, SqlServerToBigquery, Column


class AkbmSqlServerToCsv(SqlServerToCsv):
    def safe_cast(self, the_value):
        """
        Cast the value to something bigquery can handle
        """
        if isinstance(the_value, decimal.Decimal):
            # Cast to string so we dont loose precision by casting to float.
            return str(round(the_value, 9))
        else:
            if isinstance(the_value, str):
                # bigquery fails if loading null terminations.
                return the_value.replace(b"\x00".decode(), "")
            return the_value


class AkbmSqlServerToBigquery(SqlServerToBigquery):
    def bq_type(self, sql_server_type: Column):
        conversion = {
            "DATETIME": "TIMESTAMP",
            "NUMBER": "NUMERIC",
            "DECIMAL": "NUMERIC",
            "FLOAT": "FLOAT",
            "INT": "INT64",
            # akbm types
            "MONEY": "NUMERIC"
        }
        for sql_server_type_from, bigquery_type_to in conversion.items():
            if sql_server_type_from in sql_server_type.data_type:
                return bigquery_type_to
        return "STRING"
