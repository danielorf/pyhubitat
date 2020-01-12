from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pyhubitat',
      version='0.0.1',
      description='A python library for interacting with the Hubitat API',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/danielorf/pyhubitat',
      author='Daniel Orf',
      author_email='danielorf@gmail.com',
      license='GNU GPLv3',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
      ],
      keywords='hubitat home automation',
      install_requires=['httpx'],
      python_requires='>=3.6')
