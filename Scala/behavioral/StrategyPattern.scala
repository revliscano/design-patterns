package behavioral

import scala.util.Random

object StrategyPattern extends App {

  trait Strategy {
    def makeMove: Any
  }

  class OpeningStrategy extends Strategy {
    override def makeMove: Any = println("selecting move based on chess opening theory book")
  }

  class ComputationStrategy extends Strategy {
    override def makeMove: Any = println("selecting move based on computation")
  }

  class ChessEngine(var strategy: Strategy) {
    def makeMove: Any = strategy.makeMove
  }

  class GameControlModule {

    private val openingStrategy = new OpeningStrategy
    private val computationStrategy = new ComputationStrategy
    private val chessEngine = new ChessEngine(computationStrategy)

    def positionInOpeningsBook: Boolean = Random.nextBoolean

    def evalOpponentsMove: Any = positionInOpeningsBook match {
      case true => chessEngine.strategy = openingStrategy
      case false => chessEngine.strategy = computationStrategy
    }

    def makeMove: Any = chessEngine.makeMove
  }

  val computerPlayer = new GameControlModule
  computerPlayer.evalOpponentsMove
  computerPlayer.makeMove
  computerPlayer.evalOpponentsMove
  computerPlayer.makeMove
  computerPlayer.evalOpponentsMove
  computerPlayer.makeMove
  computerPlayer.evalOpponentsMove
  computerPlayer.makeMove
  computerPlayer.evalOpponentsMove
  computerPlayer.makeMove
  computerPlayer.evalOpponentsMove
  computerPlayer.makeMove
  computerPlayer.evalOpponentsMove

}
