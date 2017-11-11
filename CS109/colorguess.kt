import org.otfried.cs109ui.*
import org.otfried.cs109ui.ImageCanvas
import org.otfried.cs109.Color
import org.otfried.cs109.DrawStyle
import org.otfried.cs109.readString
import java.awt.image.BufferedImage
val random = java.util.Random()

// Input h in [0,359], s in [0,255], v in [0,255]
// Output r,g,b in [0,255]
fun hsvtorgb(h: Int, s: Int, v: Int): Triple<Int, Int, Int> {
  if (s == 0) {
    // no color, just grey
    return Triple(v, v, v)
  } else {
    val sector = h / 60
    val f = (h % 60) 
    val p = v * ( 255 - s ) / 255
    val q = v * ( 15300 - s * f ) / 15300
    val t = v * ( 15300 - s * ( 60 - f )) / 15300
    return when(sector) {
      0 -> Triple(v, t, p)
      1 -> Triple(q, v, p)
      2 -> Triple(p, v, t)
      3 -> Triple(p, q, v)
      4 -> Triple(t, p, v)
      else -> Triple(v, p, q)
    }
  }
}

fun randomHSV(): Triple<Int, Int, Int> {
  return Triple(random.nextInt(360),
            128 + random.nextInt(128),
    128 + random.nextInt(128))
}

fun draw(image: BufferedImage, value: Int) {
  for (x in 0 until 360) {
    for (y in 0 until 256) {
      var (red, green, blue) = hsvtorgb(x, y, value)
      val color = (red * 65536) + (green * 256) + blue
      image.setRGB(x, y, color)
    }
  }
}

fun showWait(image: BufferedImage, value: Int, ms: Int) {
  draw(image, value)
  show(image)
  waitForMs(ms)
}

fun draw(image: BufferedImage, colors: Array<Array<Int>>) {
  val g = ImageCanvas(image)
  g.clear(Color.WHITE)
  g.setColor(Color.BLACK)
  for ( i in 1 until 5) {
    g.setFont(20.0, "Batang")
    g.drawText("${i}", 50.0, 65.0 + 70*i)
    var ch = (i+64).toChar()
    g.drawText("${ch}", 50.0 + 70*i, 70.0)
  }
  for (i in 0 until 4) {
    for (j in 0 until 4) {
      g.setColor(Color(colors[i][j]))
      g.drawRectangle(100.0 + (i*70.0), 100.0 + (j*70.0), 60.0, 60.0, DrawStyle.FILL)
    }
  }
}
fun main(args: Array<String>) {
  var condition = true
  var count = 0
  var right = 0
  var colors = Array(4) { Array(4) { 0 } }
  while (condition) {
    count += 1
    var (h, s, v) = randomHSV()
    var (red, green, blue) = hsvtorgb(h, s, v)
    val color = (red * 65536) + (green * 256) + blue
    
    var image = BufferedImage(500, 500, BufferedImage.TYPE_INT_RGB)
    var delta = 20
    if (args.size == 1) {
      delta = args[0].toInt()
    }
    for (i in 0 until 4) {
      for (j in 0 until 4) {
        colors[i][j] = color
      }
    }
    var x = random.nextInt(4)
    var y = random.nextInt(4)
    var coin = random.nextInt(2)
    if (coin == 0) {
      h = (h + delta) % 360
    }
    else {
      h = 360 - delta
    }
    var (r, g, b) = hsvtorgb(h, s, v)
    val diff_color = (r * 65536) + (g * 256) + b
    colors[y][x] = diff_color
    setTitle("How good is your color vision?")
    draw(image, colors)
    show(image)
    var x_guess = 0
    var y_guess = 0
    var choos = ""
    while (condition) {
      choos = readString("Which square has a different color? (x to exit) ").toLowerCase().trim()
      if (choos[0] == 'x') {
        System.exit(0)
      }
      else if(!(choos[1] in 'a'..'d' && (choos[0].toInt() - 48) <= 4 && (choos[0].toInt() - 48) > 0)) {
        println("Incorrect input! Try 3a")
      }
      else if (choos.length != 2) {
        println("Incorrect input! Try 3a")
      }
      else {
        x_guess = choos[0].toInt() - 49
        y_guess = choos[1].toInt() - 97
        println(x_guess)
        println(y_guess)
        break
      }
    }
    if (x_guess == x && y_guess == y) {
      right += 1
      println("That is correct!")
      println("You answered ${right} of ${count} tests correctly.")
    }
    else
    {
      println("That is not correct. Square ${choos} has a different color.")
      readString("Press Enter for the next question")
    }
  }
}