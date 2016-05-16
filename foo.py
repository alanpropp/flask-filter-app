from helpers import get_schools
#from helpers import filter_by_debt, filter_by_cost, filter_by_earnings, sort_by_criteria


# store the datarows in memory
schools = get_schools()


# this function is the only one that app.py needs to know about
#cost = COSTT4_A, debt = GRAD_DEBT_MDN_SUPP, retention = RET_FT4 (4 year institutions)
#median earnings 10 years out = md_earn_wne_p10
def just_do_it(debt="", cost="", earnings = "", sortby="alpha"):
    matched_rows = []
    datarows = schools
    # first, filter
    if debt:
        filteredrows = filter_by_debt(debt, schools)
    elif cost:
        filteredrows = filter_by_cost(cost, schools)
    else:
        filteredrows = filter_by_earnings(earnings, schools)
    # then, sort and return the result
    # remember to pass in filteredrows
    return sort_by_criteria(sortby, filteredrows)



def print_record_count():
    print("There are", len(schools), 'rows.')