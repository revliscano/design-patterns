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

  class ChessEngine() {
    private val openingStrategy = new OpeningStrategy
    private val computationStrategy = new ComputationStrategy

    private var strategy: Strategy = openingStrategy

    def makeMove: Any = strategy.makeMove

    def evalOpponentsMove: Any = positionInOpeningsBook match {
      case true => strategy = openingStrategy
      case false => strategy = computationStrategy
    }

    def positionInOpeningsBook: Boolean = Random.nextBoolean
  }

  val chessEngine = new ChessEngine

  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove
  chessEngine.makeMove
  chessEngine.evalOpponentsMove

}
