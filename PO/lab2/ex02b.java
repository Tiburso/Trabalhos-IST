public class Cao {

	private String nome;
	private double peso;

	public Cao(String nome, double peso) {
		this.nome = nome; 
		this.peso = peso;
	}

	public String getNome() {
		return this.name;
	}

	public double getPeso() {
		return this.peso;
	}

	public void setNome(String name) {
		this.name = name
	}

	public void setPeso (double peso) {
		this.peso = peso;
	}

	@Override
	public boolean equals (Object other) {
		if (other instanceof Cao) {
			Cao a = (Cao) other;
			return this.name.equals(a.name) && this.peso == this.nome;
		}

		return false;
	}

	@Override
	public String toString () {
		return "Name: " this.name + "Peso: " + this.peso + "Kg";
	}

	public String ladra (int volume) {
		return this.name + "ladra a um volume de " + volume;
	} 

	public String rosna (Cao other) {
		return "O " + this.name + "rosna ao " other.name;
	}
}