from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Page1Data, Page2Data

@app.route('/')
def home():
    return render_template('base.html')

# Page 1 routes
@app.route('/page1', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        field1 = request.form.get('field1')
        field2 = request.form.get('field2')
        new_entry = Page1Data(field1=field1, field2=field2)
        db.session.add(new_entry)
        db.session.commit()
        flash("Entry added successfully!", "success")
        return redirect(url_for('page1'))
    data = Page1Data.query.all()
    return render_template('page1.html', data=data)

@app.route('/page1/delete/<int:id>')
def delete_page1(id):
    entry = Page1Data.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully!", "success")
    return redirect(url_for('page1'))

@app.route('/page1/edit/<int:id>', methods=['GET', 'POST'])
def edit_page1(id):
    entry = Page1Data.query.get_or_404(id)
    if request.method == 'POST':
        entry.field1 = request.form.get('field1')
        entry.field2 = request.form.get('field2')
        db.session.commit()
        flash("Entry updated successfully!", "success")
        return redirect(url_for('page1'))
    return render_template('edit_page1.html', entry=entry)

# Page 2 routes
@app.route('/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        field3 = request.form.get('field3')
        field4 = request.form.get('field4')
        new_entry = Page2Data(field3=field3, field4=field4)
        db.session.add(new_entry)
        db.session.commit()
        flash("Entry added successfully!", "success")
        return redirect(url_for('page2'))
    data = Page2Data.query.all()
    return render_template('page2.html', data=data)

@app.route('/gobuster', methods=['GET', 'POST'])
def gobuster():
    target_v = ""
    g_command = ""
    wordlist = ""
    cookies = ""
    extension = ""

    if request.method == 'POST':
        target_v = request.form.get('target')
        wordlist = request.form.get('wordlist')
        cookies = request.form.get('cookies')
        extension = request.form.get('extension')
        
        action = request.form.get('action')
        if action=='generate':
            g_command = f"gobuster dir {target_v}"
            if wordlist:
                g_command = f"{g_command} -w {wordlist}"
            if cookies:
                g_command = f"{g_command} -c '{cookies}'"
            if extension:
                g_command = f"{g_command} -x {extension}"
        elif action=='instinfo':
            return redirect(url_for('gobusterinfo'))
    return render_template('gobuster/gobuster.html', target=target_v, command=g_command, wordlist=wordlist, cookies=cookies, extension=extension)

@app.route('/gobusterinfo', methods=['GET', 'POST'])
def gobuster_info():
    return render_template('gobuster/gobuster_info.html')



@app.route('/page2/delete/<int:id>')
def delete_page2(id):
    entry = Page2Data.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted successfully!", "success")
    return redirect(url_for('page2'))

@app.route('/page2/edit/<int:id>', methods=['GET', 'POST'])
def edit_page2(id):
    entry = Page2Data.query.get_or_404(id)
    if request.method == 'POST':
        entry.field3 = request.form.get('field3')
        entry.field4 = request.form.get('field4')
        db.session.commit()
        flash("Entry updated successfully!", "success")
        return redirect(url_for('page2'))
    return render_template('edit_page2.html', entry=entry)
