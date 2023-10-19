# import setuptools

# with open("README.md", "r") as fh:
# 	long_description = fh.read()

# setuptools.setup(
# 	name ='ft_package',
# 	version ='0.0.1',
# 	summary ='A sample test package',
# 	home_page =' https://github.com/juhyulee/ft_packages' ,
# 	author ='juhyulee' ,
# 	author_email='juhyulee@42.fr',
# 	license= 'MIT' ,
# 	location= '/home/juhyulee/...' ,
# 	requires= ' ',
# 	required_by=' ',
# 	metadata_version='2.1' ,
# 	installer='pip' ,
# 	classifiers=' ',
# 	entry_points=' '

# )

from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
	description='A sample test package',
    author='juhyulee',
    author_email='pismire0317@gmail.com',
    home_page='https://github.com/juhyulee/ft_package',
	license= 'MIT' ,
    packages=find_packages(exclude=[]),
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
)
