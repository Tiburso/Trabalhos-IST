public class Laranjeira extends Arvore {
	private double acidez;

	public Laranjeira(int idade, double altura, double acidez) {
		super(idade, altura);
		this.acidez = acidez;
	}

	public double getAcidez() { return this.acidez; }
	public void setAcidez(double acidez) { this.acidez = acidez; }

	public void desenvolverEspinhos() {
		System.out.println("Uma laranjeira desenvolveu espinhos");
	}

	@Override
	public boolean equals(Object other) {
		if(other instanceof Laranjeira) {
			Laranjeira l = (Laranjeira) other;
			return super.equals(l) && this.acidez == l.acidez;
		}

		return false;
	}

	@Override
	public String toString() {
		return super.toString() + " Acidez:" + this.acidez;
	}
}