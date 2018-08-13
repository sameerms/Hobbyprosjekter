package no.uio.ifi.pascal2100.parser;
import java.util.EnumSet;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;


	abstract class Statement extends PascalSyntax {
		
		Block b;
		public static Statement st = null;
		public IfStatm ifsta;

		public StatmList stmlist;
		public Statement nextstmt;
		
	Statement(int lNum) {
	super(lNum);
	}
	 
    
	static Statement parse(Scanner s) {
	enterParser("statement");
	
	switch (s.curToken.kind) {
	case beginToken:
		
	st = CompoundStatm.parse(s); break;
	case ifToken:
	st = IfStatm.parse(s); break;
	case nameToken:
	switch (s.nextToken.kind) {
	case assignToken:
	case leftBracketToken:
	st = AssignStatm.parse(s); break;
	default:
	st = ProcCallStatm.parse(s); break;
	} break;
	case whileToken:
	st = WhileStatm.parse(s); break;
	default:
	st = EmptyStatm.parse(s); break;
	}
	leaveParser("statement");
	
	return st;
	}
	/*@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<statement> " + " on line " + lineNum;
	}

	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		System.out.println("kommer hit for Œ printe");
		if (st != null) st.prettyPrint();
		
	}*/

}
