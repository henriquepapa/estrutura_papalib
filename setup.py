from setuptools import find_packages, setup

setup(name='papalib',
      version='0.1',
      url='https://github.com/henriquepapa/estrutura_papalib',
      license='MIT',
      author='Henrique Papa',
      author_email='Henrique Papa A. Fonseca',
      description='Função padrão para criação de libs',
      packages=find_packages(include=['papalib']),
      long_description=open('README.md').read(),
      zip_safe=False)
