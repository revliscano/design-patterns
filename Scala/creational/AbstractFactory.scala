import java.util.Calendar

object AbstractFactory extends App {

  trait Fridge

  class FridgeWithBeer extends Fridge

  class FridgeWithoutBeer extends Fridge

  trait FridgeFactory {
    def createFridge: Fridge
  }

  class NiceFridgeFactory extends FridgeFactory {
    def createFridge: Fridge = new FridgeWithBeer
  }

  class PoorFridgeFactory extends FridgeFactory {
    def createFridge: Fridge = new FridgeWithoutBeer
  }

  def createFridgeFactory: FridgeFactory =
    Calendar.getInstance.get(Calendar.DAY_OF_WEEK) match {
      case Calendar.FRIDAY => new NiceFridgeFactory
      case _ => new PoorFridgeFactory
    }

  val fridgeFactory: FridgeFactory = createFridgeFactory
  val fridge: Fridge = fridgeFactory.createFridge

  println(s"I created ${fridge.getClass.getSimpleName}")
}
