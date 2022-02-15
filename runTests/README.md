# [GPM](../README.md) / Run Tests

## Local installation

1. Install PyEnv in any machine where will be used this exercise. Follow this link (Start from "1. Install pyenv" and follow the steps until "Success" section). !!!!WARNING!!!!!: use pyhton 3.8.6 or higher as version to install https://opensource.com/article/19/5/python-3-default-mac
1. Clone the repo
1. Run `pip install -r requirements.txt`
1. Optional - Only for MAC - Add chromedriver as a secure application run: `xattr -d com.apple.quarantine core/assets/webdrivers/chromedriver` (Only for local webdrivers). This step can fail, but it is ok
1. To run the test: in the folder **tests**, run `pytest test_example.py`