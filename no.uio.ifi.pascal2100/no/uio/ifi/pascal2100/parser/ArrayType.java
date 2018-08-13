package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.*;
import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class ArrayType extends Type {
Type tp,tp2;

	public ArrayType(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}


    /**
     * Parse a ArrayType.
     * @param Scanner Tokens.
     * @return the ArrayType object of the parse tree.
     * array --[---- type--- ]--- of--- type
     */
	public static ArrayType parse(Scanner s) {
		enterParser("array-type");
		ArrayType et= new ArrayType(s.curLineNum());
		s.skip(arrayToken);
		s.skip(leftBracketToken);
		
		/*System.out.println("f�r type"+s.curToken.kind);*/
		et.tp=Type.parse(s);
		
		s.skip(rightBracketToken);
		s.skip(ofToken);
		/*System.out.println("etter of"+s.curToken.kind);*/
		et.tp2=Type.parse(s);
		
		leaveParser("array-type");
		return et;
}
	
	@Override public String identify() {
		return "<array-type> " +  " on line " + lineNum;
		}
	 @Override
		public void prettyPrint() {
			
		 
		 Main.log.prettyPrint("array "); 
		 Main.log.prettyPrint("[");
		 tp.prettyPrint();
		 Main.log.prettyPrint("]  of");
		 tp2.prettyPrint();
		  Main.log.prettyIndent();
		
		}


	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		if (tp!=null) tp.check(curScope, lib);
		if (tp2!=null) tp2.check(curScope, lib);
		
		
	}
}
