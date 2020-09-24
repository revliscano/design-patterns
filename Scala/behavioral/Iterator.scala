package behavioral

object Iterator extends App {

  val iterator = scala.Iterator(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)

  while (iterator.hasNext) {
    println(s"element = ${iterator.next()}")
  }

}
