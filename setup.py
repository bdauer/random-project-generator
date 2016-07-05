from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['tests/']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import sys, pytest
        errcode = pytest.main(self.pytest_args)
        sys.exit(errcode)


with open('README.md') as f:
    readme = f.read()


with open('LICENSE') as f:
    license = f.read()


setup(
    name='random_project_app',
    version='0.0.1',
    description='Get a random project!',
    long_description='',
    authors='Ben Dauer',
    url='',
    license='',
    packages=['random_project_app'],
    install_requires=[
        'Flask>=0.11.1'
    ],
     tests_require=[
        'pytest==2.9.2',
        'pytest-cov==2.2.1',
        'coverage==4.0.3',
    ],
    cmdclass={'test': PyTest},
)
