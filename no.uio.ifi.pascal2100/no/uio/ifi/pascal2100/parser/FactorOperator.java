package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;


public class FactorOperator extends Operator {

	public Term tm;	
	public String symbol;
	static FactorOperator fot = null;

	public FactorOperator(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	public static FactorOperator parse(Scanner s) {
		
		enterParser("factor opr");
		FactorOperator localfactOpr = new FactorOperator(s.curLineNum());
		
		/*System.out.println("facotr oprs"+ s.curToken.id);*/
		 if (s.curToken.id=="*")localfactOpr.oprToken =nameToken;
		 
		 else {
			 localfactOpr.oprToken=s.curToken.kind;
			 
		 }
		
		leaveParser("factor opr");
		return localfactOpr;
		}
	
@Override
public String identify() {
	// TODO Auto-generated method stub
	return "<factor opr> "+symbol  + " on line " + lineNum;
	
	
}
	

@Override
	public void prettyPrint() {
		// TODO Auto-generated method stub
		
		String op= "";
		switch (oprToken) {
		case divToken:     op = "div";  break;
		case modToken:     op = "mod";  break;
		case andToken:     op = "and";   break;
		
		case nameToken:   /*if(oprToken.isFactorOpr()) */ op = "*";  break;
		default:
			break;
		}
		
		Main.log.prettyPrint(" " + op + " ");
}

@Override
public void check(Block curScope, Library lib) {
	// TODO Auto-generated method stub
	
}
		
		
	}

