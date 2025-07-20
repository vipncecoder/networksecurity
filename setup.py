from setuptools import setup, find_packages
from typing import List
def get_requirements()->List[str]:
    """
    This function returns a list of requirements for the package.
    """
    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #process each line
            for line in lines:

                requirement=line.strip()
                ## ignore empty lines and comments and -e .
                if requirement and requirement!= '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the package directory.")                

    return requirements_lst    

print(get_requirements())

## this is the setup function and it is used to set up the package it will take the name of the package, version, author, description, and requirements from requirements.txt
    
setup(
    name='networksecurityvk',
    version='0.0.1', 
    author='Vikram Kumar',
    author_email='vipnce45@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
    )  