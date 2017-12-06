import frappe


@frappe.whitelist()
def get_continent(country):
    if country == 'Vietnam':
        return 'Asia'

    return 'Europe'
