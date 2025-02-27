'''
The Setup.py file is an essential part of packaging and distributing Python Projects. It is used by setuptools to define
the configuration of the project, such as metadata, dependencies, and more.
'''

from setuptools import setup, find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    '''
    This function will  return list of requirements

    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            # Read Lines from the file
            lines=file.readlines()
            ## Process Each Line
            for line in lines:
                requirement = line.strip()
                # Ignore empty Lines and ignore -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0,0,1",
    author="Abhinandan Nahar",
    author_email="abhinandannahar378@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)



    