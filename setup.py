from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requirements
    '''
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="e2e_ml",
    version="0.0.1",
    author="Kalyanbrata Maity",
    author_email="maitykalyanbrata94@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements('requirements.txt')
)