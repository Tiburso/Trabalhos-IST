public class Arvore {
	private int idade; 
	private double altura;


	public Arvore(int idade) {
		this.idade = idade;
		this.altura = 1;
	}

	public Arvore(int idade, double altura) {
		this(idade); 
		this.altura = altura;
	}

	public int getIdade() { return this.idade; }
	public double getAltura() { return this.altura; }
	public void setIdade(int idade) { this.idade = idade; }
	public void setAltura(double altura) { this.altura = altura; }

	public void florescer() {
		System.out.println("Uma arvore floresceu");
	}

	@Override
	public boolean equals(Object other) {
		if(other instanceof Arvore) {
			Arvore arvore = (Arvore) other;
			return this.idade == arvore.idade && this.altura == arvore.altura;
		}

		return false;
	}

	@Override
	public String toString() {
		return "Idade:" + this.idade + " Altura:" + this.altura;
	}

}