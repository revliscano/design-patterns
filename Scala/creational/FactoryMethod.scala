package creational

object FactoryMethod extends App {

  trait CarbonatedDrink

  class CocaCola extends CarbonatedDrink

  class Fanta extends CarbonatedDrink

  class Sprite extends CarbonatedDrink

  trait CarbonatedDrinkFactory {
    def createDrink: CarbonatedDrink
  }

  class CocaColaFactory extends CarbonatedDrinkFactory {
    def createDrink: CarbonatedDrink = new CocaCola
  }

  class FantaFactory extends CarbonatedDrinkFactory {
    def createDrink: CarbonatedDrink = new CocaCola
  }

  class SpriteFactory extends CarbonatedDrinkFactory {
    def createDrink: CarbonatedDrink = new CocaCola
  }

  class BottledDrink(val carbonatedDrink: CarbonatedDrink)

  val factories = Seq(new CocaColaFactory, new FantaFactory, new SpriteFactory)

  val producedDrinks = (for (_ <- 1 to 100) yield factories.map(_.createDrink).map(new BottledDrink(_))).flatten
}
