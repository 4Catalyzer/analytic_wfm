from setuptools import setup, find_packages

setup(
   name='analytic_wfm',
   version='0.4',
   author='None',
   url='https://gist.github.com/1178136.git',
   description='peak detection algorithms',
   packages=find_packages(),
   install_requires=['numpy', 'scipy'],
   tests_require=['matplotlib'],
)
