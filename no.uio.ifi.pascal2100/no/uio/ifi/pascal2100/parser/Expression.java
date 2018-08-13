package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;



/**
 * <h1>Expression </h1>
 *
 * <p>Parse a Pascal Expression as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class Expression extends PascalSyntax {
	
	public  Operator relop;
	public IfStatm ifstat;
	public AssignStatm assignst;
	public Variable varibl;
	public ProcCallStatm proccall;
	public SimpleExp smpexpr,smpexpr1= null;
	public FuncCall fccall;
	public InnerExp inex;
	public Expression nextexp;
	public static List <SimpleExp>explist = new ArrayList<SimpleExp>(); 

	public Expression(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<expression> "  + " on line " + lineNum;
	}
	
	
	

    /**
     * Parse a Expression.
     * @param Scanner Tokens.
     * @return the Expression object of the parse tree.
     *--- simple expr ---rel opr---- simple expr----
     */

	public static Expression parse(Scanner s) {
		enterParser("expression ");
		Expression  exp = new Expression (s.curLineNum());
		
		exp.smpexpr = SimpleExp.parse(s);exp.smpexpr.expr=exp;
		explist.add(exp.smpexpr);
		
		if (s.curToken.kind.isRelOpr()){
			exp.relop=RelOperator.parse(s);
			
			exp.smpexpr1 = SimpleExp.parse(s);
			explist.add(exp.smpexpr1);
			
			
		}
		
		leaveParser("expression");
		return exp;
		}
	
@Override void prettyPrint() {
	
	if (smpexpr != null) smpexpr.prettyPrint();
	if (relop != null){relop.prettyPrint();
	if (smpexpr1 != null) smpexpr1.prettyPrint();}
}
@Override
public void check(Block curScope, Library lib) {
	// TODO Auto-generated method stub
	if (smpexpr != null) smpexpr.check(curScope, lib);
	if (relop != null){relop.check(curScope,  lib);
	if (smpexpr1 != null) smpexpr1.check(curScope,  lib);}
}
}

