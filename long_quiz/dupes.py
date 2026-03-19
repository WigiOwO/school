def remove_duplicates(items:list):
    setItems = set(items)
    listItems = list(setItems)
    sortedItems = []
    for i in items:
        for j in listItems:
            if j == i and i not in sortedItems:
                sortedItems.append(j)
    return sortedItems
