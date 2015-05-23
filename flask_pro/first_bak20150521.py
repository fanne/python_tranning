__author__ = 'JYC103'

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import Required




app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'


class NameForm(Form):
    version_mt_server_192 = StringField('Input version_mt_server_192?',validators=[Required()])
    version_mt_resource_192 = IntegerField('Input version_mt_resource_192',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    version_mt_server_192 = None
    version_mt_resource_192 = None
    form = NameForm()
    if form.validate_on_submit():
        version_mt_server_192 = form.version_mt_server_192.data
        version_mt_resource_192 = form.version_mt_resource_192.data
        form.version_mt_server_192.data=''
        form.version_mt_resource_192.data=None
    print version_mt_resource_192,version_mt_server_192
    return render_template('index.html',form=form,version_mt_server_192=version_mt_server_192,version_mt_resource_192=version_mt_resource_192)



@app.route('/usr/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



if __name__=='__main__':
    app.run(debug=True)
