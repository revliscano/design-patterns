package structural

import scala.util.Random

object Bridge extends App {

  trait RightBank {
    def explode: Any
  }

  abstract class LeftBank(var rightBank: RightBank) {
    def reactToMilitaryConflict: Any = rightBank.explode
  }

  class RightBankWhenWar extends RightBank {
    def explode: Any = println("Triggering explosion of the Bridge")
  }

  class RightBankWhenPeace extends RightBank {
    def explode: Any = println("There is no real military conflict. No explosion during security training.")
  }

  class LeftBankInWarAndPeace(rightBank: RightBank) extends LeftBank(rightBank) {
    override def reactToMilitaryConflict: Any = {
      println("take own military resources to the left bank")
      super.reactToMilitaryConflict
    }
  }

  val rightBankWhenWar = new RightBankWhenWar
  val rightBankWhenPeace = new RightBankWhenPeace
  val leftBank = new LeftBankInWarAndPeace(rightBankWhenPeace)

  val isThereWar = () => Random.nextBoolean()

  if (isThereWar()) {
    leftBank.rightBank = rightBankWhenWar
  }

  leftBank.reactToMilitaryConflict

}
