package no.uio.ifi.pascal2100.parser;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.*;

abstract class Constant extends Factor {

	public ConstDecl Constdecle;
	public ConstDeclPart constfrm;
	public ConstDeclPart constDeclfrm;
	public RangeType rgt;
	static CharLiteral ct;
	public Factor fct;
	public static Constant tp =null;
	int number;
	


	 Constant(int n) {
		super(n);
		
	}
	
	@Override
	public String identify() {
		
		return "<constant> " +  " on line " + lineNum;
	}

	
	static Constant parse(Scanner s) {
		
		enterParser("constant");
		
		
		switch (s.curToken.kind ) {
		case nameToken:
			tp =NamedConst.parse(s);
			break;
		
		case intValToken:
			tp = Numberliteral.parse(s); break;
		case stringValToken:
			
			if(s.curToken.strVal .length() ==1){
				tp = CharLiteral.parse(s); 
				}
			else {
				tp = StringLiteral.parse(s); 
				}break;	
		
		default:
		tp = StringLiteral.parse(s); break;
		}
		leaveParser("constant");
		
		return 	tp;
	}
	
	@Override void prettyPrint() {
		
	}


	}