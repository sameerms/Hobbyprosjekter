package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class Numberliteral extends Constant {

	int num;
	public Numberliteral(int n) {
		super(n);
		
	}
	public static Numberliteral parse(Scanner s) {
		enterParser("number literal");
		Numberliteral nm= new Numberliteral (s.curLineNum());
		s.test(intValToken);
		nm.num=s.curToken.intVal;
	
		numberliteral=s.curToken.intVal;
		
		s.readNextToken();
		
		leaveParser("number literal");
		return nm;
	}
	@Override public String identify() {
		return "<number literal> " + num + " on line " + lineNum;
		}
	
	@Override	
 void prettyPrint() {
	Main.log.prettyPrint(Integer.toString(num));
	}
	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
	}
}
