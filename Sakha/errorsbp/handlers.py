from flask import Blueprint, render_template


handlers = Blueprint('handlersbp', __name__)


errors = ['Sorry, requested page is not found', 'Access Forbidden', 'File of size upto 5MB is allowed to upload', 'Server is down']


@handlers.app_errorhandler(404)
def pageNotFound(_):
    return render_template('errors/error.html', title='Page not found', error_code=404, msg=errors[0]), 404


@handlers.app_errorhandler(403)
def permissionDenied(_):
    return render_template('errors/error.html', title='Permission denied', error_code=403, msg=errors[1]), 403


@handlers.app_errorhandler(413)
def tooLarge(_):
    return render_template('errors/error.html', title='Too large', error_code=413, msg=errors[2]), 413


@handlers.app_errorhandler(500)
def serverError(_):
    return render_template('errors/error.html',title='Server down', error_code=500, msg=errors[3]), 500