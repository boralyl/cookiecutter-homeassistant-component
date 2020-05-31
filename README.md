# cookiecutter-homeassistant-component

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for generating
a new [homeassistant](https://www.home-assistant.io/) custom component.

## Features

- Generates the appropriate file structure for a minimal homeassistant custom component.
- Generates metadata to allow submission to [HACS](https://hacs.xyz/).
- Contains everything needed to get started with writing unit tests for your custom component.

## Installation

To get started you will need to install [cookiecutter](https://github.com/cookiecutter/cookiecutter).

```bash
$ pip install cookiecutter
```

Then generate your custom component:

```bash
$ cookiecutter https://github.com/boralyl/cookiecutter-homeassistant-component
```

## Context Options

You will be asked to provide the following values to configure your component:

| Field       | Default                               | Description                                                                                                                                                                                  |
| ----------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| domain      | my_component                          | The domain name of your custom component.                                                                                                                                                    |
| name        | My Component                          | The human readable name of your component.                                                                                                                                                   |
| docs_url    | https://github.com/user/my_component/ | The URL pointing to documentation for your component.                                                                                                                                        |
| owner       | @user                                 | Your github username prefixed with `@`.                                                                                                                                                      |
| config_flow | yes                                   | Signifies if your component will support configuring via the UI via [config flow](https://developers.home-assistant.io/docs/config_entries_config_flow_handler).                             |
| iot_class   | Assumed State                         | The Internet of Things classification for your component. Read more in the [Home Assistant documentation](https://www.home-assistant.io/blog/2016/02/12/classifying-the-internet-of-things). |

## Testing

After generating your project you can install the test requirements using pip:

```bash
$ pip install -r requirements.test.txt
```

Once the test requirements are installed you can run the test suite. A simple
working test is provided out of the box.

```bash
$ pytest
Test session starts (platform: linux, Python 3.7.5, pytest 5.4.2, pytest-sugar 0.9.3)
rootdir: /home/aaron/projects/my-component, inifile: setup.cfg, testpaths: tests
plugins: aiohttp-0.3.0, requests-mock-1.8.0, timeout-1.3.4, sugar-0.9.3, cov-2.8.1, homeassistant-0.1.0
collecting ...
 tests/test_init.py ✓                                                                                                                                                          100% ██████████

----------- coverage: platform linux, python 3.7.5-final-0 -----------
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
custom_components/__init__.py                    0      0   100%
custom_components/my_component/__init__.py       3      0   100%
custom_components/my_component/const.py          1      0   100%
--------------------------------------------------------------------------
TOTAL                                            4      0   100%


Results (0.07s):
       1 passed

```
