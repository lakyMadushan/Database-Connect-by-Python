import mysql.connector
query = "SELECT * FROM users"

# Other function can run in here.
# String query = "INSERT INTO users VALUES ('Gayan',25)";
# String query = "DELETE FROM users WHERE age=24";
# String query = "UPDATE users SET age=39 WHERE name='Kamal";
# String query = "CREATE TABLE subjects ( Code VARCHAR(10), Name VARCHAR(20)";
# String query = "DROP TABLE subjects";

try:
    connection = mysql.connector.connect(host='localhost', database='connector', user='root', password='lak170BG@')
    cursor = connection.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    print(result)

    connection.commit()
except:
    print("Somthing went wrong")
finally:
    if connection.is_connected():
        connection.close()