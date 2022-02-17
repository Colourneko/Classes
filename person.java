
public class person {
	private String Fname;
	private String Lname;
	private int age;
	
	public person(String Fname, String Lname, int age) {
		}
	/**
	 * @return the name
	 */
	public String getFName() {
		return Fname;
	}
	/**
	 * @param name the name to set
	 */
	public void setFName(String Fname) {
		this.Fname = Fname;
	}
	/**
	 * @return the name
	 */
	public String getLName() {
		return Lname;
	}
	/**
	 * @param name the name to set
	 */
	public void setLname(String Lname) {
		this.Lname = Lname;
	}
	/**
	 * @return the age
	 */
	public int getAge() {
		return age;
	}
	/**
	 * @param age the age to set
	 */
	public void setAge(int age) {
		this.age = age;
	}
	
	public String toString() {
		return this.Fname + " " + this.Lname;
		
	}
	
	public static void main(String args[]) {
		
		person newPerson = new person(null,null, 0);
		newPerson.setFName("Luke");
		newPerson.setLname("Edmunds");
		newPerson.setAge(90);
		
		System.out.println(newPerson.toString());
	
	
		
	}

		
	}
	

