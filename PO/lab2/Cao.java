public class Cao {

	private String name;
	private double peso;

	public Cao(String nome, double peso) {
		this.name = nome; 
		this.peso = peso;
	}

	@Override
	public boolean equals (Object other) {
		if (other instanceof Cao) {
			Cao a = (Cao) other;
			return this.name.equals(a.name) && this.peso == a.peso;
		}

		return false;
	}

	@Override
	public String toString() {
		return "Name: " + this.name + "Peso: " + this.peso + "KG";
	}

	public void ladra (int volume) {
		System.out.println(this.name + "ladra a um volume de " + volume);
	} 

	public void rosna	 (Cao other) {
		System.out.println("O " + this.name + "rosna ao " + other.name); 
	}
}