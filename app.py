from flask import Flask, request
from mysql.connector import connect, Error
from datetime import datetime


def setdata(datam,datetimem):
    try:
        with connect(host="den1.mysql3.gear.host ",user="ioeproj1",password="Os4KoJ7ZP!-z",database="ioeproj1",) as connection:
            print(connection)
            create_movies_table_query = "INSERT INTO gasdata(timedata,datafromsensor) values(%s,%s);" 
            with connection.cursor() as cursor:
                cursor.execute(create_movies_table_query,(str(datetimem),str(datam)))
                connection.commit()

    except Error as e:
        print(e)
    


app = Flask(__name__)



@app.route("/setdata", methods=['POST'])
def communicate():
    some_json=request.get_json()
    
    data = some_json['data']
    setdata(data, datetime.now())
    response = "OK"  
    return str(response)

if __name__=='__main__':
    app.run(debug=True)
    #setdata(str(50),str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))

