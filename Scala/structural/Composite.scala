package structural

import scala.collection.mutable.ListBuffer

object Composite extends App {

  trait Node {
    def ==(): Int
  }

  case class BranchNode(children: ListBuffer[Node]) extends Node {
    def +(child: Node): BranchNode = {
      children += child
      this
    }

    def -(child: Node): BranchNode = {
      children -= child
      this
    }

    override def ==(): Int = children.map(child => child.==()).sum
  }

  case class Leaf(value: Int) extends Node {
    override def ==(): Int = value
  }

  val b = BranchNode(ListBuffer())
  b + Leaf(1)
  b + Leaf(2)
  b + BranchNode(ListBuffer(Leaf(3), Leaf(4)))
  b - Leaf(2) - Leaf(1) - BranchNode(ListBuffer(Leaf(3), Leaf(4))) + Leaf(256)

  println(b.==())
}
