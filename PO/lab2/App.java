public class App {
	public static void main(String[] args) {
		Cao a = new Cao("Bolinha", 50);
		Cao b = new Cao("Rolindo", 34);

		System.out.println(a.equals(b));
		System.out.println(a);

		a.ladra(30);
		a.rosna(b);
	}
}