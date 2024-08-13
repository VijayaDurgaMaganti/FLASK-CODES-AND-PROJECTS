from flask import Flask,request,redirect,url_for,render_template,flash,session,send_file
from flask_session import Session
import mysql.connector
from io import BytesIO

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('welcome.html')

#file uploading - new files uploading
@app.route('/fileupload',methods=['GET','POST'])
def fileupload():
      if not session.get('email'):
           return redirect(url_for('login'))
      else:
           if request.method=='POST':
                file=request.files['file']
                file_name=file.filename
                added_by=session.get('email')
                cursor=mydb.cursor(buffered=True)
                cursor.execute('insert into files_data(file_name,file_data,added_by) values(%s %s %s))',[file_name,file_data,added_by])
                mydb.commit()
                cursor.close()
                flash(f'file {file.fiename} added successfully')
                return redirect(url_for('panel'))
      return render_template('fileupload.html')

#view_files - viewing the files
@app.route('/viewall_files')
def viewall_files():
     if not session.get('email'):
          return redirect(url_for('login'))
     else:
          added_by=session.get('email')
          cursor=mydb.cursor(buffered=True)
          cursor.execute('select f_id,file_name,created_at from files_data where added_by=%s',[added_by])
          data=cursor.fetchall()
          return render_template('allfiles',data=data)
     
#backend data fetching from database and viewing the file in flask
@app.route('/view_file/<fid>') 
def view_file(fid):
     if not session.get('email'):
          return redirect(url_for('login'))   
     else:
        try:
             cursor=mydb.cursor(buffered=True)
             cursor.execute('select file_name,file_data from files_data where f_id=%s and added_by=%s',[fid,session.get('email')])
             fname,fdata=cursor.fetchone()
             bytes_data=BytesIO(fdata)
             filename=fname
             return send_file(bytes_data,download_name=filename,as_attachment=False)
        except Exception as e:
             print(e)
             return 'file not found'
        finally:
             cursor.close() 
#download single file
@app.route('/download_file/<fid>') 
def download_file(fid):
     if not session.get('email'):
          return redirect(url_for('login'))   
     else:
        try:
             cursor=mydb.cursor(buffered=True)
             cursor.execute('select file_name,file_data from files_data where f_id=%s and added_by=%s',[fid,session.get('email')])
             fname,fdata=cursor.fetchone()
             bytes_data=BytesIO(fdata)
             filename=fname
             return send_file(bytes_data,download_name=filename,as_attachment=False)
        except Exception as e:
             print(e)
             return 'file not found'
        finally:
             cursor.close()      
app.run(debug=True,use_reloader=True)
