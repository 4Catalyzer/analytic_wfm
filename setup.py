from setuptools import setup, find_packages

setup(
   name='analytic_wfm',
   version='0.1',
   author='None',
   url='https://gist.github.com/1178136.git',
   description='peak detection algorithms',
   packages=find_packages(),
   install_requires=['logging', 'numpy', 'matplotlib', 'scipy', 'pdb' ]
)
