from xml.etree import cElementTree as et

from CellManager.checker import evaluate


def set_displayed(cell, val):
    disp = cell.find('displayedValue')
    if disp is not None:
        cell.remove(disp)
    else:
        disp = et.Element('displayedValue')
    disp.text = str(val)
    cell.append(disp)


def eval_if_need(value, fun):
    if value[0] == "=":
        return evaluate(value[1:], fun)
    return value


class XML:
    tree = None
    xml_root = None

    def __init__(self, file):
        self.tree = et.parse(file)
        self.xml_root = self.tree.getroot()
        assert self.xml_root.tag == 'sheets'

    def eval(self):
        for sheet in self.xml_root:
            for cell in sheet:
                set_displayed(cell,
                              eval_if_need(cell.find('value').text,
                                           self.get_value))

    def get_value(self, let, num):
        cell = self.xml_root.find('.//cell[@col=\'%s\'][@row=\'%s\']' % (let, num))
        val = cell.find('displayedValue')

        if not val:
            return val.text
        val = cell.find('value')

        if val:
            return ''

        val = str(eval_if_need(val.text, self.get_value))
        set_displayed(cell, val)

        return val

    def save(self, file):
        self.tree.write(file, encoding="UTF-8")
