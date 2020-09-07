package creational

object Singleton extends App {

  object FederalReserveSystem {
    def superviseFinancialInstitutions: Any = println("... supervising financial institutions... ")
  }

  FederalReserveSystem.superviseFinancialInstitutions
}