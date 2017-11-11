val words = java.io.File("words.txt").useLines { it.toSet() }

fun sortWord(s: String): String =
    s.toCharArray().sorted().joinToString(separator="")

fun findAnagrams(word: String): List<String> {
	return words.filter {sortWord(word).toLowerCase().replace(" ", "") == sortWord(it)}
}

fun ePluribusUnum(phrase: String) {
  println("E pluribus unum: '$phrase' --> '${findAnagrams(phrase)}'")
}

fun IEorEI() {
	println("contain 'cie' " + words.count {"cie" in it})
	println("contain 'cei' " + words.count {"cei" in it})
	println("contain 'ei', but not 'cei'" + words.count {"ei" in it && "cei" !in it})
	println("containt 'ie', but not 'cie'" + words.count {"ie" in it && "cie" !in it})

}
IEorEI()
fun similarWords() {
	var l1 = words.filter {it.length == 7}.toSet()
	var l2 = words.filter {it.length == 8 && it[1] == 't'}.toSet()
	var l3 = l2.filter {(it.substring(0, 1) + it.substring(2, 8)) in  l1}
	println(l3.max())

	l1 = words.filter {it.length == 6}.toSet()
	l2 = words.filter {it.length == 7 && it[0] == 'z'}.toSet()
	l3 = l2.filter {(it.substring(1, 7)) in  l1}
	println(l3.max())

	l1= words.filter {it.length == 10}.toSet()
	l2 = words.filter {it.length == 11 && it[5] == 't'}.toSet()
	l3 = l2.filter {(it.substring(0, 5) +it.substring(6, 11)) in  l1}
	println(l3.max())

	l1 = words.filter {it.length == 7 && it[4] == 'c'}.toSet()

	l2 = words.filter {it.length == 7 && it[4] == 'd'}.toSet()
	l3 = l2.filter {(it.substring(0, 4) + 'c' +it.substring(5, 7)) in  words}
	println(l3[8])
}

fun fourDifferentWords() {
	var l4 = words.filter { it.length == 9 && it.startsWith("expe") }.map { it.substring(4) }.filter { "e" + it in words && "au" + it in words && "cre" + it in words}
	println("expe" + l4.joinToString())	
	var l1 = words.filter { it.length == 5 && it.startsWith("rh") }.map { it.substring(2) }.filter { "b" + it in words && "c" + it in words && "t" + it in words }
	println("rh" + l1.joinToString())
}


similarWords()
fourDifferentWords()