from unittest import TestCase
from unittest.mock import MagicMock

from modules.Covering.StandardCovering.final_standard_covering import FinalStandardCovering
from modules.Crowding.crowding import Crowding
from modules.GCSBase.domain.Rule import Rule
from modules.GCSBase.domain.symbol import Symbol
from modules.GCSBase.domain.types.SymobolType import SymbolType
from modules.GCSBase.grammar.grammar import Grammar
from modules.Visualisation.iteration import Iteration


class TestFinalStandardCovering(TestCase):

    def setUp(self):
        iteration = Iteration()
        self.crowding = Crowding()
        self.crowding.set_iteration(iteration)
        self.covering = FinalStandardCovering(self.crowding)
        self.covering.set_iteration(iteration)
        self.grammar = Grammar()
        self.first_right_symbol = Symbol('a', SymbolType.ST_TERMINAL)
        self.second_right_symbol = Symbol('b', SymbolType.ST_TERMINAL)
        self.left_symbol = Symbol('x', SymbolType.ST_TERMINAL)
        self.rule = Rule([self.left_symbol, self.first_right_symbol, self.second_right_symbol])

    def test_add_new_rule(self):
        self.covering.crowding.add_rule = MagicMock()
        self.grammar.get_start_symbol = MagicMock(return_value=self.left_symbol)

        result = self.covering.add_new_rule(self.grammar, self.first_right_symbol, self.second_right_symbol)

        self.assertEqual(self.rule, result)
        self.covering.crowding.add_rule.assert_called_once_with(self.grammar, self.rule)
        self.grammar.get_start_symbol.assert_called_once_with()
