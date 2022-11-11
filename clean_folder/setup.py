from setuptools import setup

setup(name='clean_folder',
      version='1.0.8',
      description='script for cleaning folders',
      url='https://github.com/OleksandrGnatiuk/python_core',
      author='Oleksandr Gnatiuk',
      author_email='oleksandr.gnatiuk@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )