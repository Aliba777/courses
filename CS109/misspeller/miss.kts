val random = java.util.Random()
fun readPronounciations(): Map<String, Set<String>> {
  val words = java.io.File("words.txt").useLines { it.toSet() + setOf("i", "a") }
  val M = mutableMapOf<String, Set<String>>()
  java.io.File("cmudict.txt").forEachLine { l ->
    if (l[0].isLetter()) {
      val p = l.trim().split(Regex("\\s+"), 2)
      val i = p[0].indexOf('(')
      val word = (if (i >= 0) p[0].substring(0,i) else p[0]).toLowerCase()
      if (word in words) {
	val pro = p[1]
	val S = M.getOrElse(word) { emptySet<String>() }
	M[word] = S + pro
      }
    }
  }
  return M
}

fun reverseMap(m: Map<String, Set<String>>): Map<String,Set<String>> {
  var r = mutableMapOf<String,MutableSet<String>>()
  for ((word, pro) in m) {
    for (item in pro) {
      val s = r.getOrElse(item) { mutableSetOf<String>() }
      s.add(word)
      r[item] = s
    }
  }
  return r
}


//val m = readPronounciations()
//val r = reverseMap(m)

//print(m["i"])
//print(r[m["right"]])

java.io.File("poem.txt").forEachLine {
  if (it != "") {
    val m = readPronounciations()
    val r = reverseMap(m)
    val words = it.split(Regex("[ :;?!<>()-]+"))
    for (word in words) {
      var lower = word.toLowerCase()
      if (m[lower] != null) {
        var prolist = m[lower]!!.toList()
        var rand = random.nextInt(prolist.size)
        var randpro = prolist[rand]
        var wordlist = r[randpro]!!.toList()
        rand = random.nextInt(wordlist.size)
        var randword = wordlist[rand]
        //var need = r[m[word]]
        //println(need)
        if (randword != lower)
          if (word.toUpperCase() == word)
            print(randword.toUpperCase() + " ")
          else if (word[0].isUpperCase())
            print(randword[0].toUpperCase() + randword.substring(1, randword.length) + " ")
          else
            print(randword + " ")
        else
          print(word + " ")
      }
      else
        print(word + " ")
      }
    
  }
  println("")
}

