import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    print(long_description)
    print('i was here and made changes in a new branch')
    print('my new changes in branch1')
    print('add new print line for try making changes on the remote repository')

setuptools.setup(
    name="metabase-api",
    version="0.3.1",
    author="Vahid Vaezian",
    author_email="vahid.vaezian@gmail.com",
    description="A Python Wrapper for Metabase API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vvaezian/metabase_api_python",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
