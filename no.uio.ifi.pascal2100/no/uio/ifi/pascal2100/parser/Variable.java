package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>Variable</h1>
 *
 * <p>Parse a Pascal Variable as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class Variable extends Factor {

	public String name;
	public AssignStatm assignst;
	Expression  exp;
	public Factor fa;

	public Variable(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}

	
	/**
     * Parse a Variable.
     * @param Scanner Tokens.
     * @return the Variable object of the parse tree.
     * ---name ---[ --expression --]--
     */

	public static Variable parse(Scanner s){
		enterParser("variable");
		Variable vb=new Variable(s.curLineNum());
		s.test(nameToken);
		vb.name=s.curToken.id;
	
		
		s.readNextToken();
		
		if(s.curToken.kind == leftBracketToken){
			s.skip(leftBracketToken);
		
			vb.exp=Expression.parse(s);vb.exp.varibl=vb;
			/*s.readNextToken();*/
			s.skip(rightBracketToken);
		}
		
		
		leaveParser("variable");
		return vb;
	}
	
	
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<variable> "  +name+ " on line " + lineNum;
	}

	
	
	
	@Override void prettyPrint() {

		/*System.out.println("named vab 2" +named);*/
		Main.log.prettyPrint(name);
		if (exp!=null){
		Main.log.prettyPrint(" [ ");
		exp.prettyPrint();
		Main.log.prettyPrint(" ] ");
		}
		
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
		PascalDecl d = curScope.findDecl(name,this);
		exp.check(curScope, lib);
	}
		
}
