import setuptools

setuptools.setup(
    name="mortgage-calculator",
    version="0.1",
    packages=setuptools.find_packages(include=["mortgage_calculator"]),
    entry_points={
        "console_scripts": [
            "mortgage = mortgage_calculator.main:main",
        ]},
)
