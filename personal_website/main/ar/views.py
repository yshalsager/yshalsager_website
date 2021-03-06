from flask import render_template, url_for
from flask_babel import force_locale as force_locale, _

from ..utils.posts import get_blog_posts
from .. import main


@main.route('/ar/')
def index_ar():
    with force_locale('ar'):
        return render_template('index.html', lang="ar", image=url_for('static', filename='img/home-bg.jpg'))


@main.route('/ar/about')
def about_ar():
    with force_locale('ar'):
        return render_template('about.html', lang="ar",
                               heading=_("About Me"), image=url_for('static', filename='img/home-bg.jpg'))


@main.route('/ar/blog')
def blog_ar():
    posts = get_blog_posts('ar')
    with force_locale('ar'):
        return render_template('blog.html', heading=_("Blog"),
                               image=url_for('static', filename='img/home-bg.jpg'),
                               lang='ar', posts=posts)


@main.route('/ar/projects')
def projects_ar():
    with force_locale('ar'):
        return render_template('projects.html', heading=_("My Works and Projects"),
                               lang="ar", image=url_for('static', filename='img/home-bg.jpg'))


@main.route('/ar/contact')
def contact_ar():
    with force_locale('ar'):
        email_body = _('Hi yshalsager, I came across your website and would like to get in touch.')
        return render_template('contact.html', lang="ar", email_body=email_body,
                               heading=_("Contact Me"), image=url_for('static', filename='img/contact.webp'))
