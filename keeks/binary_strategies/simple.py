from keeks.binary_strategies.base import BaseStrategy

__author__ = 'willmcginnis'


class NaiveStrategy(BaseStrategy):
    def __init__(self, payoff, loss, transaction_cost):
        """
        The Naive strategy returns full portion of bet if expected value is above transaction costs at all.

        :param payoff:
        :param loss:
        :param transaction_cost:
        """
        self.payoff = payoff
        self.loss = loss
        self.transaction_cost = transaction_cost

    def evaluate(self, probability):
        E = (self.payoff * probability) - (self.loss * (1 - probability)) - self.transaction_cost
        if E > 0:
            return 1.0
        else:
            return 0

