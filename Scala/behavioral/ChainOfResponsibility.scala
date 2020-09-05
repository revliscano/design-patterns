package behavioral

import java.util.{Calendar, Date}

import scala.util.{Failure, Success, Try}

object ChainOfResponsibility extends App {

  abstract class Certificate(val nextCertificate: Option[Certificate], val validityDate: Date) {

    def isValid: Boolean = validityDate.after(Calendar.getInstance().getTime)

    def isTrusted: Boolean

    def validateNext: Try[Certificate] => Boolean = {
      case Success(next) => next.verify
      case Failure(_) =>
        println("Certificate is not valid because next chain element is missing")
        false
    }

    def verify: Boolean = {
      println(this.getClass)
      if (!isValid) {
        println("Certificate is not valid because validity date is not in the future")
        false
      }
      else if (isValid && isTrusted) {
        true
      }
      else {
        validateNext(Try(nextCertificate.get))
      }
    }
  }

  class EndEntityCertificate(override val nextCertificate: Option[Certificate], override val validityDate: Date)
    extends Certificate(nextCertificate, validityDate) {
    override def isTrusted: Boolean = false
  }

  class IntermediateCertificate(override val nextCertificate: Option[Certificate], override val validityDate: Date)
    extends Certificate(nextCertificate, validityDate) {
    override def isTrusted: Boolean = false
  }

  class RootCertificate(override val validityDate: Date)
    extends Certificate(None, validityDate) {
    override def isTrusted: Boolean = true
  }

  val date = Calendar.getInstance()
  date.add(Calendar.HOUR, 10)
  val certificateValidityDate: Date = date.getTime

  val rootCertificate = new RootCertificate(certificateValidityDate)
  val intermediateCertificate1st = new IntermediateCertificate(Some(rootCertificate), certificateValidityDate)
  val intermediateCertificate2nd = new IntermediateCertificate(Some(intermediateCertificate1st), certificateValidityDate)
  val intermediateCertificate3rd = new IntermediateCertificate(Some(intermediateCertificate2nd), certificateValidityDate)
  val endEntityCertificate = new EndEntityCertificate(Some(intermediateCertificate3rd), certificateValidityDate)
  
  println(endEntityCertificate.verify)

}
