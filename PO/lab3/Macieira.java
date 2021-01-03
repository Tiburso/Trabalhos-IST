public class Macieira extends Arvore {
	private String cor;

	public Macieira(int idade, double altura, String cor) {
		super(idade, altura);
		this.cor = cor;
	}

	public String getCor() { return this.cor; }
	public void setCor(String cor) { this.cor = cor; }

	public void perderFolhas() {
		System.out.println("Uma macieira perdeu folhas");
	}

	@Override
	public boolean equals(Object other) {
		if(other instanceof Macieira) {
			Macieira m = (Macieira) other;
			return super.equals(m) && this.cor.equals(m.cor);
		}

		return false;
	}

	@Override
	public String toString() {
		return super.toString() + " Cor:" + this.cor;
	}


}