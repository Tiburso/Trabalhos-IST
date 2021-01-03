public class App {
	public static void main(String[] args) {
		Arvore a1 = new Arvore(12);
		Arvore a2 = new Arvore(15, 1.5);

		Macieira m1 = new Macieira(10, 1.0, "vermelho");
		Macieira m2 = new Macieira(11, 1.0, "verde");

		Laranjeira l1 = new Laranjeira(6, 0.7, 15);
		Laranjeira l2 = new Laranjeira(2, 0.9, 10);

		System.out.println(a1);
		System.out.println(a2);

		m1.florescer();
		if(m1.equals(m2)) { System.out.println("Sao iguais"); } 
		else { System.out.println("Nao sao iguais"); }
		System.out.println(m1);
		m2.perderFolhas();

		
		if(m1.equals(m2)) { System.out.println("Sao iguais"); } 
		else { System.out.println("Nao sao iguais"); }
		System.out.println(l1);
		l2.desenvolverEspinhos();

	}
}