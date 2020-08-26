object Visitor extends App {

  trait HouseElement {
    def accept(visitor: Visitor): Unit
  }

  class House(kitchen: Kitchen) extends HouseElement {
    def accept(visitor: Visitor): Unit = {
      visitor.visit(this)
      kitchen.accept(visitor)
    }
  }

  class Kitchen(fridge: Fridge) extends HouseElement {
    def accept(visitor: Visitor): Unit = {
      visitor.visit(this)
      fridge.accept(visitor)
    }
  }

  class Fridge extends HouseElement {
    def accept(visitor: Visitor): Unit = {
      visitor.visit(this)
    }
  }

  trait Visitor {
    def visit(house: House): Any

    def visit(kitchen: Kitchen): Any

    def visit(fridge: Fridge): Any
  }

  class Friend extends Visitor {
    def visit(house: House): Any = println("House entered")

    def visit(kitchen: Kitchen): Any = println("Kitchen entered")

    def visit(fridge: Fridge): Any = println("Beer taken")
  }

  class Burglar extends Visitor {
    def visit(house: House): Any = println("House entered")

    def visit(kitchen: Kitchen): Any = println("Kitchen entered")

    def visit(fridge: Fridge): Any = println("Fridge taken")
  }

  val house = new House(new Kitchen(new Fridge))
  house.accept(new Friend)
  house.accept(new Burglar)

}
