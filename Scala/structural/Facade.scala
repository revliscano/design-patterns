package structural

import java.time.format.DateTimeFormatter.ISO_LOCAL_TIME
import java.time.temporal.ChronoUnit.SECONDS
import java.time.{ZoneId, ZonedDateTime}

import scala.util.{Failure, Random, Success, Try}

object Facade extends App {

  class TimeService {
    def getTime(country: String): ZonedDateTime = ZonedDateTime.now(Map(
      "Venezuela" -> ZoneId.of("America/Caracas"),
      "Poland" -> ZoneId.of("Europe/Warsaw"),
      "Austria" -> ZoneId.of("Europe/Vienna")
    )(country))
  }

  class LanguageService {
    def getGreetingPhrase(country: String): Option[String] = Map(
      "Venezuela" -> "Buenos dias",
      "Poland" -> "Dzien dobry",
      "Austria" -> "Guten Tag"
    ).get(country)
  }

  class MoodService {
    def getMoodPhrase: String = List(
      "I am so happy to hear you!",
      "I don't want to speak with you."
    )(Random.nextInt(2))
  }

  class Chatbot(val languageService: LanguageService, val timeService: TimeService, val moodService: MoodService) {
    def respond(inputStatement: String): String = {
      val s"Hi! My name is $name. I live in $country." = inputStatement
      val greeting = languageService.getGreetingPhrase(country).getOrElse("Good morning")
      val time = Try(timeService.getTime(country)) match {
        case Success(value) => ISO_LOCAL_TIME.format(value.truncatedTo(SECONDS))
        case Failure(_) => "unknown"
      }
      val moodPhrase = moodService.getMoodPhrase
      s"$greeting, $name! Current time in $country is $time. $moodPhrase"
    }
  }

  val chatbot = new Chatbot(new LanguageService, new TimeService, new MoodService)
  println(chatbot.respond("Hi! My name is Lukasz. I live in Austria."))
  println(chatbot.respond("Hi! My name is Rafael. I live in Venezuela."))
}
