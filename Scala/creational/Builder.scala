package creational

import scala.collection.mutable.ArrayBuffer

object Builder extends App {

  class Wall(val length: Integer, val height: Integer)

  class Door(val length: Integer, val height: Integer, val woodType: String)

  class Window(val length: Integer, val height: Integer, val woodType: String, val glassType: String)

  class Roof

  class SwimmingPool

  abstract class House(
                        val walls: Seq[Wall],
                        val doors: Seq[Door],
                        val windows: Seq[Window],
                        val roof: Roof,
                        val swimmingPool: Option[SwimmingPool])

  class LuxuryHouse(
                     override val walls: Seq[Wall],
                     override val doors: Seq[Door],
                     override val windows: Seq[Window],
                     override val roof: Roof,
                     override val swimmingPool: Option[SwimmingPool]) extends House(walls, doors, windows, roof, swimmingPool)

  class BudgetHouse(
                     override val walls: Seq[Wall],
                     override val doors: Seq[Door],
                     override val windows: Seq[Window],
                     override val roof: Roof) extends House(walls, doors, windows, roof, None)


  abstract class HouseBuilder {

    protected var walls: ArrayBuffer[Wall] = ArrayBuffer()
    protected var doors: ArrayBuffer[Door] = ArrayBuffer()
    protected var windows: ArrayBuffer[Window] = ArrayBuffer()

    def buildWall(length: Integer, height: Integer): Any = walls += new Wall(length, height)

    def installDoor(length: Integer, height: Integer, woodType: String): Any = doors += new Door(length, height, woodType)

    def installWindow(length: Integer, height: Integer, woodType: String, glassType: String): Any = windows += new Window(length, height, woodType, glassType)

    def getResult: House
  }

  class BudgetHouseBuilder extends HouseBuilder {
    override def getResult: House = new BudgetHouse(walls.toSeq, doors.toSeq, windows.toSeq, new Roof)
  }

  class LuxuryHouseBuilder extends HouseBuilder {
    override def getResult: House = new LuxuryHouse(walls.toSeq, doors.toSeq, windows.toSeq, new Roof, Some(new SwimmingPool))
  }

  class ConstructionDirector(val houseBuilder: HouseBuilder) {
    def construct(): Any = {
      houseBuilder.buildWall(10, 10)
      houseBuilder.buildWall(10, 10)
      houseBuilder.buildWall(10, 10)
      houseBuilder.buildWall(10, 10)
      houseBuilder.installDoor(2, 2, "oak")
      houseBuilder.installWindow(1, 1, "oak", "laminated")
      houseBuilder.installWindow(1, 1, "oak", "laminated")
      houseBuilder.installWindow(1, 1, "oak", "laminated")
      houseBuilder.installWindow(1, 1, "oak", "laminated")
    }
  }

  val houseBuilder = new LuxuryHouseBuilder
  val director = new ConstructionDirector(houseBuilder)
  director.construct()
  val house = houseBuilder.getResult
}
