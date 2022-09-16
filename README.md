# NCSU_SE_Fall22_22_hw2_5  
**Migrating csv.lua to Python based library** 


[![GitHub](https://img.shields.io/github/license/agupta15k/ncsu_se_fall22_22_hw2-5?color=green&label=license&logo=MIT)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/blob/main/LICENSE.md)
[![Github](https://img.shields.io/badge/language-python-red.svg)](https://www.python.org/downloads/)
[![GitHub issues](https://img.shields.io/github/issues-raw/agupta15k/ncsu_se_fall22_22_hw2-5)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/issues)
[![Github closed issues](https://img.shields.io/github/issues-closed-raw/agupta15k/ncsu_se_fall22_22_hw2-5)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/issues?q=is%3Aissue+is%3Aclosed)
[![Github pull requests](https://img.shields.io/github/issues-pr/agupta15k/ncsu_se_fall22_22_hw2-5?color=red)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/pulls)
[![Github closed pull requests](https://img.shields.io/github/issues-pr-closed/agupta15k/ncsu_se_fall22_22_hw2-5?color=blue)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/pulls?q=is%3Apr+is%3Aclosed)
[![Github all contributors](https://img.shields.io/github/contributors/agupta15k/ncsu_se_fall22_22_hw2-5?color=green)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/graphs/contributors)
[![Github workflow badge](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/actions/workflows/run-test.yml/badge.svg)](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/actions)

<!-- ## Objective? -->

<!-- Converting a LUA based system into python based library.. -->

- **Built on**

  <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="40" height="40" />

- **Language used:** Python
- **Libraries used:** [re](https://docs.python.org/3/library/re.html), [os](https://docs.python.org/3/library/os.html), [csv](https://docs.python.org/3/library/csv.html), [sys](https://docs.python.org/3/library/sys.html), [math](https://docs.python.org/3/library/math.html)

## Getting started:

  - ### Prerequisite:
    - Download [Python3](https://www.python.org/downloads/).

  - ### Installation:
    
    - Install all the requirements:

      `pip install -r requirements.txt`

  - ### Run Instructions

    - Clone [this (LUA to Python) github repo](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5).

    - Navigate to the project root directory
  
    - Run:
    
      - Test:
      
        - To run all tests, run the command `python -m src.main -e ALL`
        
        - To run a specific test, run the command `python -m src.main -e <test-name>`
        
        - To see a list of test names, run the command `python -m src.main -e LS`
        
        - To see the help section, run the command `python -m src.main -h`
        
        - If any of the tests fail, use `-d` flag to see stack trace
      

## Directory structure

    .
    ├── .github
    │   ├── workflows          
    │   │   ├── run-test.yml            # Workflow for git actions
    ├── Docs
    │   ├── TestFile.md                 # Test file
    ├── data
    |   ├── README.md                   # Readme file for data folder
    |   ├── constants.py                # Contains constants to be used by other code
    |   ├── input.csv                   # Input file used for testing the logic
    ├── src
    │   ├── Num.py                      # Num class to get mid & div
    │   ├── __init__.py                 # Init file for src directory
    |   ├── cols.py                     # Cols class with its methods
    |   ├── data.py                     # Data class to handle data from csv
    │   ├── main.py                     # Main file for src directory
    │   ├── misc.py                     # File for all miscellaneous functions
    |   ├── row.py                      # Rows class with its methods
    │   ├── sym.py                      # Sym class to get mid & div
    ├── tst
    │   ├── README.md                   # Readme file for unit tests
    │   ├── __init__.py                 # Init file for tst directory
    │   ├── testEngine.py               # Contains code for test engine
    │   ├── test_*.py                   # Specific test files
    ├── .all-contributorsrc             # File for all-contributor bot
    ├── .gitattributes                  # File for git attributes
    ├── .gitignore                      # File for git ignore
    ├── CODE_OF_CONDUCT.md              # Code of conduct for repository
    ├── CONTRIBUTING.md                 # Details about contributing to the repository
    ├── LICENSE.md                      # MIT License details
    ├── README.md                       # Readme file for repository
    ├── requirements.txt                # Details of dependency packages
    ├── INSTALL.md                      # Installation steps for complex packages
    └── setup.py                        # Setup file for the module

## Roadmap
  - [List of Roadmap and their corresponding open issues](https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/issues/)

## Contributors ✨

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-5-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/nagarajumadamshetti"><img src="https://avatars.githubusercontent.com/u/42158715?v=4?s=100" width="100px;" alt=""/><br /><sub><b>nagaraj madamshetti</b></sub></a><br /><a href="#infra-nagarajumadamshetti" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=nagarajumadamshetti" title="Tests">⚠️</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=nagarajumadamshetti" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/agupta15k"><img src="https://avatars.githubusercontent.com/u/112216701?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Akash Gupta</b></sub></a><br /><a href="#infra-agupta15k" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=agupta15k" title="Tests">⚠️</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=agupta15k" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Arunsp2000"><img src="https://avatars.githubusercontent.com/u/56639917?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Arunsp2000</b></sub></a><br /><a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=Arunsp2000" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/nitesh31mishra"><img src="https://avatars.githubusercontent.com/u/54522260?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Nitesh Mishra</b></sub></a><br /><a href="#infra-nitesh31mishra" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=nitesh31mishra" title="Tests">⚠️</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=nitesh31mishra" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/sumitsinghhazard"><img src="https://avatars.githubusercontent.com/u/112218156?v=4?s=100" width="100px;" alt=""/><br /><sub><b>sumitsinghhazard</b></sub></a><br /><a href="#infra-sumitsinghhazard" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/agupta15k/ncsu_se_fall22_22_hw2-5/commits?author=sumitsinghhazard" title="Tests">⚠️</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
