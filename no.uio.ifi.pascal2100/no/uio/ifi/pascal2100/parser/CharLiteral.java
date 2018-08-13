package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.stringValToken;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class CharLiteral extends Constant {

	public char c;
	
	public CharLiteral(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	public static CharLiteral parse(Scanner s) {
		enterParser("char literal");
		/*System.out.println("char literal parser");*/
		CharLiteral sl= new CharLiteral (s.curLineNum());
		sl.c=s.curToken.strVal.charAt(0);
		s.readNextToken();
		leaveParser("char literal");
		return sl;
	}
	@Override public String identify() {
		return "<char literal> " + c + " on line " + lineNum;
		}
	
	@Override
	void prettyPrint() {
	// TODO Auto-generated method stub
	/*System.out.println("char prt prttypnt");*/
	Main.log.prettyPrint("'");
	Main.log.prettyPrint(Character.toString(c));
	Main.log.prettyPrint("'");
}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
		
	}
}
