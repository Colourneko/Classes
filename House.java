
public class House {
	private String address;
	private int numOfRooms;
	private float price;
	private boolean isForSale;
	public House(String string, int i, double d, boolean b) {
		// TODO Auto-generated constructor stub
	}
	/**
	 * @return the address
	 */
	public String getAddress() {
		return address;
	}
	/**
	 * @param address the address to set
	 */
	public void setAddress(String address) {
		this.address = address;
	}
	/**
	 * @return the numOfRooms
	 */
	public int getNumOfRooms() {
		return numOfRooms;
	}
	/**
	 * @param numOfRooms the numOfRooms to set
	 */
	public void setNumOfRooms(int numOfRooms) {
		this.numOfRooms = numOfRooms;
	}
	/**
	 * @return the price
	 */
	public float getPrice() {
		return price;
	}
	/**
	 * @param price the price to set
	 */
	public void setPrice(float price) {
		this.price = price;
	}
	/**
	 * @return the isForSale
	 */
	public boolean isForSale() {
		return isForSale;
	}
	/**
	 * @param isForSale the isForSale to set
	 */
	public void setForSale(boolean isForSale) {
		this.isForSale = isForSale;
	}
	
	public static void main(String arg[]) {
		
		House house = new House("home",10,10.99,true);
		System.out.println(house.toString());
	}

}
