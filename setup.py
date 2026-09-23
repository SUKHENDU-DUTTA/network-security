'''
    This is the setup file for the project. 
    It contains the metadata and configuration for packaging and distributing the project.
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    
    Returns:
        List[str]: A list of package dependencies.
    """
    requirement_lst:List[str] = []
    try:
        with open('requirements.txt') as file:
            # Read the lines from the requirements.txt file
            lines = file.readlines()
            #Process each line to extract the package names and versions
            for line in lines:
                requirement = line.strip()
                #Ignore empty lines and -e .
                if requirement and not requirement.startswith('-e .'):
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Sukhendu Dutta',
    author_email='sukhendudutta2003@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)