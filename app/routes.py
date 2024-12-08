from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from app.models import formulaires
from datetime import datetime

@app.route('/')
@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        try:
            
            upload_dir = app.config['UPLOAD_FOLDER']
            os.makedirs(upload_dir, exist_ok=True)
            
            
            print("Form Data Received:")
            print(request.form)
            print("Files:", request.files)

            
            nom_du_bootcamp = request.form.get('nom_du_bootcamp', '').strip()
            priorite_de_retour = request.form.get('priorite_de_retour', '').strip()
            type_de_retour = request.form.get('type_de_retour', '').strip()
            
            
            dates_str = request.form.get('dates', '')
            try:
                dates = datetime.strptime(dates_str, '%Y-%m-%d').date()
            except ValueError:
                flash("Invalid date format. Please use YYYY-MM-DD", "danger")
                return redirect(url_for('formulaire'))

            
            try:
                evaluation = int(request.form.get('evaluation', 0))
            except ValueError:
                evaluation = 0

            commentaire = request.form.get('commentaire', '').strip()
            droits_donnee = request.form.get('droits_donnee') == 'on'

            
            file = request.files.get('piece_joites')
            file_path = None
            if file and file.filename:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

            new_entry = formulaires(
                nom_du_bootcamp=nom_du_bootcamp,
                priorite_de_retour=priorite_de_retour,
                type_de_retour=type_de_retour,
                dates=dates,
                evaluation=evaluation,
                commentaire=commentaire,
                piece_joites=file_path,
                droits_donnee=droits_donnee
            )

            db.session.add(new_entry)
            db.session.commit()
            flash("Form data saved successfully!", "success")

        except Exception as e:
            print(f"Error saving form: {str(e)}")
            db.session.rollback()
            flash(f"Error saving form data: {str(e)}", "danger")

        return redirect(url_for('result', id=new_entry.id))
    return render_template('form.html')

@app.route('/result/<int:id>', methods=['GET'])
def result(id):
    entry = formulaires.query.get_or_404(id)
    return render_template('result.html', entry=entry)

@app.route('/admin', methods=['GET'])
def admin():
    entries = formulaires.query.all()
    return render_template('admin.html', entries=entries)