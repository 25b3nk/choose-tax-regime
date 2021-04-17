"""
Python script to calculate old regime vs new regime tax

Reference:
    * https://groww.in/blog/old-vs-new-tax-regime-which-is-better/

TODO : Need to add standard reductions
TODO : Need to add HRA
TODO : Add proper savings limits based on many conditions
"""

new_tax_regime = {
    1500000: 0.30,
    1250000: 0.25,
    1000000: 0.20,
     750000: 0.15,
     500000: 0.10,
     250000: 0.05
}

old_tax_regime = {
    1000000: 0.30,
     500000: 0.20,
     250000: 0.05
}

savings_limit = {
    '80C': 150000,
    '80CCD': 50000,
    '80D': 25000,
}


def calculate_tax_for_old_regime(income,
                                 savings_80c=0,
                                 savings_80ccd=0,
                                 savings_80d=0,
                                 age=25,
                                 parent_age=55
                                ):
    """Calculate the income tax in old regime

    Args:
        income (int): Total income
        savings_80c (int, optional): 80C savings. Defaults to 0.
        savings_80ccd (int, optional): 80CCD savings. Defaults to 0.
        savings_80d (int, optional): 80D savings. Defaults to 0.
        age (int, optional): Individual's age. Defaults to 25.
        parent_age (int, optional): Parent age. Defaults to 55.

    Returns:
        int: Tax amount for the income provided
    """
    tax_amount = 0
    savings_80c = min(savings_limit['80C'], savings_80c)
    savings_80ccd = min(savings_limit['80CCD'], savings_80c)
    savings_limit_80d = savings_limit['80D'] * (2 if age > 60 else 1)
    savings_limit_80d += savings_limit['80D'] * (2 if parent_age > 60 else 1)
    savings_80d = min(savings_limit_80d, savings_80d)

    total_savings = savings_80c + savings_80ccd + savings_80d
    print("Total savings: {}".format(total_savings))

    deducted_income = income - total_savings
    init_income = deducted_income

    slab_breaks = sorted(old_tax_regime.keys(), reverse=True)

    for upper_tax_slab in slab_breaks:
        if deducted_income > upper_tax_slab:
            curr_tax = old_tax_regime[upper_tax_slab] * (deducted_income - upper_tax_slab)
            tax_amount += curr_tax
            print("Tax slab: {}\tAmount in the slab: {}\tTax amount: {}".format(upper_tax_slab, (deducted_income - upper_tax_slab), curr_tax))
            deducted_income = upper_tax_slab

    if init_income <= 500000:
        rebate = -1 * tax_amount
        print("Rebate: {}".format(rebate))
        tax_amount += rebate

    health_ed_cess = 0.04 * tax_amount  # 4% health and education cess on the tax amount
    print("Cess: {}".format(health_ed_cess))
    tax_amount += health_ed_cess

    return tax_amount


def calculate_tax_for_new_regime(income, **kwargs):
    """Calculate the income tax in new regime

    Args:
        income (int): Total income

    Returns:
        int: Tax amount for the income provided
    """
    tax_amount = 0
    init_income = income

    slab_breaks = sorted(new_tax_regime.keys(), reverse=True)

    for upper_tax_slab in slab_breaks:
        if income > upper_tax_slab:
            curr_tax = new_tax_regime[upper_tax_slab] * (income - upper_tax_slab)
            tax_amount += curr_tax
            print("Tax slab: {}\tAmount in the slab: {}\tTax amount: {}".format(upper_tax_slab, (income - upper_tax_slab), curr_tax))
            income = upper_tax_slab

    if init_income <= 500000:
        rebate = -1 * tax_amount
        print("Rebate: {}".format(rebate))
        tax_amount += rebate

    health_ed_cess = 0.04 * tax_amount  # 4% health and education cess on the tax amount
    print("Cess: {}".format(health_ed_cess))
    tax_amount += health_ed_cess

    return tax_amount


def get_input(message):
    inp = input(message)
    if inp == '':
        return 0
    val = int(inp.replace(',', ''))
    # print("Rs. {}".format(val))
    return val


if __name__ == '__main__':
    income = get_input("Income: ")
    savings_80c = get_input("80C savings: ")
    savings_80ccd = get_input("80CCD(1B) savings: ")
    savings_80d = get_input("80D savings: ")
    age = get_input("Enter age: ")
    parent_age = get_input("Enter parent age: ")
    print("\n-----------------------------------------------\n")

    new_regime_tax = calculate_tax_for_new_regime(income)
    print("New regime tax amount: {}".format(new_regime_tax))

    print("-----------------------------------------------")
    params = {
        'savings_80c': savings_80c,
        'savings_80ccd': savings_80ccd,
        'savings_80d': savings_80d,
        'age': age,
        'parent_age': parent_age
    }
    old_regime_tax = calculate_tax_for_old_regime(income, **params)
    print("Old regime tax amount: {}".format(old_regime_tax))

    print("-----------------------------------------------\n")
    if old_regime_tax < new_regime_tax:
        print("Choose Old regime and save Rs. {}".format(new_regime_tax - old_regime_tax))
    else:
        print("Choose New regime and save Rs. {}".format(old_regime_tax - new_regime_tax))


    print("\n-----------------------------------------------\n")
