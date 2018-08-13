package no.uio.ifi.pascal2100.parser;
import no.uio.ifi.pascal2100.scanner.*;
import no.uio.ifi.pascal2100.main.*;

public abstract class Operator extends PascalSyntax {
	 	Operator nextOpr = null;
	 	TokenKind oprToken;
	public Operator(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		
	}

}
