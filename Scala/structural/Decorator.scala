package structural

object Decorator extends App {

  trait Bike {
    def absorbShock: Any
  }

  class FrontSuspensionBike extends Bike {
    def absorbShock: Any = println("absorbing shock in the front")
  }

  class FullSuspensionBike extends Bike {
    private val bike = new FrontSuspensionBike

    def absorbShock: Any = {
      bike.absorbShock
      println("absorbing shock in the rear")
    }
  }

  val bike = new FullSuspensionBike
  bike.absorbShock
}
