import Context
import StrategyPdf
import StrategyDoc

appA = Context()
appB = Context()
appC = Context()

## selecting stratigies
appA.setStrategy(StrategyPdf())
appB.setStrategy(StrategyDoc())
appC.setStrategy()    ## sets to default strategy

## each object below execute different strategy with same method
appA.executeStrategy()
appB.executeStrategy()
appC.executeStrategy()