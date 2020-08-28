package creational

import scala.util.Random.nextInt

object Prototype extends App {

  class DNAService {
    def generateDNA: String = (1 to 100000000).map(_ => "CGAT"(nextInt(4))).mkString
  }

  abstract class Tomato(val dna: String) extends Cloneable {
    override def clone(): Tomato = super.clone().asInstanceOf[Tomato]
  }

  class PlumTomato(override val dna: String) extends Tomato(dna)

  class CherryTomato(override val dna: String) extends Tomato(dna)

  val dnaService = new DNAService

  println("Creating tomato...")
  val tomato: Tomato = new PlumTomato(dnaService.generateDNA)
  println(s"Tomato with DNA ${tomato.dna.substring(0, 10)}... created.")

  println("Cloning tomato...")
  val clonedTomato = tomato.clone()
  println(s"Tomato with DNA ${clonedTomato.dna.substring(0, 10)}... cloned.")
}
