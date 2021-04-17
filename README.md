# Which tax regime to choose ?

## Introduction
Basic python script to calculate income tax and compare old regime and new regime.


## Getting started
* Run the script
    ```bash
    $ python3 choose_tax_regime.py
    ```
* Enter the values when prompted
    ```bash
    $ python3 choose_tax_regime.py
    Income: 6,50,000
    80C savings: 1,50,000
    80CCD(1B) savings: 
    80D savings: 
    Enter age: 25
    Enter parent age: 55
    ```
* Example output
    ```bash
    -----------------------------------------------

    Tax slab: 500000	Amount in the slab: 150000	Tax amount: 15000.0
    Tax slab: 250000	Amount in the slab: 250000	Tax amount: 12500.0
    Cess: 1100.0
    New regime tax amount: 28600.0
    -----------------------------------------------
    Total savings: 200000
    Tax slab: 250000	Amount in the slab: 200000	Tax amount: 10000.0
    Rebate: -10000.0
    Cess: 0.0
    Old regime tax amount: 0.0
    -----------------------------------------------

    Choose Old regime and save Rs. 28600.0

    -----------------------------------------------

    ```


## To-Do

1. Need to add standard reductions
1. Need to add HRA
1. Add proper savings limits based on many conditions


## References
* https://groww.in/blog/old-vs-new-tax-regime-which-is-better/
* 80C - https://cleartax.in/s/80c-80-deductions#Section80C
* 80CCD - https://cleartax.in/s/section-80ccd
* 80D- https://cleartax.in/s/medical-insurance
