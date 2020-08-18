package structural

object AdapterPattern extends App {

  class EuropeanPlug {
    def connect: Any = println("European Plug Connected")
  }

  class AmericanPlug {
    def connect: Any = println("American Plug Connected")
  }

  class AmericanPlugAdapter(europeanPlug: EuropeanPlug) extends AmericanPlug {
    override def connect: Any = europeanPlug.connect;
  }

  class AmericanSocket {
    def connect(plug: AmericanPlug): Unit = plug.connect
  }

  val americanSocket = new AmericanSocket

  val americanPlug = new AmericanPlug
  val europeanPlug = new EuropeanPlug

  americanSocket.connect(americanPlug)
  americanSocket.connect(new AmericanPlugAdapter(europeanPlug))

}
