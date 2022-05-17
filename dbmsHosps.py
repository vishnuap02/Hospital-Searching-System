import pymysql

def connection():
    s = '127.0.0.1'
    d = 'hospital'
    u = 'root'
    p = 'Vishnuap@02'
    conn = pymysql.connect(host=s, user=u, password=p, database=d)
    return conn

# Completed (nothing to change)
def displayresults(placename,beds):
    hosps = []
    query = 'SELECT HOSPITALNAME,ADDRESS,'+beds+' FROM HOSPITALS WHERE CITY = "'+ placename+ '" AND '+beds+">0 ;"
    conn = connection()
    cursor = conn.cursor()
    print(query)
    cursor.execute(query)
    for row in cursor.fetchall():
        hosps.append({"HOSPITALNAME": row[0], "ADDRESS": row[1] , "beds" : row[2]},)
    conn.close()
    return hosps

# Completed (nothing to change)
def countresults(tname,placename):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM ' +tname+' WHERE CITY = "' + placename +'" ;')
    total = cursor.fetchone()
    conn.close()
    # total is a tuple , so need to extract a word and
    return total

# Completed (nothing to change)
def totalcount(tname):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM "+ tname)
    total = cursor.fetchone()
    conn.close()
    return total[0]

# Completed (nothing to change)
def totalValuecount(tname,beds):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM("+beds+") FROM " + tname)
    total = cursor.fetchone()
    conn.close()
    return total[0]

def updatehosps(id,icubeds,gwbeds,ot):
    msg="Updated Successfully .!"
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE HOSPITALS SET ICUBEDS= %s,GENWARDBEDS=%s ,OPETHEATER=%s WHERE ID=%s",(icubeds, gwbeds, ot,id))
    conn.commit()
    conn.close()
    return msg


# Completed (nothing to change)
def loginfetch(tname,id,password):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM "+tname+' WHERE ID = "'+id+'" AND PASSW = "'+password+'" ;')
    hosps = cursor.fetchone()
    conn.close()
    return hosps

def displayelements(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM HOSPITALS WHERE ID = %s ;", (id))
    hosps = cursor.fetchone()
    # .fetchall,fetchmany(size) returns a list of tuples when called.
    conn.close()
    return hosps


def displaydoctors(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM DOCTORS WHERE ID = %s ;", (id))
    hosps = cursor.fetchone()
    # .fetchall,fetchmany(size) returns a list of tuples when called.
    conn.close()
    return hosps


def registerhosps(id,hname,password,email,address,city,state,country,pcode,icubeds,gwbeds,ot):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO HOSPITALS(id,hospitalname,passw,email,address,city,state,country,postcode,icubeds,genwardbeds,opetheater) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,hname,password,email,address,city,state,country,pcode,icubeds,gwbeds,ot))
    conn.commit()
    conn.close()
    return "Registered Successfully !!"

def doctorregister(id,password,fname,lname ,rating,spl,experience):
    conn= connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO DOCTORS(id,passw,fname,lname ,rating,spl,experience) VALUES(%s,%s,%s,%s,%s,%s,%s)",(id,password,fname,lname ,rating,spl,experience))
    conn.commit()
    conn.close()
    return "SuccessFully registered"

# "RuntimeError: 'cryptography' package is required for sha256_password or
# caching_sha2_password auth methods in flask" error is coming if mysql is not opened.