class PrincipalUser:

    session = None

    @classmethod
    def setSession(cls, principal):
        cls.session = principal

    @classmethod
    def clearSession(cls):
        cls.session = None