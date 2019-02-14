[![PyPi](https://img.shields.io/pypi/v/get_a_shell.svg)](https://pypi.org/pypi/get_a_shell/)
![License](https://img.shields.io/github/license/EmilienPer/GetAShell.svg?style=flat)
[![Donate](https://img.shields.io/badge/donate-paypal-orange.svg)](https://www.paypal.me/EmilienPer)
[![Beerpay](https://beerpay.io/EmilienPer/HackRecon/badge.svg?style=flat)](https://beerpay.io/EmilienPer/HackRecon)
## Table of Contents
   * [GetAShell](#getashell)
   * [Requirement](#requirement)
   * [Installation](#installation)
   * [Options](#options)
   * [Usage](#usage)
   * [Example](#example)
   * [Issues management](#issues-management)
  
## GetAShell
Project URL : https://github.com/EmilienPer/GetAShell

GetAShell was created to be used for OSCP certification.
Get a shell code (bind/reverse) into different languages 
## Requirement
GetAShell run on Python 2.7 can't work correctly without the following tools

## Installation
`sudo pip install get-a-shell`

## Options
| Option | Require for bind | Require for reverse | Description |
| ------ | ---------------- | ------------------- | ----------- |
| type | X | X | The type of shell (bind or reverse) |
| language | X | X | The language of shell |
| --lhost | | X | The local host ip adress |
| --lport | | X | The local port|
| --rhost |X  | | The remote host ip adress |
| --rport |X |  | The remote port|
## Usage
* `get_a_shell bind python --rport 10`
* `get_a_shell reverse ruby --lhost 10.10.10.10 --lport 20`

## Issues management 
For contributions or suggestions, please [open an Issue](https://github.com/EmilienPer/GetAShell/issues/new) and clearly explain, using an example or a use case if appropriate. 