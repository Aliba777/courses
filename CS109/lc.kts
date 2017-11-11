val digits = 
  arrayOf(arrayOf(true, true, true, true, true, true, false),      // 0
	arrayOf(true, true, false, false, false, false, false),  // 1
	arrayOf(true, false, true, true, false, true, true),     // 2
	arrayOf(true, true, true, false, false, true, true),     // 3
	arrayOf(true, true, false, false, true, false, true),    // 4
	arrayOf(false, true, true, false, true, true, true),     // 5
	arrayOf(false, true, true, true, true, true, true),      // 6
	arrayOf(true, true, false, false, false, true, false),   // 7
	arrayOf(true, true, true, true, true, true, true),       // 8
	arrayOf(true, true, true, false, true, true, true),      // 9
	arrayOf(false, false, false, false, false, false, false)) // Blank


fun lcdDigit(digit: Char, k: Int, c: Char): String {
	var dig = if ('0' <= digit && digit <= '9') digit - '0' else 10

	var s : String
	s = " "
	for (j in 1..k) s += if (digits[dig][5]) c else ' '
	s += ' '
	s += "\n"

	for (i in 1..k) { // for k lines
		s += if (digits[dig][4]) c else ' '
		for (j in 1..k) s += ' '
		s += if (digits[dig][0]) c else ' '
		s += "\n" 
	}
	s += ' '
	for (j in 1..k) s += if (digits[dig][6]) c else ' '
	s += ' '
	s+= '\n'
	for (i in 1..k) { // for k lines
		s += if (digits[dig][3]) c else ' '
		for (j in 1..k) s += ' '
		s += if (digits[dig][1]) c else ' '
		s += "\n" 
	}

	s += ' '
	for (j in 1..k) s += if (digits[dig][2]) c else ' '
	s += ' '

	
	return s
}


fun combine(left: String, sep: String, right: String): String {
  var string1 = left.split("\n")
  var string2 = right.split("\n")
  var line = ""
  for(i in 0 .. (string1.size-2)) {
  	line += string1[i] + sep + string2[i] + '\n'
  }
  line += string1[string1.size-1] + sep + string2[string1.size-1]
  return line
}
fun lcd(s: String, k: Int, c: Char, sep: String): String {
  var result = lcdDigit(s[0], k, c)
  for (i in 1 until s.length)
    result = combine(result, sep, lcdDigit(s[i], k, c))
  return result
}

fun clearScreen() {
  println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
}

fun clock() {
  val form = java.text.SimpleDateFormat("HH mm ss")
  var current = form.format(java.util.Calendar.getInstance().getTime())
  clearScreen()
  println(lcd(current, 4, '#', " "))
  while (true) {
    Thread.sleep(100)
    val ntime = form.format(java.util.Calendar.getInstance().getTime())
    if (ntime != current) {
      current = ntime
      clearScreen()
      println(lcd(current, 4, '#', " "))
    }
  }
}
clock()