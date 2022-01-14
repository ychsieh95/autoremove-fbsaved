# Facebook Auto-Removed

A CLI tool for removing saved items in Facebook.

## Requirpments

1. Python 3.6+
2. WebDriver (can modifiy the privoder by yourself, e.g. Google Chrome, Microsoft Edge, Mozilla Firefox)

## Usage

0. Install package `selenium`:

   ```bash
   $ pip3 install selenium
   ```

1. Download the [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) from official.
   At this step, make sure the WebDriver version you install matches your browser version. You can follow the steps provided by [Download Microsoft Edge Driver](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=c-sharp#download-microsoft-edge-driver) to do it correctly.

   If you want to use other WebDrivers, just download the executable and modify the name of WebDriver in the code:

   ```python
   ...
   # Default, for Microsoft Edge
   self.driver = webdriver.Edge()

   # For Google Chrome
   self.driver = webdriver.Chrome()

   # For Mozilla Firefox
   self.driver = webdriver.Firefox()
   ...
   ```

2. Put the WebDriver executable in the directory. The directory architecture should be:

   ```text
   .
   |-- Driver_Notes
   |   |-- EULA
   |   |-- LICENSE
   |   `-- credits.html
   |-- README.md
   |-- main.py
   `-- msedgedriver.exe
   ```

3. Run the python script:

   ```bash
   $ python main.py --help
   usage: main.py [-h] -u USERNAME -p PASSWORD [-o OPTION]

   A CLI tool for removing saved items in Facebook.

   optional arguments:
   -h, --help            show this help message and exit
   -u USERNAME, --username USERNAME
                           facebook username
   -p PASSWORD, --password PASSWORD
                           facebook password
   -o OPTION, --option OPTION
                           options of remove: all, links, videos, photos, places, products, events, offers, unlisted_only, seen, archive
   ```

   For example, if you want to remove all saved items:

   ```bash
   $ python main.py --username=<Facebook_Username> --password=<Facebook_Password>
   ```

   Or you want to remove all `videos` saved items:

   ```bash
   $ python main.py --username=<Facebook_Username> --password=<Facebook_Password> --option=videos
   ```