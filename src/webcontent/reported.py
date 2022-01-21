from ..saucier.soup import Soup

def grab_table_item(tag, row_attr, col_attr, row_index=None, col_index=None):
    """Returns a <td> item from a table using a row and column attribute search -
    and index search if multiple rows or columns are found

    Parameters
    ----------
    tag : Tag
        A <table> object
    row_attr : dict
        Attributes for the desired row
    col_attr : dict
        Attributes for the desired column
    row_index : int
        (Optional) Index of desired row - if multiple rows are found
    col_index : int
        (Optional) Index of desired column - if multiple rows are found.

    Returns
    -------
    item: Tag
        <td> item

    """

    def _grab_row(tag, row_attrs, index=None):
        if index:
            return tag.find_all(attrs=row_attrs)[index]
        return tag.find(attrs=row_attrs)

    def _grab_col_in_row(tag, col_attrs, index=None):
        if index:
            return tag.find_all(attrs=col_attrs)[index]
        return tag.find(attrs=col_attrs)

    row = _grab_row(tag, row_attr, row_index)
    item = _grab_col_in_row(row, col_attr, col_index)
    return item

