# Recover Data from .git Directory w/o Git Installation

## Prerequisites

* gin
  ```bash
  python3 -m pip install --user gin
  ```
* advance-touch
  ```bash
  python3 -m pip install --user advance-touch
  ```
* pre-compiled [zpipe](https://github.com/madler/zlib/blob/master/examples/zpipe.c) program
  ```bash
  # after downloading the zpipe.c file, run command below
  
  gcc -o zpipe zpipe.c -lz
  ```
  
## Usage

* Do check the privileges before
* Download the `main.py`, then place `zpipe` program in the same directory
* Run `python3 main.py GIT_DIR DST_DIR`
  * `GIT_DIR` is the `.git` you want to recover
  * `DST_DIR` is the directory to store files generated

  
  
  

