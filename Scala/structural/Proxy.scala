package structural

object Proxy extends App {

  trait BrakingSystem {
    def brake: Any
  }

  class HydraulicBrake extends BrakingSystem {
    def brake: Any = println("mechanical braking")
  }

  class BrakeByWireSystem(val brakingSystem: BrakingSystem) extends BrakingSystem {
    def brake: Any = {
      println("activating brake by wire")
      brakingSystem.brake
    }
  }

  class Driver(val brakingSystem: BrakingSystem) {
    def pressBrakePedal: Any = brakingSystem.brake
  }

  val driver = new Driver(new BrakeByWireSystem(new HydraulicBrake))

  driver.pressBrakePedal
}
