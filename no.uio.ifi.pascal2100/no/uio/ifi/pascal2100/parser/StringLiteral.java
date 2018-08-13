package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class StringLiteral extends Constant {

	 String text;
	public StringLiteral(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	public static StringLiteral parse(Scanner s) {
		enterParser("string literal");
		
		StringLiteral sl= new StringLiteral (s.curLineNum());
		sl.text=s.curToken.strVal;
		s.skip(stringValToken);
		leaveParser("string literal");
		return sl;
	}
	@Override public String identify() {
		return "<string literal> " + text + " on line " + lineNum;
		}
	
		
	@Override 
	void prettyPrint() {
	// TODO Auto-generated method stub
	/*System.out.println("strng lteral prttypnt");*/
	Main.log.prettyPrint("'");
	Main.log.prettyPrint(text);
	Main.log.prettyPrint("'");
}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
	}
}