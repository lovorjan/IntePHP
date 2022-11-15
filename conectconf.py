import psycopg2
connection = psycopg2.connect(
                        database='dbname',
                        host='ip',
                        user='integrador',
                        password='contra',
                        port='5432')
