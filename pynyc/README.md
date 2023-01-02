[![Documentation Status](https://readthedocs.org/projects/pynyc/badge/?version=latest)](https://pynyc.readthedocs.io/en/latest/?badge=latest) [![Python package](https://github.com/amstelchen/pynyc/actions/workflows/python-package-no-pytest.yml/badge.svg)](https://github.com/amstelchen/pynyc/actions/workflows/python-package-no-pytest.yml)

<h1>PyNYC</h1>

#### A New Years's Clock

TODO

#### What is it *not*?

TODO

#### Usage

```
usage: PyNYC [-h] [-fg FG] [-bg BG] [-v]

A New Years's Clock

options:
  -h, --help     show this help message and exit
  -fg FG         foreground (text) color
  -bg BG         background (wall) color
  -v, --version  show program's version number and exit
```

#### Installation

Steps assume that `python` (>= 3.8) and `pip` are already installed.

Install dependencies (see sections below)

Then, run:

    $ pip install pynyc

Install directly from ``github``:


    $ pip install git+https://github.com/amstelchen/pynyc#egg=GameInfo

When completed, run it with:

    $ pynyc

#### Configuration

The package contains a sample configuration, `pynyc.conf.sample` which can be copied to `~/.config/pynyc.conf`. It will then be read to use its settings instead of *pynyc*'s built-in.

```
fg = white
bg = black
fontface = Courier
fontsize = 50
screensaver = 1
alarm = 60, 15, 1
```

#### Dependencies

On Debian-based distributions (Mint, Ubuntu, MX, etc.), installation of the packages `tk` and `python3-tk` may be necessary.

    $ sudo apt install python3-tk tk

On Arch based distributions, only tk needs to be installed.

    $ sudo pacman -S tk

On Void Linux, installation of the package `python3-tkinter`is necessary instead.

    $ sudo xbps-install python3-tkinter

Anyways, it often helps to keep your python installation updated:

    $ python -m pip install --upgrade pip wheel setuptools

#### System requirements

*pynyc* is tested to work on the following distributions:

TODO

#### Reporting bugs

If you encounter any bugs or incompatibilities, __please report them [here](https://github.com/amstelchen/pynyc/issues/new)__.


#### Enabling logging/debugging

```
$ pynyc --verbose
2022-06-09 01:42:43.612974 DEBUG: ... 1.0.12

```

#### Licences

*pynyc* is licensed under the [GPLv2](LICENSE) license.
