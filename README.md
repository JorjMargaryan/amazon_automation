# Amazon Automation Tests

Automated tests for verifying the functionality of the Amazon website. These tests are implemented using Python and Selenium WebDriver.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)

## Introduction

This repository contains automated test cases to validate the functionality of the Amazon website.

## Prerequisites

Make sure you have the following installed:

    - Python 3.x
    - Selenium WebDriver
    - Web browser driver (e.g., ChromeDriver for Google Chrome)
    - `pathlib` - library for working with file paths
    - `os` - library for interacting with the operating system
    - `logging` - library for generating log messages
    - `random` - library for random data generation

## Installation

1.Clone the repository to your local machine:

    git clone [repository_url]

2.Install the required Python packages:

    pip install -r requirements.txt

## Running the Tests

1.Set the path to your web browser driver in the test scripts.

2.Run the tests using a test runner or directly via Python.

    python -m unittest discover tests
