import os
from app import app
from certificate_helper import sign_certificate, SIGNED_CERTIFICATES_PATH

from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import uuid


# Only files without any extensions should be allowed to be uploaded (certification request files does not have an
# extension)
def allowed_file(filename):
    return not ('.' in filename)


@app.route('/sign-certificate', methods=['POST'])
def sign_certificate_route():
    # check if the post request has the expected file, certificate-request
    if 'certificate-request' not in request.files:
        resp = jsonify(
            {'message': 'No \'certificate-request\' file has been provided in the request'})
        resp.status_code = 400
        return resp

    file = request.files['certificate-request']
    if file.filename == '':
        resp = jsonify({'message': 'No certificate selected'})
        resp.status_code = 400
        return resp

    if file and allowed_file(file.filename):
        # secure_filename makes sure that invalid file paths which could compromise the server host are removed.
        # (e.g '../../../../home/username/.bashrc' becomes -> ''home_username_.bashrc' )
        filename = secure_filename(file.filename)
        uuid_suffix = str(uuid.uuid4())
        file.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename + uuid_suffix))

        if not sign_certificate(app.config['UPLOAD_FOLDER'] + '/' + filename + uuid_suffix, uuid_suffix):
            resp = jsonify(
                {'message': 'Something went wrong, signing could not complete, please try agian'})
            resp.status_code = 500
            return resp
        else:
            return send_from_directory(SIGNED_CERTIFICATES_PATH, 'cert-signed' + uuid_suffix)
            # TODO: Delete the files again so they don't take up a lot of space
    else:
        resp = jsonify(
            {'message': 'Only files without extensions are allowed!'})
        resp.status_code = 400
        return resp

@app.route('/get-certificate', methods=['GET'])
def get_certificate_route():
    # TODO: Make sure that not just everyone can get access to this certificate
    return send_from_directory('/ssl', 'ca-cert')


if __name__ == "__main__":
    # Listen on any connections for containerization
    app.run(host='0.0.0.0')
