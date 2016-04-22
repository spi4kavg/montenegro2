import os
import datetime
from sqlalchemy.sql import text
from index import connection


if __name__ == "__main__":
    connection.execute(text("""
        DROP TABLE test_table;
        CREATE TABLE test_table (
            "id" serial NOT NULL,
            "timestamp" timestamp without time zone,
            CONSTRAINT test_table_pk PRIMARY KEY (id)
        )
        WITH (
            OIDS=FALSE
        );

        ALTER TABLE test_table
            OWNER TO postgres;
    """))
    dt = datetime.datetime.now()
    for i in range(10):
        rows = []
        dt = datetime.datetime(dt.year + 1, dt.month, dt.day)
        for j in range(100000):
            dt += datetime.timedelta(minutes=1)
            rows.append("('{}')".format(dt))

        connection.execute("""
            INSERT INTO test_table
                ("timestamp")
                VALUES {}
        """.format(",".join(rows)))
