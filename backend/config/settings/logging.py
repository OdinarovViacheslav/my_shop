LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'main_formatter'
        },
        'console': {'class': 'logging.StreamHandler'}
    },
    'loggers': {
        'core.views.integration': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'production': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
    'formatters': {
        'main_formatter': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'style': '{',
            'datefmt': "%d/%b/%Y" "%H:%M:%S",
        },
        'simple': {'format': '%(levelname)s %(message)s'}
    }
}