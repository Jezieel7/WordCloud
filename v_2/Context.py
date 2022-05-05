import Strategy
import StrategyTxt


class Context:
    strategy: Strategy

    def setStrategy(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = StrategyTxt()

    def executeStrategy(self) -> str:
        print(self.strategy.execute())
