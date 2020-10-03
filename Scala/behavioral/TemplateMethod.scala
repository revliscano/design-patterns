package behavioral

object TemplateMethod extends App {

  trait HouseBuildProcessor {

    def constructBasement: Any

    def constructWalls: Any

    def constructRoof: Any

    def construct: Any = {
      constructBasement
      constructWalls
      constructRoof
    }
  }

  class ConcreteHouseBuildProcessor extends HouseBuildProcessor {
    override def constructBasement: Any = println("Construct concrete basement...")

    override def constructWalls: Any = println("Construct concrete walls...")

    override def constructRoof: Any = println("Construct concrete roof...")
  }


  class WoodenHouseBuildProcessor extends HouseBuildProcessor {
    override def constructBasement: Any = println("Construct wooden basement...")

    override def constructWalls: Any = println("Construct wooden walls...")

    override def constructRoof: Any = println("Construct wooden roof...")
  }

  new ConcreteHouseBuildProcessor().construct

  new WoodenHouseBuildProcessor().construct
}
