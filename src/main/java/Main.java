class Square {
  private int x;
  private int y;

  public Square(int x, int y) {
    this.x = x;
    this.y = y;
  }
  public int getX() {
    return x;
  }
  public int getY() {
    return y;
  }
  public int getSum(){
    return x + y;
  }
}


public class Main {
  public static void main(String[] args) {
     Square square = new Square(103, 12);

     System.out.println("The Sum of " +square.getX() +" and " +square.getY() +" is " +square.getSum());
   }
}