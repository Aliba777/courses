class Board {
  val random = java.util.Random()

  private val a = Array<Array<Int>>(4) { arrayOf(0, 0, 0, 0) } 

  private fun displayRow(s: StringBuilder, row: Int, 
			 form: String?, term: String) {
    for (col in 0 until 4) {
      if (form == null) {
	val m = a[row][col]
	if (m != 0) {
	  var ms = "   " + m.toString()
	  ms = ms.substring(ms.length - 3)
	  s.append(if (m < 1000) "|$ms " else "|$m")
	} else
	  s.append("|    ")
      } else
	s.append(form)
    }
    s.append(term)
    s.append('\n')
  }
  override fun toString(): String {
    val s = StringBuilder()
    for (row in 0 .. 3) {
      displayRow(s, row, "o----", "o")
      displayRow(s, row, "|    ", "|")
      displayRow(s, row, null, "|")
      displayRow(s, row, "|    ", "|")
    }
    displayRow(s, 3, "o----", "o")
    return s.toString()
  }

  // for debugging and testing
  constructor(vararg contents: Int) {
    if (contents.size != 0) {
      assert(contents.size == 15)
      for (row in 0 until 4)
        for (col in 0 until 4)
          a[row][col] = contents[4 * row + col]
    }
  }  
  
  // for debugging and testing
  fun toList(): List<Int> = a.flatMap { it.toList() }

  fun cell(row: Int, col: Int): Int = a[row][col]

  // is the board completely filled?
  fun isFull(): Boolean {
    var k = 0
    for (i in 0 until 4) {
      for (j in 0 until 4)
      {
        if (a[i][j] == 0) {
          k += 1
        }
      }
    }
    return k == 0
  }
  
  fun insert() {
    var random_num = random.nextDouble()
    var n: Int
    if (random_num > 0.9) {
      n = 4
    }
    else {
      n = 2
    }
    var x = random.nextInt(4)
    var y = random.nextInt(4)
    
    while(true) {
      if (a[x][y] == 0) {
        a[x][y] = n
        break
      }
      else {
        x = random.nextInt(4)
        y = random.nextInt(4)
      }
    }
  }
	
  fun pushLeft(): Int {
    var points = 0
    for (i in 0 until 4) {
      var merg = false
      for (j in 1 until 4) {
        if (a[i][j] != 0) {
          for (k in j downTo 1) {
            if (a[i][k-1] == 0) {
              a[i][k-1] = a[i][k]
              a[i][k] = 0
            }
            else if (a[i][k-1] == a[i][k] && !merg) { 
              a[i][k-1] += a[i][k]
              a[i][k] = 0
              merg = true
              points += a[i][k-1]
            }
            else {
              merg = false
              break
            }
          }
        }
      }
    }
    return points
  }

  fun pushRight(): Int {
    var points = 0
    for (i in 0 until 4) {
      var merg = false

      for (j in 2 downTo 0) {
        if (a[i][j] != 0) {
          for (k in j..2) {
            if (a[i][k+1] == 0) {
              a[i][k+1] = a[i][k]
              a[i][k] = 0
            }
            else if (a[i][k+1] == a[i][k] && !merg) { 
              a[i][k+1] += a[i][k]
              a[i][k] = 0
              merg = true
              points += a[i][k+1]
            }
            else {
              merg = false
              break
            }
          }
        }
      }
    }  
    return points
  }

  fun pushUp(): Int {
    var points = 0
    for (i in 0 until 4) {
      var merg = false
      for (j in 1 until 4) {
        if (a[j][i] != 0) {
          
          for (k in j downTo 1) {
            if (a[k-1][i] == 0) {
              a[k-1][i] = a[k][i]
              a[k][i] = 0
            }
            else if (a[k-1][i] == a[k][i] && !merg) { 
              a[k-1][i] += a[k][i]
              a[k][i] = 0
              points += a[k-1][i]
              merg = true
            }
            else {
              merg = false
              break
            }
          }
        }
      }
    }  
    return points
  }

  fun pushDown(): Int {
    var points = 0
    for (i in 0 until 4) {
      var merg = false
      for (j in 2 downTo 0) {
        if (a[j][i] != 0) {
          
          for (k in j..2) {
            if (a[k+1][i] == 0) {
              a[k+1][i] = a[k][i]
              a[k][i] = 0
            }
            else if (a[k+1][i] == a[k][i] && !merg) { 
              a[k+1][i] += a[k][i]
              a[k][i] = 0
              points += a[k+1][i]
              merg = true
            }
            else {
              merg = false
              break
            }
          }
        }
      }
    }  
    return points
  }

  // pushes in direction ch (in 'lrud')
  // returns number of points
  fun push(ch: Char): Int = when(ch) {
    'l' -> pushLeft()
    'r' -> pushRight()
    'u' -> pushUp()
    'd' -> pushDown()
    else -> 0
  }
}
