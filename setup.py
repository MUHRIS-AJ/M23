from setuptools import setup, find_packages

setup(
    name='m23',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'm23=m23:main',  # calls main() from m23/__init__.py
        ],
    },
    author='MUHRIS_A.J',
    Email='abooljayahmuhris@gmail.com',
    description='M23: Human-friendly Data Science Language',
    url='https://github.com/MUHRIS-AJ/M23.git',
    license='MIT',
)
