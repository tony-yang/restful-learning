from setuptools import setup

requires = [
    'pyramid'
]

setup(
    name='read',
    install_requires=requires,
    entry_points='''
    [paste.app_factory]
    main = read.main
    '''
)
