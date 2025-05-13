from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    description='A sample test package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='adiri',
    author_email='adiri@student.1337.ma',
    url='https://github.com/ayoubediri/Python-for-Data-Science/tree/main/starting/ex09/ft_package',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
