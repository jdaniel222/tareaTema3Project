from flask import render_template
import app
from . import public


@public.route('/')
def index():  # put application's code here
    app.logger.info("Mensaje de información")
    app.logger.debug("Mensaje de depuración")
    app.logger.warning("Mensaje de advertencia")
    app.logger.error("Mensaje de error")
    app.logger.exception("Mensaje de excepción")
    app.logger.critical("Mensaje critico")
    return render_template('index.html')

