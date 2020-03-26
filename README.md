# Product Name
> Macro helping CNU Enrolment

This python program helps you to enrol subjects you want to learn in CNU, especially when you have failed the 1st enrolment.

The program automatically finds the cordinate of Macro-Protection-Popup(MPP) in your screen.
Then it copies the 4 numbers on MPP, pastes to insert textbox.
After, it presses Enter to submit the 4-number-code on MPP.
This process will be repeated untill the enrolment succeeds.

![Macro-Protection-Popup](MacroProtectionPopup.PNG)

## Installation

Python 3 Required(Test Environment: Windows10, Python 3.7.0, Chrome)

Windows:

```sh
pip install Pillow
pip install pytesseract
pip install pyperclip
pip install pyautogui
pip install opencv-python
pip install numpy
pip install python3_xlib
```
**If python3 is installed at pip3, try changing ``pip install`` to ``pip3 install`` just as below**

```sh
pip3 install Pillow
pip3 install pytesseract
pip3 install pyperclip
pip3 install pyautogui
pip3 install opencv-python
pip3 install numpy
pip3 install python3_xlib
```

## Instructions

### 1. Modify Variables

Modify variables in CNU_Macro.py following the comments in file.

### 2. Run CNU_Macro.py

Change Chrome as **Foreground Process** after running ``CNU_Macro.py``.

### 3. THINGS TO KNOW

- **All the results and its responsibility comming from using this program owns to the USER.**

- The Accuracy improves when there is no underline below 4-number-code on MPP in ``capture.png``.
  - You can make it by modifying these variables:  ``width``, ``height``, constant area of ``numCodeX``, ``numCodeY``

- capture.png is generated after running ``CNU_Macro.py``.

## Usage example

![test-example](test-macro.gif)

_For more examples and usage, please refer to the [Wiki](https://github.com/hy38/CNU-Enrolment-Macro/wiki)._

## Release History

* 0.0.1
    * First Edition with hardcoded cordinates.

## Meta

SangHyun Park – [@hy387](https://facebook.com/hy387) – sanghyun12101@gmail.com

Distributed under the **GNU General Public License v3.0 license.** See ``LICENSE`` for more information.

[https://github.com/hy38/CNU-Enrolment-Macro/blob/master/LICENSE](https://github.com/hy38/CNU-Enrolment-Macro/blob/master/LICENSE)

## Contributing

1. Fork it (<https://github.com/hy38/CNU-Enrolment-Macro/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
