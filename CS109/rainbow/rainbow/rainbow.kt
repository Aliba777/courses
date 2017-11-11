import org.otfried.cs109ui.*
import org.otfried.cs109ui.ImageCanvas
import org.otfried.cs109.Color
import org.otfried.cs109.DrawStyle

import java.awt.image.BufferedImage
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
fun draw(image: BufferedImage, value: Int) {
  for (x in 0 until 360) {
    for (y in 0 until 256) {
      var (red, green, blue) = hsvtorgb(x, y, value)
      val color = (red * 65536) + (green * 256) + blue
      image.setRGB(x, y, color)
    }
  }
}

fun main(args: Array<String>) {
  var v = 255
  if (args.size == 1) {
    v = args[0].toInt()
  }
  val image = BufferedImage(360, 256, BufferedImage.TYPE_INT_RGB)
  draw(image, v)
  show(image)
  setTitle("Rainbow for v = ${v}")
}