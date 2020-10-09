public class Cao {

	private String nome;
	private double peso;

	public Cao(String nome, double peso) {
		this.nome = nome; 
		this.peso = peso;
	}

	@Override
	public boolean equals (Object other) {
		if (other instanceof Cao) {
			Cao a = (Cao) other;
			return this.name.equals(a.name) && this.peso == other.peso;
		}

		return false;
	}

	@Override
	public String toString() {
		return "Name: " + this.name + "Peso: " + this.peso + "KG";
	}

	public void ladra (int volume) {
		System.out(this.name + "ladra a um volume de " + volume);
	} 

	public void rosna	 (Cao other) {
		System.out.println("O " + this.name + "rosna ao " + other.name); 
	}
}