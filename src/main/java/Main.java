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
  public int getArea() {
    return x * y;
  }
  public int getPerimeter() {
    return 2 * (x + y);
  }
}


public class Main {
  public static void main(String[] args) {
     Square square = new Square(103, 12);

     System.out.println("The Sum of " +square.getX() +" and " +square.getY() +" is " +square.getSum());

    System.out.println("The Area of " +square.getX() +" and " +square.getY() +" is " +square.getArea() +"m");

  System.out.println("The Perimeter of " +square.getX() +" and " +square.getY() +" is " +square.getPerimeter() +"m");
   }
}