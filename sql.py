# -*- coding: utf-8 -*-


CREATE_INDEX = """
    CREATE INDEX test_table_timestamp ON test_table("timestamp")
        WHERE
            "timestamp" >= '{}'::timestamp
            AND
            "timestamp" <= '{}'::timestamp
"""

DROP_INDEX = "DROP INDEX test_table_timestamp"

DELETE_QUERY = """
    WITH F AS (
        SELECT id
        FROM test_table
        WHERE "timestamp" >= '{}'::timestamp
        AND
        "timestamp" <= '{}'::timestamp
        LIMIT 100
    )
    DELETE FROM test_table
    WHERE id in (
        SELECT * FROM F
    )
"""

SELECT_MIN_TS = """
    SELECT MIN("timestamp")
    FROM test_table
"""