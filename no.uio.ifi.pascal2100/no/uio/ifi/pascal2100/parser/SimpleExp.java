package no.uio.ifi.pascal2100.parser;

import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.scanner.Scanner;



/**
 * <h1>SimpleExp</h1>
 *
 * <p>Parse a Pascal SimpleExp as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class SimpleExp extends PascalSyntax {

	public Expression expr;
	static PrefixOperator pfOp;
	static TermOperator tmOp;
	static Term tm1,tm2;
	Term tx;
	Operator firstOpr = null;
	public static List <Term>termlist = new ArrayList<Term>(); 

	public SimpleExp(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<simple expr> "  + " on line " + lineNum;
	}
	

	/**
     * Parse a SimpleExp.
     * @param Scanner Tokens.
     * @return the SimpleExp object of the parse tree.
     *-- prefix opr -----term ----term opr---
     */
	
	
	
	public static SimpleExp parse(Scanner s) {
		enterParser("simple expr ");
		SimpleExp  exp = new SimpleExp (s.curLineNum());
		
		
		if (s.curToken.kind.isPrefixOpr()){
			exp.pfOp=PrefixOperator.parse(s);
		}
		
		exp.tx = Term.parse(s);
        Term localTm= exp.tx;
        TermOperator firstOpr = null;
        while (s.curToken.kind.isTermOpr()) {
            TermOperator localTermOpr = TermOperator.parse(s);
            if (firstOpr == null) 
                exp.firstOpr = firstOpr = localTermOpr;
            else
                firstOpr.nextOpr = firstOpr = localTermOpr;
            localTm.nextTerm = localTm = Term.parse(s);
            
        }
		
		
		leaveParser("simple expr");
		return exp;
		}
	
	@Override void prettyPrint() {
	
	if (pfOp !=null) pfOp.prettyPrint();
	 Term localTerm = tx;
     for (Operator localOperator = firstOpr; ; localOperator = localOperator.nextOpr) {
         localTerm.prettyPrint();
         localTerm = localTerm.nextTerm;
         if (localOperator == null)
             break;
         localOperator.prettyPrint();
         
     }
         
 }

	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if (pfOp !=null) pfOp.check(curScope, lib);
		 Term localTerm = tx;
	     for (Operator localOperator = firstOpr; ; localOperator = localOperator.nextOpr) {
	         localTerm.check(curScope, lib);
	         localTerm = localTerm.nextTerm;
	         if (localOperator == null)
	             break;
	         localOperator.check(curScope, lib);
	         
	     }
		
	}


}