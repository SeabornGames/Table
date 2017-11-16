from setuptools import setup

setup(
    name='seaborn_table',
    version='1.0.0',
    description='SeabornTable reads and writes tables in '
                'csv and md and acts like a list and dict."',
    long_description='',
    author='Ben Christenson',
    author_email='Python@BenChristenson.com',
    url='',
    install_requires=[],
    extras_require={
        'test': ['test-chain'],
    },
    py_modules=['seaborn.seaborn_table'],
    license='MIT License',
    classifiers=(
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5')
)
