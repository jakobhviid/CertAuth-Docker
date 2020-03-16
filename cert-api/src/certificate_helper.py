from subprocess import call

SIGNED_CERTIFICATES_PATH = '/signed_certificates'


def sign_certificate(certificate_file_path, certificate_suffix):
    signing_result = call(['openssl', 'x509', '-req', '-CA', '/ssl/ca-cert', '-CAkey', '/ssl/ca-key', '-in',
                           certificate_file_path, '-out',
                           SIGNED_CERTIFICATES_PATH + '/cert-signed' + certificate_suffix,
                           '-days', '365', '-CAcreateserial'])
    # return true if signing went correctly
    return signing_result == 0
