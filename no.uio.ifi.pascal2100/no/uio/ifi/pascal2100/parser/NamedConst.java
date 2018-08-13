package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

public class NamedConst extends Constant {

	 String name;
	public NamedConst(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	public static NamedConst parse(Scanner s) {
		enterParser("named constant");
		NamedConst nm= new NamedConst (s.curLineNum());
		
		s.test(nameToken);
		nm.name= s.curToken.id;
		
		s.readNextToken();
		leaveParser("named constant");
		return nm;
	}
	@Override public String identify() {
		return "<named constant> " + name + " on line " + lineNum;
		}
	
	@Override	
 void prettyPrint() {
	// TODO Auto-generated method stub
	
	/*System.out.println("namend const prttypnt");*/
	Main.log.prettyPrint(name);
}
	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
	PascalDecl d =curScope.findDecl(name,this);
	
		
	}

}
