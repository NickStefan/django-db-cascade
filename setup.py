from setuptools import setup, find_packages

setup(
    name='django-db-cascade',
    version='0.1.3',
    description='Optionally use postgres db ON CASCADE DELETE on django foreign keys',
    url='http://github.com/nickstefan/django-db-cascade',
    author='Nick Stefan',
    author_email='nickstefan12@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django >= 1.8',
        'psycopg2 >= 2.5'
    ],
    classifiers=[
        'Framework :: Django',
        'Topic :: Database',
    ],
    zip_safe=False
)
