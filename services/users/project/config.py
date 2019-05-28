# services/users/project/config.py


class BaseConfig:
    '''
    Base Configuration
    '''
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    '''
    Development Configuration
    '''
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    '''
    Testing Configuration
    '''
    TESTING = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    '''
    Production Configuration
    '''
    pass
