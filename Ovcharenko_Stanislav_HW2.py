import sqlite3
from flask import Flask, request

app = Flask(__name__)


# conn= sqlite3.connect('phones.db')
#
# cur = conn.cursor()
#
# cur.execute('''
# CREATE TABLE phones
# (ContactName varchar(50), Phone varchar(30))''')
#
# conn.commit()
# conn.close()

@app.route('/phones/create/')
def create_phones():
    phone = request.args['phone']
    name = request.args['name']
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        create_sql = f'''
        INSERT INTO phones
        VALUES ('{name}', '{phone}')'''

        cur.execute(create_sql)
        conn.commit()
    finally:
        conn.close()
    return "Create Phones"


@app.route('/phones/read/')
def read_phones():
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        read_sql = '''
        SELECT * FROM phones;
        '''

        cur.execute(read_sql)

        phones = cur.fetchall()
    finally:
        conn.close()
    return str(phones)


@app.route('/phones/delete/')
def delete_phones():
    phone = request.args['phone']
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        delete_sql = f'''
        DELETE FROM phones WHERE Phone == "{phone}";'''

        cur.execute(delete_sql)
        conn.commit()
    finally:
        conn.close()
    return "Delete Phone"


@app.route('/phones/update/')
def update_phones():
    phone = request.args['phone']
    new_phone = request.args['NewPhone']
    try:
        conn = sqlite3.connect('phones.db')
        cur = conn.cursor()
        create_sql = f'''
        UPDATE phones
        SET Phone = '{new_phone}'
        WHERE Phone == '{phone}';'''

        cur.execute(create_sql)
        conn.commit()
    finally:
        conn.close()
    return "Update Phones"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)