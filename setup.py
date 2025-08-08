from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains the code in the ./src directory of the project",
    author="Manoj Sahoo",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"],
    entry_points={
        "packages":[
            "main=dab_project.main:main"
        ]
    }
)
