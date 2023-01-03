from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.0.9',
      description='script for cleaning folders',
      url='https://github.com/OleksandrGnatiuk/clean_folder_script',
      author='Oleksandr Gnatiuk',
      author_email='oleksandr.gnatiuk@gmail.com',
      include_package_data=True,
      license='MIT',
      packages=find_namespace_packages()
      install_requires=['markdown'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )