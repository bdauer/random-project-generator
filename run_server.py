import os
import binascii

from random_project_app.views import app


if __name__ == '__main__':
    app.debug = True
    app.secret_key = binascii.hexlify(os.urandom(24))
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
