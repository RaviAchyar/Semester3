from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_mysqldb import MySQL
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secret123'

# Konfigurasi koneksi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rapehck123'
app.config['MYSQL_DB'] = 'crud_upload_db'
app.config['UPLOAD_FOLDER'] = os.path.abspath('uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

mysql = MySQL(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
# READ - Tampilkan semua data
@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stok")
    data = cur.fetchall()
    return render_template('index.html', files=data)

# Menampilkan gambar di folder uploads
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# CREATE - Tambah data
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO stok (kode, nama, harga, filename) VALUES (%s, %s, %s, %s)", (kode, nama, harga, filename))
            mysql.connection.commit()
            return redirect(url_for('index'))

    return render_template('add.html')

# DELETE - Hapus data
@app.route('/delete/<id>', methods=['GET'])
def delete_file(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT filename FROM stok WHERE kode=%s", (id,))
    file_data = cur.fetchone()
    if file_data:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_data[0]))
        cur.execute("DELETE FROM stok WHERE kode = %s", (id, ))
        mysql.connection.commit()
    return redirect(url_for('index'))

# UPDATE - Edit data
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_file(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM stok WHERE kode=%s", (id,))
    file_data = cur.fetchone()

    if request.method == 'POST':
        if file_data:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], file_data[3]))
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        new_file = request.files['file']

        # Ganti gambar baru
        if new_file and allowed_file(new_file.filename):
            filename = secure_filename(new_file.filename)
            new_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            cur.execute("UPDATE stok SET kode= %s, nama = %s, harga = %s, filename = %s WHERE kode = %s", (kode, nama, harga, filename, id))
        else:
            cur.execute("UPDATE stok SET kode= %s, nama = %s, harga = %s WHERE kode = %s", (kode, nama, harga, id))
        mysql.connection.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', file=file_data)

if __name__ == '__main__':
    app.run(debug=True)