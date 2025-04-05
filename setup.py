from setuptools import setup, find_packages

setup(
    name='projinit',
    version='1.0.0',
    author='Srijan',
    author_email='srijanbahal.work@example.com',
    description='🛠️ Generate full project structures from markdown blueprints.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/srijanbahal/Projinit',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'projinit=projinit.main:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
