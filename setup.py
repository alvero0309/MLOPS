from setuptools import setup,find_packages
from typing import List


HYPHEN_E_DOT = '-e .'

def getRequirements(file_requirements:str)->List[str]:

    list_requirements = []
    with open(file_requirements) as file_obj:
        list_requirements = file_obj.readlines()
        list_requirements = [req.replace("\n","")for req in list_requirements]
        print(list_requirements)

        if HYPHEN_E_DOT in list_requirements:
            list_requirements.remove(HYPHEN_E_DOT)
    
    return list_requirements

setup(

    name="MLOPS",
    version='0.0.1',
    author='Alejandro Vega',
    author_email='avega@gmail.com',
    packages=find_packages(),
    install_requires = getRequirements('requirements.txt')
)