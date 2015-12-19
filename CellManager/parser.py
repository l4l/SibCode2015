from xml.etree import cElementTree as tree

from CellManager.checker import evaluate


def set_displayed(cell, val):
    disp = tree.Element('displayedValue')
    disp.text = str(val)
    cell.append(disp)


def eval_if_need(value, fun):
    if value[0] == "=":
        return evaluate(value[1:], fun)
    return value


class XML:
    xml_data = None

    def __init__(self, data):
        self.xml_data = tree.fromstring(data)
        assert self.xml_data.tag == 'sheets'

    def eval(self):
        for sheet in self.xml_data:
            for cell in sheet:
                set_displayed(cell,
                              eval_if_need(cell.find('value').text,
                                           self.get_value))

    def get_value(self, let, num):
        cell = self.xml_data.find('.//cell[@col=\'%s\'][@row=\'%s\']' % (let, num))
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
        t = tree.ElementTree()
        t._setroot(self.xml_data)
        t.write(file, encoding="UTF-8")
