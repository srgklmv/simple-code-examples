class Category:

    def __init__(self, category):
        self.name = category
        self.ledger = []

    def __str__(self):
        printed_data = [self.name.center(30, "*")]

        for entry in self.ledger:
            description = entry["description"]
            if len(description) > 23:
                description = description[:23]
            amount = float(entry["amount"])
            printed_data.append(description.ljust(23) +
                                "{:.2f}".format(amount).rjust(7))
        total = sum(map(lambda e: e["amount"], self.ledger))
        printed_data.append(f"Total: {'{:.2f}'.format(total)}")
        return "\n".join(printed_data)

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return round(sum(map(lambda e: e["amount"], self.ledger)), 2)

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,
                                "description": f"Transfer to {destination.name}"})
            destination.ledger.append({"amount": amount,
                                       "description": f"Transfer from {self.name}"})
            return True
        else:
            return False

    def check_funds(self, amount):
        return self.get_balance() - amount >= 0


def percent_to_o(total, local):

    number = local * 100 / total

    return int(number / 10) + 1


def create_spend_chart(categories):

    data = ["Percentage spent by category"]

    for i in range(100, -1, -10):
        data.append(f"{i}|".rjust(4) + "   " * len(categories) + " ")
    data.append("    -" + "---" * len(categories))
    for _ in range(max(map(lambda c: len(c.name), categories))):
        data.append("     " + "   " * len(categories))

    total_withdrawals = 0
    for i in range(len(categories)):
        withdrawals = sum([item["amount"] if item["amount"] < 0
                           else 0 for item in categories[i].ledger])
        total_withdrawals += withdrawals

    for i in range(len(categories)):
        local_withdrawals = sum([item["amount"] if item["amount"] < 0 else 0 for item in categories[i].ledger])

        for j in range(percent_to_o(total_withdrawals, local_withdrawals)):
            data[11 - j] = data[11 - j][:5 + 3 * i] + "o" + data[10 - j][6 + 3 * i:]
        for c in range(len(categories[i].name)):
            data[13 + c] = data[13 + c][:5 + 3 * i] + categories[i].name[c] + data[13 + c][6 + 3 * i:]

    printed_data = "\n".join(data)
    return printed_data
