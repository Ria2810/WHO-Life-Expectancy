import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "WHO-Life-Expectancy"
AUTHOR_USER_NAME = "Ria2810"
SRC_REPO = "LifeExoectancyProject"
AUTHOR_EMAIL = "riachoudhari9@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This project utilizes the Global Health Observatory (GHO) data repository from the World Health Organization (WHO) and United Nations data to analyze life expectancy and critical health factors for 193 countries from 2000 to 2015. After merging datasets, missing values, mainly in population, Hepatitis B, and GDP categories, were addressed, with lesser-known countries excluded due to data unavailability. The final dataset comprises 22 columns and 2,938 rows, focusing on 20 predicting variables categorized into Immunization, Mortality, Economic, and Social factors. Through this analysis, the project aims to gain insights into global health trends and their determinants.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)