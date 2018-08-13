package no.uio.ifi.pascal2100.main;
import no.uio.ifi.pascal2100.parser.*;
import no.uio.ifi.pascal2100.scanner.*;

public class PascalError extends RuntimeException {
	// Since RuntimeException extends Exception and
	// Exception implements Serializable, it should define this constant:
	private static final long serialVersionUID = 20150629L;

	PascalError(String message) {
		super(message);
	}
}
