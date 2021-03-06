from games.game import SymmetricNPlayerGame


class HawkDoveBourgeois(SymmetricNPlayerGame):
    """
    A class used to to represent the 2 player hawk-dove-bourgeois game. See U{http://www.life.umd.edu/classroom/zool360/L18-ESS/ess.html}
    """
    DEFAULT_PARAMS = dict(v=30, c=100)
    STRATEGY_LABELS = ('Hawk', 'Dove', 'Bourgeois')
    EQUILIBRIA_LABELS = ('Bourgeois Bourgeois')

    def __init__(self, v, c):
        payoff_matrix = (((v - c) / 2, v, 3 * v / 4 - c / 4),
                         (0, v / 2, v / 4),
                         ((v - c) / 4, 3 * v / 4, v / 2))
        
        super(HawkDoveBourgeois, self).__init__(payoff_matrix, 2)
        
    @classmethod
    def classify(cls, params, state, tolerance):
        threshold = 1 - tolerance
        
        if state[0][2] >= threshold:
            return 0#Bourgeois Bourgeois
        else:
            return super(HawkDoveBourgeois, cls).classify(params, state, tolerance)
