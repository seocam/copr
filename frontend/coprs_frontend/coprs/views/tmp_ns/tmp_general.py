import flask
import os
from coprs.views.tmp_ns import tmp_ns
from coprs import app

@tmp_ns.route("/<directory>/<file>")
def give_srpm(directory, file):
    path = os.path.join(app.config["SRPM_STORAGE_DIR"], directory)
    return flask.send_from_directory(path, file)
