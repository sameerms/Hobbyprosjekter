package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

public class PrefixOperator extends Operator {

	public SimpleExp smpexp;
	public static String symbol;
	public PrefixOperator(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	public static PrefixOperator parse(Scanner s) {
		// TODO Auto-generated method stub
		
		enterParser("prefix opr");
		PrefixOperator localpfOpr = new PrefixOperator(s.curLineNum());
		localpfOpr.oprToken=s.curToken.kind;
		s.readNextToken();
		
		leaveParser("prefix opr");
		return localpfOpr;
		}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<prefix opr> "+symbol  + " on line " + lineNum;
	}
	
	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		String op= "";
		
		/*System.out.println("prefix oper token called");*/
		switch (oprToken) {
		case addToken:        op = "+";  break;
		case subtractToken:     op = "-";  break;
		}
		Main.log.prettyPrint(" " + op + " ");
	}
	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
	}
		
}


