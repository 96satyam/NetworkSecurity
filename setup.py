from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function returns a list of requirements.
    """
    requirement_1st :List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines  = file.readlines()

            for line in lines:
                requirement = line.strip()

                if requirement and requirement!= '-e .':
                    requirement_1st.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_1st

print(get_requirements())

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Satyam Tiwari",
    author_email="satyam.tiwari.9695@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)