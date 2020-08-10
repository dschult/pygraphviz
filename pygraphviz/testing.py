
def stringify(agraph):
    result = agraph.string().split()
    if '""' in result:
        result.remove('""')
    some = " ".join(result)
    if '\\N' in some:
        some = some.replace('node [label="\\N"];', '')
        result = some.replace(', label="\\N" ', '').split()
    return " ".join(result)

