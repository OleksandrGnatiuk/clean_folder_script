from setuptools import setup

setup(name='clean_folder',
      version='1.0.9',
      description='script for cleaning folders',
      url='https://github.com/OleksandrGnatiuk/clean_folder_script',
      author='Oleksandr Gnatiuk',
      author_email='oleksandr.gnatiuk@gmail.com',
      license='MIT',
      packages=['clean_folder'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )