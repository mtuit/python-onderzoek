from .abs_cust import AbsCust


class ENTCust(AbsCust):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def send_invoice(self):
        print('Sending invoice to enterprise customer {}.'.format(self._name))
