from setuptools import setup

setup(
    name='curethinkdb',
    version='0.0.1',
    keywords='curio rethinkdb async driver',
    description='Curio + RethinkDB: Async RethinkDB driver',
    long_description=__doc__,
    author='guyskk',
    author_email='guyskk@qq.com',
    url='https://github.com/guyskk/curethinkdb',
    license='MIT',
    packages=['curethinkdb'],
    install_requires=[
        'rethinkdb',
        'curio',
    ],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
