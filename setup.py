from setuptools import setup, find_packages

setup(
    name="see_surf",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "see_surf": ["see_surf.py"]
    },
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "see-surf=see_surf:scan"
        ]
    },
    python_requires=">=3.10",
)