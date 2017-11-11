import org.otfried.cs109.Context
import org.otfried.cs109.MiniApp
import org.otfried.cs109.Canvas
import org.otfried.cs109.Color
import org.otfried.cs109.DrawStyle
import org.otfried.cs109.TextAlign
import java.lang.Math

class Main(val ctx: Context) : MiniApp {
	private val a = Array<Array<Int>>(4) { arrayOf(0, 0, 0, 0) }
	private val chooseFrom = listOf(2,2,2,2,2,2,2,2,2,4) //For random insertion
	val random = java.util.Random();
	var score = 0
	var finished = false
	val tileColors = mapOf(0 to Color(205, 192, 180), 2 to Color(0xeee4da),
		     4 to Color(0xede0c8), 8 to Color(0xf2b179),
		     16 to Color(0xf59563), 32 to Color(0xf67c5f),
		     64 to Color(0xf65e3b), 128 to Color(0xedcf72),
		     256 to Color(0xedcc61), 512 to Color(0xedc850),
		     1024 to Color(0xedc53f), 2048 to Color(0xedc22e))
	val otherTileColor = Color(0x3c3a32)
	val backgroundColor = Color(0xbbada0)
	val lightTextColor = Color(119, 110, 101)
	val darkTextColor = Color(0xf9f6f2)
	var changed = false
	
	init {
		insert()
		insert()
		if (!finished){
			ctx.setTitle("2048")
			ctx.onFling { x, y, dir, d -> flinged(dir) }
		}
	}
	
	fun flinged(dir: Char) {
		when(dir) {
			'l' -> score+=pushLeft()
			'd' -> score+=pushDown()
			'r' -> score+=pushRight()
			else -> score+=pushUp()
		}
		if (changed)
			insert()
		changed = false
		ctx.update()
	}
	
	override fun onDraw(canvas: Canvas) {
		canvas.clear(backgroundColor)
		var x = canvas.width.toDouble()
		var y = canvas.height.toDouble()
		var square = (x - 120.0) / 4.0
		var h = y - 4.0 * square - 160.0 
		for (row in 0 until 4){
			for (col in 0 until 4){
				var tileNum = a[row][col]
				canvas.setColor(tileColors[tileNum] ?: otherTileColor)
				canvas.drawRectangle(30.0 + (square + 20.0 ) * col, h + (square + 20.0 ) * row, square, square)
				if (tileNum > 0) {
					canvas.setColor(textColor(tileNum))
					canvas.setFont(textSize(tileNum))
					val s = tileNum.toString()
					val w = canvas.textWidth(s)
					canvas.drawText(s, 30.0 + (square + 20.0) * col + square / 2.0 - w/2, h + (square + 20.0) * row + square / 2.0 + textSize(tileNum) / 2.0)
				}
			}
		}
		finished = gameOver()
		canvas.setColor(Color(205, 192, 180))
		canvas.drawRectangle( x / 2.0 + x / 10.0 , y / 8.0 , x / 4.0 , y / 15.0)
			
		canvas.setColor(Color.BLACK)
		canvas.setFont(36.0)
		canvas.drawText(score.toString(),x / 2.0 + x / 10.0 + x / 8.0 - canvas.textWidth(score.toString()) / 2.0 , y / 8.0 + y / 30.0 + 18.0)
		if (finished){
			canvas.setColor(Color.BLACK)
			canvas.setFont(70.0)
			canvas.drawText("GAME OVER!", x / 2.0 - canvas.textWidth("GAME OVER!") / 2.0 , y / 2.0 )
		}
	}
	
	fun textSize(tileValue: Int) = 
	if (tileValue <= 64) 55.0
	else if (tileValue <= 512) 45.0
	else if (tileValue <= 2048) 35.0
	else 30.0
	
	fun textColor(tileValue: Int) = if (tileValue <= 4) lightTextColor else darkTextColor
	
	fun gameOver(): Boolean{
		if (!isFull()) return false
		
		for (i in 0 until 4){
			for (j in 0 until 4){
				if (i-1 >= 0 && a[i-1][j] == a[i][j])
					return false
				else if (i+1 < 4 && a[i+1][j] == a[i][j])
					return false
				else if (j-1 >= 0 && a[i][j-1] == a[i][j])
					return false
				else if (j+1 < 4 && a[i][j+1] == a[i][j])
					return false
			}
		}
		return true
	}
	
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
      changed = true
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
    changed = true
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
    changed = true
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
    changed = true
    return points
  }
}