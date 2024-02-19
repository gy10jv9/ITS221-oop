class Square {
  	private int side;

  	public Square(int side) {
    	this.side = side;
  	}

	public void setSide(int newSide) {
		this.side = newSide;

		System.out.println("Changed side to " +newSide +" successfully!");
		return;
	}

  	public int getArea() {
  	  	return side * side;
  	}

  	public int getPerimeter() {
  	  	return 2 * (side + side);
  	}
}


public class Main {
  	public static void main(String[] args) {
     	Square square = new Square(15);

    	System.out.println("The Area of the square is " +square.getArea());
		System.out.println("The Area of the square is " +square.getPerimeter());

		square.setSide(5);

		System.out.println("The Area of the square is " +square.getArea());
		System.out.println("The Area of the square is " +square.getPerimeter());
   	}
}