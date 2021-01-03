public class Pessoa {
	private int idade;
	private String nome;

	public Pessoa(int idade, String nome) {
		this.idade = idade;
		this.nome = nome;
	}

	public String getNome() { return this.nome; }

	public int getIdade() { return this.idade; }

	public void setNome(String nome) { this.nome = nome; }

	public void setIdade(int idade) { this.idade = idade; }

	@Override
	public boolean equals(Object other) {
		if (other instanceof Pessoa) {
			return this.equals.nome(other) && this.idade == other.idade;
		}
	}

	@Override
	public String toString() {
		return "Nome:" + this.name + ", Idade:" + this.idade;
	}

	public String dorme(int tempo) {
		return this.nome + "dorme por " + tempo + " segundos"
	}

	public String fala(Pessoa other) {
		return this.nome + " fala com " + other.nome;
	}

}