//
// Gravity sensor test #1
//

import org.otfried.cs109.Context
import org.otfried.cs109.MiniApp
import java.util.Date
import org.otfried.cs109.Canvas
import org.otfried.cs109.Color
import org.otfried.cs109.DrawStyle
import org.otfried.cs109.TextAlign

fun sq(x: Double) = x * x
fun abs(x: Double): Double {
  if (x >= 0)
    return x
  else
    return -x
}
class Main(val ctx: Context) : MiniApp {
  var gravity = arrayOf(0.0, 0.0, 0.0)
  var x1 = 0.0
  var y1 = 0.0
  var x1_bl = 20.0
  var y1_bl = 20.0
  var direction = 1
  var current_time = Date().getTime()
  var hit_count = 0
  var disappeared_time = Date().getTime()
  var s = ""
  var current_x = 0.0
  var current_y = 0.0
  init {
    ctx.setTitle("Game by Alibek")
    ctx.onGravity { x, y, z -> updateGravity(x, y, z) }
    ctx.onTap { x, y -> hitted("Tapped") }
    ctx.update()
  }

  fun updateGravity(x: Double, y: Double, z: Double) {
    gravity = arrayOf(x, y, z)
    ctx.update()
  }
  fun hitted(k: String) {
    s = k
    ctx.update()
  }


  override fun onDraw(canvas: Canvas) {
    val x = canvas.width / 2.0
    val y = canvas.height / 2.0


    if (gravity[0] >= 0 && gravity[1] >= 0) { // 1 right top

      if (x1 + gravity[0] <= x / 2.0 - x / 7.0 && x1 + gravity[0]  > -x / 2.0 + x / 7.0 ) {
        x1 += gravity[0]
      if (y1 + gravity[1]  >= -y / 4.0  && y1 + gravity[1] <= y / 4.0 - y / 13.0)
        y1 += gravity[1]
      }
    }

    if (gravity[0] >= 0 && gravity[1] < 0) { // 2 right bot
      if (x1 + gravity[0] <= x / 2.0 - x / 7.0 && x1 + gravity[0] > -x  / 2.0 + x / 7.0) {
        x1 += gravity[0]
      if (y1 + gravity[1]  >= -y / 4.0 && y1 + gravity[1] <= y / 4.0 - y / 13.0)
        y1 += gravity[1]
      }
    }
    if (gravity[0] < 0 && gravity[1] >= 0) { // 3 left top
      if (x1 + gravity[0] <= x / 2.0 && x1 + gravity[0] > -x / 2.0 + x / 7.0 ) {
        x1 += gravity[0]
      if (y1 + gravity[1] >= -y / 4.0  && y1 + gravity[1] <= y / 4.0 - y / 13.0)
        y1 += gravity[1]
      }
    }

    if (gravity[0] < 0 && gravity[1] < 0) { // 4 left bot
      if (x1 + gravity[0]  <= x / 2.0 + x / 7.0 && x1 + gravity[0] > -x  / 2.0 + x / 7.0) {
        x1 += gravity[0]
      if (y1 + gravity[1] >= -y / 4.0 && y1 + gravity[1]  <= y / 4.0 - y / 13.0)
        y1 += gravity[1]
      }
    }
    canvas.clear(Color(255, 255, 192))
    canvas.setColor(Color.BLUE)
    canvas.setFont(48.0)
    for (i in 0..2)
      canvas.drawText("%.3f".format(gravity[i]), x, 80.0 + i * 60.0, 
                      TextAlign.CENTER)
    val norm = Math.sqrt(sq(gravity[0]) + sq(gravity[1]) + sq(gravity[2]))
    canvas.drawText("%.3f".format(norm), x, 300.0, TextAlign.CENTER)
    canvas.setColor(Color.RED)
    if (s == "Tapped") {
      canvas.save()
      canvas.setColor(Color.BLUE)
      canvas.drawRectangle(current_x, current_y, x/7, y/10, DrawStyle.FILL)
      canvas.rotate(-90.0)
      canvas.restore()
      if (abs(x1_bl - current_x) <= x / 7.0 && abs(y1_bl - current_y) <= x) {
      //println(hit_count)
        hit_count += 1
        //println(hit_count)
        println(x1_bl)
        println(current_x)
      }
      //println(current_x)
      //println(current_y)
      s = ""
    }
    else
    {    
      canvas.drawRectangle(x / 100 * x1 + x, y / 100 * y1 + y, x/7, y/10, DrawStyle.FILL)
      current_x = x / 100 * x1 + x
      current_y = y / 100 * y1 + y
    }
    canvas.setColor(Color.BLACK)
    if (x1_bl >= x) {
      direction = -1
    }
    else if (x1_bl < 0) {
      direction = 1
    }
    x1_bl += direction * 20.0
    //println("x1 is ${x1}")
    //println("x1_bl is ${x1_bl}")


    current_time = Date().getTime()
    if (hit_count == 3){
      print(hit_count)
      disappeared_time = Date().getTime()
      hit_count = 0
    }
    else if ((current_time - disappeared_time) / 1000 > 3) {
      canvas.drawRectangle(20.0 + x1_bl, 20.0 + y1_bl, x/7.0, y/10.0, DrawStyle.FILL)
    }
    //println("x1_bl is ${x1_bl}")
    //println("y1_bl is ${y1_bl}")
    // canvas.drawCircle(canvas.width / 2.0 + gravity[0] * canvas.width / 28.0, canvas.height / 2.0 - gravity[1] * canvas.width / 28.0, canvas.width / 8.5)
    
    // canvas.setColor(Color.BLUE)
    // #canvas.drawCircle(canvas.width / 2.0, canvas.height / 2.0, canvas.width / 7.0, DrawStyle.STROKE)
    // #canvas.drawCircle(canvas.width / 2.0, canvas.height / 2.0, canvas.width / 2.0 - 20, DrawStyle.STROKE)
  }
}

