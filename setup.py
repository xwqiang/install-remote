from setuptools import setup, find_packages

setup(
    name="command tools",
    version="1.0",
    keywords=("command", "tools"),
    description="test",
    long_description="test",
    license="MIT Licence",

    url="https://xxx.com",
    author="haah",
    author_email="no",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests"],

    scripts=[],
    # 如果出现 ModuleNotFoundError: No module named,用 py_modules
    py_modules=[],
    entry_points={
        'console_scripts': [
            'ci = command.echo:command_echo'
        ]
    }
)
