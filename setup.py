from setuptools import setup, find_packages

setup(
    name='django-db-cascade',
    version='0.1',
    description='optional db level cascade delete of foreign keys',
    url='http://github.com/nickstefan/django-db-cascade',
    author='Nick Stefan',
    author_email='nickstefan12@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django >= 1.8',
        'psycopg2 >= 2.5'
    ],
    zip_safe=False
)
