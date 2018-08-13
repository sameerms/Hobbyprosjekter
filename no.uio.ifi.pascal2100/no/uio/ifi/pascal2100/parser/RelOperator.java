package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;



/*
 * A <rel oprator> (=, <>, <, <=, > or >=).
 */
public class RelOperator extends Operator {

	
	public Expression smpexp;
	String symbol ;
	
	public RelOperator(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	public static RelOperator parse(Scanner s) {
		// TODO Auto-generated method stub
		
		enterParser("rel operator");
		RelOperator localRelOpr = new RelOperator(s.curLineNum());
		localRelOpr.oprToken = s.curToken.kind;
		localRelOpr.symbol=s.curToken.id;
		s.readNextToken();
		
		leaveParser("rel operator");
		return localRelOpr;
		}
	
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<rel opr> "+symbol  + " on line " + lineNum;
	}
	
	
	@Override
	void prettyPrint() {
		// TODO Auto-generated method stub
		String op= "";

		switch (oprToken) {
		case equalToken:        op = "=";  break;
		case notEqualToken:     op = "<>";  break;
		case lessToken:         op = "<";   break;
		case lessEqualToken:    op = "<=";  break;
		case greaterToken:      op = ">";   break;
		case greaterEqualToken: op = ">=";  break;
		}
		/*System.out.println( "op rel op value " + op);*/
		Main.log.prettyPrint(" " + op + " ");
}

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
	}
}
