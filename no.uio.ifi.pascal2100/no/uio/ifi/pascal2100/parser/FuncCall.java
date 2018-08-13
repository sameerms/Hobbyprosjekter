package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;



/**
 * <h1>FuncCall</h1>
 *
 * <p>Parse a Pascal FuncCall as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class FuncCall extends Factor {

	public Factor fa;
	public  String name ;
	Expression exp;
	Expression firstexp;

	public FuncCall(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	
	
	  /**
     * Parse a FuncCall.
     * @param Scanner Tokens.
     * @return the FuncCallobject of the parse tree.
     *--name--- (--- expression----,--- )---
     */
	
	public static FuncCall parse(Scanner s) {
		enterParser("func call");
		FuncCall fc=new FuncCall (s.curLineNum());
		s.test(nameToken);
		fc.name=s.curToken.id;
	
	
		s.readNextToken();
		
		if(s.curToken.kind == leftParToken){
			s.skip(leftParToken);
			fc.firstexp=Expression.parse(s);
			Expression tempexp=fc.firstexp;
		
			while(s.curToken.kind == commaToken){
				s.skip(commaToken);
				tempexp.nextexp= tempexp=Expression.parse(s);
			}
			s.skip(rightParToken);
			
		}
			
		leaveParser("func call");
		return fc;
		
		
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<func call> "  +name+ " on line " + lineNum;
	}

	
	// method for � printe ut programmet
	@Override void prettyPrint() {
	
		Expression localexp= firstexp;
		if (firstexp != null){
			Main.log.prettyPrint("(");

		while (localexp!=null){
			localexp.prettyPrint();

			localexp=localexp.nextexp;
		if(localexp != null)Main.log.prettyPrint(" , ");

		}
		Main.log.prettyPrint(")");
		}
	}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		
		PascalDecl d = curScope.findDecl(name,this);
		Expression localexp= firstexp;
		if (firstexp != null){
			

		while (localexp!=null){
			localexp.check(curScope, lib);

			localexp=localexp.nextexp;
		

		}
	}
			
}
}
