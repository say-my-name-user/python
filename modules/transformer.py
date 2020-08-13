class Transformer:
    def __init__(self, data):
        self.data = data

    def prepare_currency_response(self):
        outcome = []

        for item in self.data:
            outcome.append({
                'code': item[0],
                'value': item[1],
                'date': item[2],
            })

        return outcome
