package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import static no.uio.ifi.pascal2100.scanner.TokenKind.leftBracketToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.ofToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.rightBracketToken;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;


/**
 * <h1>RangeType</h1>
 *
 * <p>Parse a Pascal RangeType as per project jernbarnediagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 */
public class RangeType extends Type {
Constant c1,c2;
	public RangeType(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	
	
	 /**
     * Parse a RangeType.
     * @param Scanner Tokens.
     * @return the RangeType object of the parse tree.
     * constant .. constant
     */
	public static RangeType parse(Scanner s) {
		enterParser("range-type");
		RangeType et= new RangeType(s.curLineNum());
		et.c1=Constant.parse(s);
		/*s.readNextToken();*/
		s.skip(rangeToken);
		/*System.out.println("range"+s.curToken.id);*/
		et.c2=Constant.parse(s);
		
		leaveParser("range-type");
		return et;
}
	
	@Override public String identify() {
		return "<range-type> " +  " on line " + lineNum;
		}
	
	
	 @Override
		public void prettyPrint() {
			
		if(c1 != null) c1.prettyPrint();
		 Main.log.prettyPrint("..");
		 if(c2 != null) c2.prettyPrint();
		  Main.log.prettyIndent();
		
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if(c1 != null) c1.check(curScope, lib);
		if(c2 != null) c2.prettyPrint();
		
	}
}