inventory_dictionary = {}
def add_inventory(dictionary, widget_name, quantity):
    if dictionary == "inventory_dictionary":
        if widget_name in inventory_dictionary:
            quantity2 = 0
            quantity2 = int(inventory_dictionary.get(widget_name))
            quantity2 += quantity
            inventory_dictionary.update({widget_name: quantity2})
        
def remove_inventory_widget(dictionary, widget_name):
    if dictionary == "inventory_dictionary":
        if widget_name in inventory_dictionary:
            inventory_dictionary.pop(widget_name)
            return 'Record deleted'
    else:
        return 'Item not found'