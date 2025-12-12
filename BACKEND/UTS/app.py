from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'secret123'

# Konfigurasi koneksi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rapehck123'
app.config['MYSQL_DB'] = 'db_armada_penerbangan'

mysql = MySQL(app)

# READ - Tampilkan semua data armada
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM armada")
    data = cur.fetchall()
    return render_template('index.html', armada=data)

# CREATE - Tambah data armada
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nama_pesawat = request.form['nama_pesawat']
        maskapai = request.form['maskapai']
        kapasitas = request.form['kapasitas']
        rute = request.form['rute']
        status = request.form['status']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO armada (nama_pesawat, maskapai, kapasitas, rute, status, departure_time, arrival_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nama_pesawat, maskapai, kapasitas, rute, status, departure_time, arrival_time))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

# UPDATE - Edit data armada
@app.route('/edit/<id_armada>', methods=['GET', 'POST'])
def edit(id_armada):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM armada WHERE id_armada=%s", (id_armada,))
    data = cur.fetchone()

    if request.method == 'POST':
        nama_pesawat = request.form['nama_pesawat']
        maskapai = request.form['maskapai']
        kapasitas = request.form['kapasitas']
        rute = request.form['rute']
        status = request.form['status']
        departure_time = request.form['departure_time']
        arrival_time = request.form['arrival_time']

        cur.execute("""
            UPDATE armada SET nama_pesawat=%s, maskapai=%s, kapasitas=%s, rute=%s, status=%s, departure_time=%s, arrival_time=%s
            WHERE id_armada=%s
        """, (nama_pesawat, maskapai, kapasitas, rute, status, departure_time, arrival_time, id_armada))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', armada=data)

# DELETE - Hapus data armada
@app.route('/delete/<id_armada>', methods=['GET'])
def delete(id_armada):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM armada WHERE id_armada=%s", (id_armada,))
    mysql.connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
