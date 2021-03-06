import os


class JWEAlgorithm(object):
    """Interface for JWE algorithm. JWA specification (RFC7518) SHOULD
    implement the algorithms for JWE with this base implementation.
    """
    TYPE = 'JWE'
    HEADER_KEY = 'alg'

    def __init__(self, name):
        self.name = name

    def prepare_private_key(self, key):
        raise NotImplementedError

    def prepare_public_key(self, key):
        raise NotImplementedError

    def wrap(self, cek, headers, key):
        raise NotImplementedError

    def unwrap(self, ek, headers, key):
        raise NotImplementedError


class JWEEncAlgorithm(object):
    TYPE = 'JWE'
    HEADER_KEY = 'enc'

    IV_SIZE = None
    CEK_SIZE = None

    def generate_cek(self):
        return os.urandom(self.CEK_SIZE // 8)

    def generate_iv(self):
        return os.urandom(self.IV_SIZE // 8)

    def check_iv(self, iv):
        if len(iv) * 8 != self.IV_SIZE:
            raise ValueError('Invalid "iv" size')

    def encrypt(self, msg, aad, iv, key):
        """Encrypt the given "msg" text.

        :param msg: text to be encrypt in bytes
        :param aad: additional authenticated data in bytes
        :param iv: initialization vector in bytes
        :param key: encrypted key in bytes
        :return: (ciphertext, iv, tag)
        """
        raise NotImplementedError

    def decrypt(self, ciphertext, aad, iv, tag, key):
        """Decrypt the given cipher text.

        :param ciphertext: ciphertext in bytes
        :param aad: additional authenticated data in bytes
        :param iv: initialization vector in bytes
        :param tag: authentication tag in bytes
        :param key: encrypted key in bytes
        :return: message
        """
        raise NotImplementedError


class JWEZipAlgorithm(object):
    TYPE = 'JWE'
    HEADER_KEY = 'zip'

    name = None
    description = None

    def compress(self, s):
        raise NotImplementedError

    def decompress(self, s):
        raise NotImplementedError
