__author__ = 'JYC103'

import logging

from flask import Flask,render_template,redirect,url_for,session

from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms.validators import Required
from updatemt import UpdateMtVersion
from wtforms import StringField,SubmitField,IntegerField



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'

# logging.basicConfig(level=logging.DEBUG,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='myapp.log',
#                 filemode='w')


class NameForm(Form):
    version_mt_server_192 = IntegerField('Input version_mt_server_192?',validators=[Required()],default=1)
    version_mt_resource_192 = IntegerField('Input version_mt_resource_192',validators=[Required()],default=1)
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    version_mt_server_192 = None
    version_mt_resource_192 = None
    form = NameForm()
    update_version = UpdateMtVersion()
    if form.validate_on_submit():
        #version_mt_server_192 = form.version_mt_server_192.data
        #version_mt_resource_192 = form.version_mt_resource_192.data
        session['version_mt_server_192'] = form.version_mt_server_192.data
        session['version_mt_resource_192'] = form.version_mt_resource_192.data
        form.version_mt_server_192.data=None
        form.version_mt_resource_192.data =None
        #logging.info(update_version.main(session.get('version_mt_server_192'),session.get('version_mt_resource_192')))
        update_version.main(session.get('version_mt_server_192'),session.get('version_mt_resource_192'))
        return redirect(url_for('index'))
    return render_template('index.html',form=form,version_mt_server_192=session.get('version_mt_server_192'),version_mt_resource_192=session.get('version_mt_resource_192'))


@app.route('/usr/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



if __name__=='__main__':
    app.run(debug=True)