#!/bin/bash

# Wait for SQL Server to start up by checking if the port is open
echo "Waiting for SQL Server to start..."
for i in {1..60};
do
    /opt/mssql-tools18/bin/sqlcmd -C -S db -U sa -P $MSSQL_SA_PASSWORD -Q "SELECT 1" &> /dev/null
    if [ $? -eq 0 ]
    then
        echo "SQL Server is up - executing script"
        /opt/mssql-tools18/bin/sqlcmd -C -S db -U sa -P $MSSQL_SA_PASSWORD -i /usr/config/setup.sql
        break
    else
        echo "SQL Server is still starting up..."
        sleep 1
    fi
done
