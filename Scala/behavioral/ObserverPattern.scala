package behavioral

import scala.collection.mutable.ListBuffer

object ObserverPattern extends App {

  trait Policeman {

    def checkSpeed(speed: Int): Any = {
      if (speed > 140) {
        policemanStatement(speed)
      }
    }

    def policemanStatement(speed: Int): Any

  }

  class GoodCop extends Policeman {
    override def policemanStatement(speed: Int): Any = println(s"${speed} kmh is too fast man, but I am a nice guy.")
  }

  class BadCop extends Policeman {
    override def policemanStatement(speed: Int): Any = println(s"${speed} kmh... pay ${speed * 5}€")
  }
  
  class Car(var observers: ListBuffer[Policeman], var speed: Int) {
    def registerObserver(policeman: Policeman): Unit = observers += policeman

    def unregisterObserver(policeman: Policeman): Unit = observers -= policeman

    def notifyObservers(): Unit = observers.foreach(observer => observer.checkSpeed(speed))

    def setSpeed(speed: Int): Unit = {
      this.speed = speed
      notifyObservers()
    }
  }

  val car = new Car(ListBuffer.empty, 0)
  val goodCop = new GoodCop
  val badCop = new BadCop
  car.registerObserver(goodCop)
  car.registerObserver(badCop)
  car.setSpeed(20)
  car.setSpeed(40)
  car.setSpeed(80)
  car.setSpeed(100)
  car.setSpeed(140)
  car.setSpeed(160)
  car.setSpeed(180)
  car.setSpeed(200)
  car.unregisterObserver(goodCop)
  car.setSpeed(210)
  car.unregisterObserver(badCop)
  car.setSpeed(240)
  car.registerObserver(badCop)
  car.setSpeed(260)
  car.registerObserver(goodCop)
  car.setSpeed(280)

}
