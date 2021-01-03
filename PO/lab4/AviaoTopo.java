public class AviaoTopo extends AviaoMedio {
	
	private Motor extra;

	public AviaoTopo(Motor motor) {
		super(motor);
		this.extra = null;
	}

	public AviaoTopo(Motor motor, Motor extra) {
		this(motor);
		this.extra = extra;
	}

	public void addExtra(Motor extra) {
		this.extra = extra;
	}

	@Override
	public void andar() {
		super.andar();
		if (extra != null) this.extra.on();
	}

	@Override
	public void parar() {
		super.parar();
		if (extra != null) this.extra.off();
	}

}