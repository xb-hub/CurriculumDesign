# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField, TextAreaField, FileField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Required, EqualTo
from flask_pagedown.fields import PageDownField
from flask_ckeditor import CKEditorField
from ..models import Role

# 首页的文章表单
class PostForm(FlaskForm):
    title = StringField(label=u'求助文章标题', validators=[DataRequired()], id='titlecode')
    body = CKEditorField(label=u'求助内容', validators=[DataRequired()])
    kind = SelectField('文章类型', validators=[DataRequired()], 
                        choices=[('学习', '学习'), ('家务', '家务'), ('工作', '工作'),('其他', '其他')],default='其他',
                        coerce=str)
    submit = SubmitField(label=u'提交')

class CommentForm(FlaskForm):
    body = PageDownField(label=u'发表评论', validators=[DataRequired()])
    submit = SubmitField(label=u'提交')


# 普通用户修改信息表单
class EditProfileForm(FlaskForm):
    username = StringField(label=u'用户名', validators=[Length(0,64), DataRequired()])
    name = StringField(label=u'真实姓名', validators=[Length(0,64)])
    location = StringField(label=u'地址', validators=[Length(0,64)])
    about_me = TextAreaField(label=u'关于我')
    submit = SubmitField(label=u'提交')


# 管理员修改信息表单,能编辑用户的电子邮件，用户名，确认状态和角色
class EditProfileAdministratorForm(FlaskForm):
    email = StringField(label=u'邮箱', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField(label=u'用户名', validators=[DataRequired(), Length(1, 64)])
    confirmed = BooleanField(label=u'确认')
    role = SelectField(label=u'角色', coerce=int)

    name = StringField(label=u'真实姓名', validators=[Length(0, 64)])
    location = StringField(label=u'地址', validators=[Length(0, 64)])
    about_me = TextAreaField(label=u'关于我')
    submit = SubmitField(label=u'提交')

    # 初始化时要对role的复选框进行搭建
    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdministratorForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name)]
        self.user = user

# 修改头像表单
class EditAvatarForm(FlaskForm):
    avatar = FileField(label=u'选择头像', validators=[DataRequired()])
    submit = SubmitField(label=u'上传')

# 修改密码
class EditPasswordForm(FlaskForm):
    current_password = PasswordField(label=u'当前密码', validators=[DataRequired()])
    password = PasswordField(label=u'密码', validators=[DataRequired()])
    confirm_password = PasswordField(label=u'确认密码:', validators=[DataRequired(), EqualTo('password', '密码不一致!')])
    submit = SubmitField(label=u'修改')

# 查找文章
# class FindArticleForm(FlaskForm):
#     keyword = StringField(label=u'搜索', validators=[DataRequired(), Length(1, 64)])
#     submit = SubmitField(label=u'查找')