from setuptools import setup, find_packages

setup(
    name='django-ticker',
    version='0.2.1',
    description='A simple Django app for newsticker with a row level permission based workflow.',
    long_description=open('README').read(),
    author='Martin Mahner',
    author_email='martin@mahner.org',
    maintainer='Jannis Leidel',
    maintainer_email='jannis@leidel.info',
    url='http://github.com/jezdez/django-ticker/tree/master',
    packages=find_packages(exclude=['example_project', 'example_project.*']),
    package_data = {
        'ticker': [
            'templates/ticker/*.html'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)
