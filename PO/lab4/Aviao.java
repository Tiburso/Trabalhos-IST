public class Aviao {
	private Motor motor;

	public Aviao(Motor motor) {
		this.motor = motor;
	}

	public Motor getMotor() { return this.motor; }

	public void setMotor(Motor motor) { this.motor = motor; }

	public void andar() {
		this.motor.on();
	}

	public void parar() {
		this.motor.off();
	}
}