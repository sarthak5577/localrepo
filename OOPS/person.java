package second;

public class person {
String name="Sarthak";
int age=20;

void display() {
	
	System.out.print("Person Name"+name);
	System.out.println("Person Age"+age);
}
}

class details extends person {
	int Personid=2165;
	void show() {
		System.out.println("Person ID is "+Personid);
		
	}
}
class salary extends person{
	int salaryem=210000;
	void watch() {
		System.out.println("Salary of employee:- "+salaryem);
	}
}
class main{
	public static void main (String args[]) {
		details e=new details(); 
		e.display();
		e.show();
		salary k=new salary(); 
		k.watch();
	}
}
