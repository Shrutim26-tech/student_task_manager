import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host = 'gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user = '2Qm2BN2dtSfRcpc.root',
        password = 'eSXv7lvGJXom8OBw',
        database = 'student_task_manager',
        port = 4000
    )

    return connection

# def get_database_connection():
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'Shru@26',
#         database = 'student_task_manager'
#     )

#     return connection