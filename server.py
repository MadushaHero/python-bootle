from bottle import default_app, run, get
import json
import mysql.connector

#####################################

try:
    #production
    
    
    import production
    db_config = {

        "host":"madushalakmal.mysql.pythonanywhere-services.com",
        "user":"madushalakmal",
        "password":"\XD{HH\PH@",
        "database":"madushalakmal$company"

    }


except Exception as ex:

    #development
    print(ex)
    db_config = {

        "host":"localhost",
        "user":"root",
        "password":"",
        "database":"company"
        
    }

    #####################

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

@get("/seed-users-table")
def seed_users_table():
 cursor.execute("INSERT INTO users VALUES (null,'A','AA') ")
 db.commit()
 return "user created"

     #####################################
@get("/get-users")
def get_users():
  cursor.execute("SELECT * FROM users")
  rows = cursor.fetchall()
  return json.dumps(rows)
     




    #####################################

try:
    #production
    import production
    application = default_app()
    
    
  


except Exception as ex:
    #development
    run(host="localhost",port=8080,debug=True,reloader=True)

    

    #####################



