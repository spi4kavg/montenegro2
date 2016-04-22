# -*- coding: utf-8 -*-
import sys
import getopt
import datetime
import time
import sqlalchemy
from sql import (
    CREATE_INDEX,
    DROP_INDEX,
    DELETE_QUERY,
    SELECT_MIN_TS
)


CONNECTION_TEXT = "postgresql://postgres:postgres@localhost:5432/montenegro2"


engine = sqlalchemy.create_engine(CONNECTION_TEXT)
connection = engine.connect()


def main(ds, count):

    de = datetime.datetime(ds.year, 12, 31)

    for i in range(count):
        # iterate by count
        # creates year index
        connection.execute(CREATE_INDEX.format(ds.isoformat(), de.isoformat()))

        rowcount = 1

        while rowcount:
            # delete year by 100 rows
            res = connection.execute(DELETE_QUERY.format(
                ds.isoformat(),
                de.isoformat()
            ))
            rowcount = res.rowcount
            time.sleep(0.2)

        # drops year index
        connection.execute(DROP_INDEX)

        print('deleted from {} to {}'.format(ds.isoformat(), de.isoformat()))
        # sets next year range
        ds = datetime.datetime(de.year + 1, 1, 1)
        de = datetime.datetime(ds.year, 12, 31)


if __name__ == "__main__":
    # gets date start and date end from CLI and call main
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, 's:c:')

    date_start = None
    count = None
    for k, v in opts:
        if k == '-s':
            date_start = v
        elif k == '-c':
            count = v

    if date_start:
        date_start = datetime.datetime.strptime(date_start, '%Y-%m-%d')

    count = int(count) if count else 5

    if not date_start:
        # if not exist datestart
        # gets minimal timestamp from db
        res = connection.execute(SELECT_MIN_TS)
        date_start = res.scalar()

    main(date_start, count)
