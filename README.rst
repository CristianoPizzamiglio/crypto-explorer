Introduction
------------

A simple script that leverages the pycoingecko_ library to write crypto-related data to an Excel file of the top 100 coins.

Data written to the Excel file are:

* Id
* Symbol
* Name
* Current Price
* Market Cap
* Market Cap Rank
* Fully Diluted Valuation
* Total Volume
* High 24H
* Low 24H
* Price Change 24H
* Price Change Percentage 24H
* Market Cap Change 24H
* Market Cap Change Percentage 24H
* Circulating Supply
* Total Supply
* Max Supply
* Ath
* Ath Change Percentage
* Ath Date
* Atl
* Atl Change Percentage
* Atl Date
* Last Updated


.. _pycoingecko: https://github.com/man-c/pycoingecko



Example Usage
-------------

From the command line, just type:

>>> python crypto_explorer.py

and the Excel file will be written in the working directory. The format of the file name is yyyy_mm_dd_hh_mm_ss.


Acknowledgment
--------------
This script uses the pycoingecko_ and pandas_ libraries.

.. _pycoingecko: https://github.com/man-c/pycoingecko
.. _pandas: https://pandas.pydata.org/